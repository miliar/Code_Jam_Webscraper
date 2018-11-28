#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cfloat>
#include <cstring>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

using namespace std;

int R, C;
vector <string> M;

struct nodo
{
	int n;
	vector < pair <int, int> > v;
	bool ok;
	nodo(int a, vector < pair <int, int> > b, bool c)
	{
		n = a;
		v = b;
		ok = c;
	}
	void norm()
	{
		sort(all(v));
	}
};

map < vector < pair <int, int> >, bool > visited;

//bool visited[(12*12)*(4)*(2*4)*(3*4)*(4*7)];

int dx[8] = {0, 0, 1, -1, 1, 1, -1, -1};
int dy[8] = {1, -1, 0, 0, 1, -1, 1, -1};

bool safe(nodo e)
{
	int used[e.n];
	memset(used, 0, sizeof(used));
	queue <int> Q;
	Q.push(0);
	used[0] = 1;
	
	while(!Q.empty())
	{
		int q = Q.front();
		Q.pop();
		
		for(int i=0; i<e.n; i++)
		{
			if(!used[i])
			{
				for(int k=0; k<4; k++)
				{
			 		if(e.v[q].first + dx[k] == e.v[i].first && e.v[q].second + dy[k] == e.v[i].second)
					{	
						Q.push(i);
						used[i] = 1;
					}
				}
			}
		}
	}
	for(int i=0; i<e.n; i++)
		if(!used[i]) return 0;
	return 1;
}

bool visitado(nodo e)
{
	e.norm();
	return visited[e.v];
}

void visitar(nodo e)
{
	e.norm();
	
	visited[e.v] = 1;
	/*
	if(e.n == 1)
	{
		visited[e.v[0].first * 12 + e.v[0].second] = 1;
	}
	else if(e.n == 2)
	{
		for(int k=0; k<8; k++)
		{
			if(e.v[0].first + dx[k] == e.v[1].first && e.v[0].second + dy[k] == e.v[1].second)
			{
				visited[e.v[0].first * 12 * 8 + e.v[0].second * 8 + k] = 1;
			}
		}
	}
	else
	{
		int ind = -1;
		for(int i=0; i<e.v.size(); i++)
		{
			for(int j=0; j<e.v.size(); j++)
			{
				if(i!=j && (v[i].first == v[j].first) || (v[i].second == v[j].second))
				{
					ind = i;
					break;
				}
			}
			if(ind != -1) break;
		}
		
		vector < pair <int, int> > mask;
		mask.push_back(make_pair(e.v[ind].first, 12));
		mask.push_back(make_pair(e.v[ind].second, 12));
		
		bool used[5];
		memset(used, 0, sizeof(used));
		
		queue <int> Q;
		Q.push(ind);
		used[ind] = 1;
		int cnt = 1;
		
		while(!Q.empty())
		{
			int q = Q.front();
			Q.pop();
			
			for(int i=0; i<e.n; i++)
			{
				if(!used[i])
				{
					for(int k=0; k<4; k++)
					{
				 		if(e.v[q].first + dx[k] == e.v[i].first && e.v[q].second + dy[k] == e.v[i].second)
						{
							mask.push_back(make_pair(i, cnt));
							if(cnt == q.n - 1) mask.push_back(make_pair(k, 8));
							else mask.push_back(make_pair(k, 4));
							
							Q.push(i);
							used[i] = 1;
							cnt++;
						}
					}
				}
			}
		}
		
		if(cnt < e.n)
		{
			int malo = -1;
			for(int i=0; i<e.n; i++)
				if(!used[i])
					malo = i;
			
			for(int i=0; i<e.n; i++)
			{
				for(int k=0; k<8; k++)
				{
					if(e.v[i].first + dx[k] == e.v[i].first && e.v[q].second + dy[k] == e.v[i].second)
				}
			}
		}
		
		visited[encode(mask)] = 1;
	}
	*/
}

int encode(vector < pair <int, int> > mask)
{
	int x = 0;
	for(int i=0; i<mask.size(); i++)
		x = x*mask[i].second + mask[i].first;
	return x;
}

bool iguales(nodo a, nodo b)
{
	a.norm();
	b.norm();
	return a.v == b.v;
}

bool vacio(int I, int J, nodo e)
{
	if(I>=0 && I<R && J>=0 && J<C && M[I][J] != '#')
	{
		for(int i=0; i<e.v.size(); i++)
			if(e.v[i].first == I && e.v[i].second == J)
				return 0;
		return 1;
	}
	else return 0;
}

int bfs(nodo nInicial, nodo nFinal)
{
	visited.clear();
	//memset(visited, 0, sizeof(visited));
	visitar(nInicial);
	queue < pair <nodo, int> > Q;
	Q.push(make_pair(nInicial, 0));
	while(!Q.empty())
	{
		nodo q = Q.front().first;
		int d = Q.front().second;
		Q.pop();
		if(iguales(q, nFinal)) return d;
		else
		{
			for(int i=0; i<q.v.size(); i++)
			{
				for(int k=0; k<4; k++)
				{
					int I = q.v[i].first, J = q.v[i].second;
					if(vacio(I-dx[k], J-dy[k], q) && vacio(I+dx[k], J+dy[k], q))
					{
						nodo tmp = q;
						tmp.v[i].first = I + dx[k];
						tmp.v[i].second = J + dy[k];
						
						if(!visitado(tmp))
						{
							if(safe(tmp))
							{
								tmp.ok = 1;
								Q.push(make_pair(tmp, d+1));
								visitar(tmp);
							}
							else if(tmp.ok == 1)
							{
								tmp.ok = 0;
								Q.push(make_pair(tmp, d+1));
								visitar(tmp);
							}
						}
					} 
				}
			}	
		}
	}
	return -1;
}

int doit()
{
	int n = 0;
	vector < pair <int, int> > vInicial;
	for(int i=0; i<R; i++)
	{
		for(int j=0; j<C; j++)
		{
			if(M[i][j]=='o' || M[i][j]=='w')
			{
				n++;
				vInicial.push_back(make_pair(i, j));
			}
		}
	}
	nodo nInicial = nodo(n, vInicial, 1);
	
	n = 0;
	vector < pair <int, int> > vFinal;
	for(int i=0; i<R; i++)
	{
		for(int j=0; j<C; j++)
		{
			if(M[i][j]=='x' || M[i][j]=='w')
			{
				n++;
				vFinal.push_back(make_pair(i, j));
			}
		}
	}
	nodo nFinal = nodo(n, vFinal, 1);
	
	return bfs(nInicial, nFinal);
}

int main()
{
	//freopen("inA.txt", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	
	freopen("out.txt", "w", stdout);
	
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		cin>>R>>C;
		M = vector <string> (R);
		for(int i=0; i<R; i++)
			cin>>M[i];
		cout<<"Case #"<<caso<<": "<<doit()<<endl;
	}
	
	return 0;
}
