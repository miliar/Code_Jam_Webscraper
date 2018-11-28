#include<cstdio>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<list>
#include<stack>
#include<map>
#include<queue>
#include<climits>

#define FOR(i,a,b) for(int i=(int)(a); i<(int)(b); ++i)
#define FORE(it,C) for(__typeof(C.begin()) it=C.begin(); it!=C.end(); ++it)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

using namespace std;

const int max_n = 100; // maksymalne liczba wierzcholkow po obu stronach

int n1, n2;              // wejscie: liczby wierzcholkow po obu stronach
bool edge[max_n][max_n]; // wejscie: macierz sasiedztwa (mozna zmienic na liste)
int mate1[max_n], mate2[max_n]; // wynik: wierzcholki skojarzone (-1 ozn. brak)
int dist1[max_n], dist2[max_n];

bool search(int b) {
  for (int a = 0; a < n1; ++a) // <- tu zmienic
   if (edge[a][b] && dist1[a] == dist2[b]-1) {
    dist1[a] = INT_MAX;
    if (mate1[a] == -1 || search(mate1[a])) {
      mate1[a] = b;
      mate2[b] = a;
      return true;
    }
  }
  return false;
}

int compute_bcm() {
  fill_n(mate1, n1, -1);
  fill_n(mate2, n2, -1);
  int result = 0;
  for (;;) {
    queue<int> Q;
    for (int a = 0; a < n1; ++a) {
      if (mate1[a] == -1) {
        dist1[a] = 0;
        Q.push(a);
      }
      else dist1[a] = INT_MAX;
    }
    fill_n(dist2, n2, INT_MAX);
    int max_dist = INT_MAX;
    while (!Q.empty()) {
      int a = Q.front();
      Q.pop();
      if (dist1[a] > max_dist) break;
      for (int b = 0; b < n2; ++b) // <- tu zmienic
       if (edge[a][b] && dist2[b] == INT_MAX) {
        dist2[b] = dist1[a]+1;
        if (mate2[b] == -1) max_dist = dist2[b];
        else {
          dist1[mate2[b]] = dist2[b]+1;
          Q.push(mate2[b]);
        }
      }
    }
    if (max_dist == INT_MAX) break;
    for (int b = 0; b < n2; ++b)
     if (mate2[b] == -1 && dist2[b] != INT_MAX && search(b)) ++result;
  }
  return result;
}

const int nMax = 105;
const int kMax = 30;

int tabN[nMax][kMax];
bool canBe[nMax][nMax];
bool vis[nMax];

void testcase(int testNr) {

	int N,K;
	scanf("%d %d",&N,&K);
	
	FOR(i,0,N) FOR(j,0,K)
		scanf("%d",&tabN[i][j]);
		
	FOR(i,0,N) FOR(j,0,N) {
		canBe[i][j] = true;
		bool iUp = false;
		bool jUp = false;
		FOR(k,0,K) {
			if(tabN[i][k] >= tabN[j][k])
				iUp = true;
			if(tabN[j][k] >= tabN[i][k])
				jUp = true;
		}
		if(iUp && jUp)
			canBe[i][j] = false;
	}
	
	vector<int> chain;
	FOR(i,0,N) vis[i] = false;
	
	for(int z=0; z<N;) {
		vector<int> cands;
		FOR(i,0,N) if(!vis[i]) {
			bool isLow = false;
			FOR(k,0,K) {
				bool isOk = true;
				FOR(j,0,N) if(!vis[j] && tabN[j][k]<tabN[i][k]) {
					isOk = false;
					break;
				}
				if(isOk) {
					isLow = true;
					break;
				}
			}
			if(isLow)
				cands.PB(i);
		}
		FOR(i,0,cands.size())
			vis[cands[i]] = true;
		while(true) {
			bool any = false;
			FOR(i,0,N) if(!vis[i]) {
				bool isOk = true;
				FOR(j,0,cands.size()) if(canBe[i][cands[j]]) {
					isOk = false;
					break;
				}
				if(isOk) {
					cands.PB(i);
					vis[i] = true;
					any = true;
				}
			}
			if(!any)
				break;
		}
		
		n1 = chain.size();
		n2 = cands.size();
		
		FOR(i,0,n1) FOR(j,0,n2)
			edge[i][j] = canBe[chain[i]][cands[j]];
			
		compute_bcm();
		
		FOR(j,0,n2) if(mate2[j]>=0)
			chain[mate2[j]] = cands[j]; else
			chain.PB(cands[j]);
		
		FOR(i,0,cands.size())
			vis[cands[i]] = true;
		z += cands.size();
		
		/*FOR(i,0,chain.size())
			printf("%d ",chain[i]);
		printf("\n");*/
	}
	
	int res = chain.size();
	printf("Case #%d: %d\n", testNr, res);
}

int main() {
	int t;
	scanf("%d",&t);
	FOR(i,0,t)
		testcase(i+1);
}
