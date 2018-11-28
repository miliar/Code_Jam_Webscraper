#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;
#define GI ({int t;scanf("%d",&t);t;})
typedef pair<int,int> ii;
#define INF (int)1e8

vector<ii> adj[101][101];
vector<ii> MN;
vector<ii> V[26];
vector<ii> st;
bool reach[26];
int A[101][101];

int main() {
  int t = GI;
  for (int cas = 1; cas <= t; cas++) {
    st.clear();
    MN.clear();
    memset(reach,0,sizeof(reach));
    for (int i = 0; i < 26; i++)
      V[i].clear();
    int M = GI, N = GI;
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
	A[i][j] = GI;
	adj[i][j].clear();
      }
    }
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
	int mn = A[i][j];
	int adjj = -1, adji = -1;
	if (i > 0 && A[i-1][j] < A[i][j] && mn > A[i-1][j]) {
	    mn = A[i-1][j];
	    adji = i-1, adjj = j;
	}
	if (j > 0 && A[i][j-1] < A[i][j] && mn > A[i][j-1]) {
	    mn = A[i][j-1];
	    adji = i, adjj = j-1;
	}
	if (j < N-1 && A[i][j+1] < A[i][j] && mn > A[i][j+1]) {
	    mn = A[i][j+1];
	    adji = i, adjj = j+1;
	}
	if (i < M-1 && A[i+1][j] < A[i][j] && mn > A[i+1][j]) {
	    mn = A[i+1][j];
	    adji = i+1, adjj = j;
	}
	if (adji == -1) {
	  st.push_back(ii(i,j));
	  continue;
	}
	adj[adji][adjj].push_back(ii(i,j));
      }
    }
    /*for (int i = 0; i < st.size(); i++) {
      printf("%d %d\n",st[i].first, st[i].second);
      }*/
    MN.resize(st.size());
    for (int k = 0; k < st.size(); k++) {
      ii mn = st[k];
      queue<ii> Q;
      Q.push(mn);
      while (!Q.empty()) {
	ii u = Q.front();
	V[k].push_back(u);
	mn = min(mn,u);
	int r = u.first, c = u.second;
	Q.pop();
	for (int i = 0; i < adj[r][c].size(); i++) {
	  Q.push(adj[r][c][i]);
	}
      }
      MN[k] = mn;
    }
    /*for (int i = 0; i < st.size(); i++) {
      printf("\n%d\n",i);
      for (int j = 0; j < V[i].size(); j++) {
	printf("%d %d\n",V[i][j].first,V[i][j].second);
      }
    }
    printf("\nMN\n");
    for (int i = 0; i < st.size(); i++) {
      printf("%d %d\n",MN[i].first,MN[i].second);
    }
    printf("\n");*/
    for (int i = 0; i < st.size(); i++) {
      int m;
      for (m = 0; m < st.size(); m++)
	if (!reach[m]) {
	  break;
	}
      for (int j = m+1; j < st.size(); j++) {
	if (!reach[j] && MN[j] < MN[m]) {
	  m = j;
	}
      }
      //printf("%d\n",m);
      reach[m] = true;
      for (int j = 0; j < V[m].size(); j++) {
	A[V[m][j].first][V[m][j].second] = i;
      }
    }
    printf("Case #%d:\n",cas);
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++)
	printf("%c ",A[i][j]+'a');
      printf("\n");
    }
  }
}
