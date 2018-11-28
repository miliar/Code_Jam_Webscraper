
#include <algorithm>
#include <cstdio>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#define INF (1 << 30)

using namespace std;

int N;
string a[40];
int ind[40];
int dist[40320];

int prod[8] = {5040, 720, 120, 24, 6, 2, 1, 1};

vector <int> init(8);

vector <int> decode(int mask)	{
	vector <int> ret(8), t = init;
	int u, v;
	for(u = 0; u < 8; u++)	{
		v = mask / prod[u];
		ret[u] = t[v];
		t.erase(t.begin() + v);
		mask -= v * prod[u];
	}
	return ret;
}

int encode(vector <int> num)	{
	int u, v, mask = 0;
	vector <int> t = init;
	for(u = 0; u < 8; u++)	{
		for(v = 0; t[v] != num[u]; v++);
		mask += v * prod[u];
		t.erase(t.begin() + v);
	}
	return mask;
}

void generate() {
  for(int i = 0; i < 40320; i++)
    dist[i] = INF;
  for(int i = 0; i < 8; i++)
    init[i] = i;
  
  dist[0] = 0;
  vector <int> q;
  q.push_back(0);
  for(int i = 0; i < q.size(); i++) {
    vector <int> perm = decode(q[i]);
    
    for(int j = 0; j < 7; j++) {
      int t = perm[j];
      perm[j] = perm[j + 1];
      perm[j + 1] = t;
      
      int ni = encode(perm);
      
      if(dist[ni] == INF) {
        dist[ni] = dist[q[i]] + 1;
        q.push_back(ni);
      }
      
      t = perm[j];
      perm[j] = perm[j + 1];
      perm[j + 1] = t;
    }
    
  }
  for(int i = 0; i < 50; i++) {
    printf("%d %d\n", i, dist[i]);  
  }
  system("pause");
}

int solve() {
  
  
  for(int i = 0; i < N; i++) {
    ind[i] = -1;
    for(int j = 0; j < N; j++)
      if(a[i][j] == '1')
        ind[i] = j;
  }
  
  int best = 10000000;
  for(int i = 0; i < 40320; i++) {
    vector <int> perm = decode(i);
    int j = 0;
    for(; j < N; j++)
      if(perm[j] >= N || ind[perm[j]] > j) break;
      
    if(j == N && dist[i] < best)
      best = dist[i];
  }
  
  return best;
}

int main() {
  generate();
  
  FILE *fout = fopen("A-small1.out", "w");
  ifstream fin("A-small-attempt1.in");
  string w;
  getline(fin, w);
  int T = atoi(w.c_str());
  for(int i = 1; i <= T; ++i) {
    getline(fin, w);
    N = atoi(w.c_str());
    for(int j = 0; j < N; j++)
      getline(fin, a[j]);
      
    fprintf(fout, "Case #%d: %d\n", i, solve());
  }
  
  return 0;
}
