#include <iostream>
#include <utility>
#include <queue>

using namespace std;

#define MAXV 500
#define MAXA 500

int al[MAXV][MAXA], ral[MAXV][MAXA], flow[MAXV][MAXA], cap[MAXV][MAXA];
int nadj[MAXV], capres[MAXV]; bool visited[MAXV]; pair<int, int> anterior[MAXV];

void init() { for(int i = 0; i < MAXV; i++) { nadj[i] = 0; capres[i] = 1000000000; } }

int bfs(int source, int sink)
{
    queue<int> q; q.push(source);
    while(!q.empty())
    {
      int cur = q.front(); q.pop();
      if(visited[cur]) continue; visited[cur] = true;
     
      for(int i = 0; i < nadj[cur]; i++)
      {
        if(cap[cur][i] - flow[cur][i] <= 0 || visited[al[cur][i]]) continue;       
        anterior[al[cur][i]] = make_pair(cur, i);
        capres[al[cur][i]] = min(capres[cur], cap[cur][i] - flow[cur][i]);
        q.push(al[cur][i]); if(al[cur][i] == sink) return capres[sink];       
      }
    }
    return 0;
}

void aresta(int origem, int destino, int c)
{
  al[origem][nadj[origem]] = destino; al[destino][nadj[destino]] = origem;
  cap[origem][nadj[origem]] = c; cap[destino][nadj[destino]] = 0;
  flow[origem][nadj[origem]] = 0; flow[destino][nadj[destino]] = 0;
  ral[destino][nadj[destino]] = nadj[origem]; ral[origem][nadj[origem]] = nadj[destino];               

  nadj[origem]++; nadj[destino]++;
}

int mflow(int source, int sink)
{
  for(int i = 0; i < MAXV; i++) visited[i] = false;
  int tmp, maxflow = 0;

  while((tmp = bfs(source, sink)) != 0)
  {
    int prev = sink;
    while(prev != source)
    {
      flow[anterior[prev].first][anterior[prev].second] += tmp;
      flow[prev][ral[anterior[prev].first][anterior[prev].second]] -= tmp;     
      prev = anterior[prev].first;
    }
    maxflow += tmp;               
    for(int i = 0; i < MAXV; i++) visited[i] = false;   
  }
 
  return maxflow;
}

int main()
{
    int T;
    cin >> T;
    for(int z = 1; z <= T; z++)
    {
	init();
	int N, K;
	cin >> N >> K;
       
	int vals[N][K];
	for(int i = 0; i < N; i++)
	    for(int j = 0; j < K; j++)
		cin >> vals[i][j];

	for(int i = 0; i < N; i++)
	{
	    aresta(0, 1 + i, 1);
	    for(int j = 0; j < N; j++)
	    {
		bool edge = true;
		for(int k = 0; k  < K; k++)
		    if(vals[i][k] >= vals[j][k]) 
			edge = false;

		if(edge)
		    aresta(1 + i, N + 1 + j, 1);
	    }
	    aresta(1 + i + N, 2*N + 1, 1);
	}

	cout << "Case #" << z << ": " << N - mflow(0, 2*N + 1) << endl;
    }
}
