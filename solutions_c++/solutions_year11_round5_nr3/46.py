#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <algorithm>
#include <stack>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.0000000001
#define inf 1<<28
#define mod 1000003

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <VVI> VVVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef queue <int> QI;
typedef pair<int,int> PI;
typedef pair<int,PI> PT;
typedef queue<PI> QPI;
typedef priority_queue<PT> QPT;
typedef pair<double,double> PD;
typedef map<int,int> MII;
typedef vector<string> VS;
typedef stack<int> SI;

VI ant;
VB vis;

VVI G;
VI cb;
VVI inv;

SI s;

VI lcc;
int ncc;

bool dfs (int a)
{
	if (vis[a]) return false;
	vis[a]=true;
	fi (2)
	{
		int b = G[a][i];
		if (ant[b] == -1)
		{
			ant[b] = a;
			return true;
		}
		if (dfs (ant[b]))
		{
			ant[b] = a;
			return true;
		}
	}
	return false;
}

int otro (int a, int b)
{
	if (G[a][0] == b)
		return G[a][1];
	return G[a][0];
}

void dfs2(int a)
{
	if (vis[a]) return;
	vis[a]=true;
	dfs2(cb[a]);
	s.push(a);
}

void dfs3 (int a)
{
	if (lcc[a] != -1) return;
	lcc [a] = ncc;
	fi (inv[a].size())
		dfs3(inv[a][i]);
}

int main()
{
	int T;
	cin >> T;
	for (int caso=1;caso<=T;caso++)
	{
		cout << "Case #" << caso << ": ";
		int R, C;
		cin >> R >> C;
		VS v(R);
		fi (R) cin >> v[i];
		int n = R*C;
		G = VVI (n, VI (2));
		fi (R)
		{
			fj (C)
			{
				//buscamos vecinos
				int a = i*C+j;
				if (v[i][j] == '-')
				{
					G[a][0] = i*C+(j+C-1)%C;
					G[a][1] = i*C+(j+1)%C;
				}
				else if (v[i][j] == '|')
				{
					G[a][0] = ((i+R-1)%R)*C+j;
					G[a][1] = ((i+1)%R)*C+j;				
				}
				else if (v[i][j] == '/')
				{
					G[a][0] = ((i+R-1)%R)*C+(j+1)%C;
					G[a][1] = ((i+1)%R)*C+(j+C-1)%C;					
				}
				else
				{
					G[a][0] = ((i+R-1)%R)*C+(j+C-1)%C;
					G[a][1] = ((i+1)%R)*C+(j+1)%C;
				}
			}
		}
		//fi (n) cout << i << ": " << G[i][0] << " " << G[i][1] << endl;
		ant = VI (n, -1);
		bool ok = true;
		fi (n)
		{
			vis = VB (n,false);
			if (not dfs(i))
				ok=false;
			if (not ok)
				break;
		}
		if (not ok)
		{
			cout << 0 << endl;
			continue;
		}
		//fi (n) cout << i << "<-" << ant[i] << endl;
		VI va (n);
		fi (n) va[ant[i]] = i;
		
		cb = VI (n);
		fi (n) cb[i] = ant[otro(i,va[i])];
		
		//fi (n) cout << i << "->" << cb[i] << endl;
		
		inv = VVI (n);
		fi (n) inv[cb[i]].push_back(i);
		
		s = SI();	
		
		vis = VB (n, false);
		
		fi (n)
		{
			dfs2(i);
		}
		ncc = 0;
		lcc = VI (n,-1);
		while (not s.empty())
		{
			dfs3(s.top());
			s.pop();
			ncc++;
		}
		//fi (n)	cout << i << ": " << lcc[i] << endl;
		MII m;
		fi (n)
			m[lcc[i]]++;
		
		int num = 0;
		for (MII::iterator it = m.begin();it!=m.end();it++)
		{
			if (it->second > 1)
				num++;
		}
		ll resp = 1;
		fi (num)
		{
			resp*=2;
			resp%=mod;
		}
		cout << resp << endl;
	}
}
