#include <vector>
#include <iostream>
#include <algorithm>
#include <utility>
#include <map>
#include <cmath>
#include <queue>

using namespace std;

const int INF = 1000000000;

int R, C;
#define MAXV 300
#define MAXA 20

int pesos[MAXV][MAXA], adj[MAXV][MAXA];
int nadj[MAXV], shortest[MAXV]; bool visited[MAXV];

void init() { memset(nadj, 0, sizeof(nadj)); }

void aresta(int i, int j, int peso)
{
  //  cout << "A: " << i/C << " - " << i % C << " - " << j/C << " - " << j % C << " - " << peso << endl;
  for(int k = 0; k < nadj[i]; k++)
    if(adj[i][k] == j) return;
  adj[i][nadj[i]] = j;
  pesos[i][nadj[i]++] = peso;
}

int dijkstra(int inicio, int fim)
{
  priority_queue<pair<int, int> > q;
  q.push(make_pair(0, inicio));

  for(int i = 0; i < MAXV; i++) { shortest[i] = INF; visited[i] = false; }
  shortest[inicio] = 0;

  while(!q.empty())
  {
    int v = q.top().second; q.pop();
    if(visited[v]) continue; visited[v] = true;
    for(int i = 0; i < nadj[v]; i++)
    {
	shortest[adj[v][i]] = min(shortest[adj[v][i]], shortest[v] + pesos[v][i]);
      q.push(make_pair(-shortest[adj[v][i]], adj[v][i]));
    }
  }

  return shortest[fim]; 
}

int main()
{
    int n;
    cin >> n;
    
    for(int z = 0; z < n; z++)
    {
        init();
	int retVal = 0;

	cin >> R >> C;

	int reach[R][C][4];
	int dx[4] = {1, -1, 0, 0};
	int dy[4] = {0, 0, 1, -1};
	int starti, startj, endi, endj;
	char bo[R][C];

	for(int i = 0; i < R; i++)
	    for(int j = 0; j < C; j++)
	    {
		char c; cin >> c;
		bo[i][j] = c;
		if(bo[i][j] == 'O') starti = i, startj = j;
		else if(bo[i][j] == 'X') endi = i, endj = j;
	    }

	for(int i = 0; i < R; i++)
	  for(int j = 0; j < C; j++)
	  {
	    if(bo[i][j] == '#') continue;
	      int k;
	      for(k = i; k >= 0; k--)
		  if(bo[k][j] == '#') 
		  { reach[i][j][0] = k + 1; break; }
	      if(k == -1) reach[i][j][0] = 0;

	      for(k = i; k < R; k++)
		  if(bo[k][j] == '#') 
		  { reach[i][j][1] = k - 1; break; }
	      if(k == R) reach[i][j][1] = R - 1;


	      for(k = j; k >= 0; k--)
		  if(bo[i][k] == '#')
		  { reach[i][j][2] = k + 1; break; }
	      if(k == -1) reach[i][j][2] = 0;

	      for(k = j; k < C; k++)
		  if(bo[i][k] == '#') 
		  { reach[i][j][3] = k - 1; break; }
	      if(k == C) reach[i][j][3] = C - 1;

	      //	      cout << i << " - " << j << " - " << reach[i][j][0] << " - " << reach[i][j][1] << " - " << reach[i][j][2] << " - " << reach[i][j][3] << " - " << endl;
	  }


	//	cout << "A" << endl;
	for(int i = 0; i < R; i++)
	    for(int j = 0; j < C; j++)
	    {	    if(bo[i][j] == '#') continue;

		for(int k = 0; k < 4; k++)
		{
		    int new_i = i + dx[k], new_j = j + dy[k];
		    if(new_i < 0 || new_i >= R || new_j < 0 || new_j >= C)
			continue;

		    if(bo[new_i][new_j] == '#')
			continue;

		    aresta(C*i + j, C*new_i + new_j, 1);
		}
		
		int mini = 999999999;
		mini = min(mini, i - (reach[i][j][0] - 1));
		mini = min(mini, (reach[i][j][1] + 1) - i);
		mini = min(mini, j - (reach[i][j][2] - 1));
		mini = min(mini, (reach[i][j][3] + 1) - j);

		//		cout << "A"<< endl;
		aresta(C*i + j, C*reach[i][j][0] + j, mini);
		//		cout << "B" << endl;
 		aresta(C*i + j, C*reach[i][j][1] + j, mini);
		//		cout << "C" << endl;
		aresta(C*i + j, C*i + reach[i][j][2], mini);
		//		cout << "D" << endl;
		aresta(C*i + j, C*i + reach[i][j][3], mini);
	    }

		//		cout << "B" << endl;

		//		cout << C*endi + endj << endl;
	int ret = dijkstra(C*starti + startj, C*endi + endj);
	if(ret >= 999999999)
	    cout << "Case #" << z + 1 << ": THE CAKE IS A LIE" << endl;
	else
	    cout << "Case #" << z + 1 << ": " << ret << endl;
    }
}
