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

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define eps 1e-8
#define pi acos(-1)

using namespace std;

int memo[1000];

map <string, int> M;
bool adj[1000][1000];
int N;

bool mix(string s)
{
	return s[0] >= 'A' && s[0] <= 'Z';
}

int f(int p)
{
	if(memo[p]!=-1) return memo[p];
	
	int nhijos = 0;
	for(int i=0; i<N; i++)
		if(adj[p][i])
			nhijos++;
	if(nhijos==0) return 1;
	
	vector <int> v;
	for(int i=0; i<N; i++)
		if(adj[p][i])
			v.push_back(f(i));
	
	sort(rall(v));
	
	int x = 1<<30;
	
//	do
//	{
		int ans = 0, disp = 0;	
		for(int i=0; i<v.size(); i++)
		{
			if(disp < v[i])
			{
		 		int need = v[i] - disp;
				ans += need;
				disp += need - 1;
			}
			else
			{
				disp--;
			}
		}
		if(disp) x = min(x, ans);
		else x = min(x, ans+1);
//	}while(next_permutation(all(v)));
	
	memo[p] = x;
	return x;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		cout<<"Case #"<<caso<<": ";
		
		M.clear();
		memset(adj, 0, sizeof(adj));
		int tmp = 0;
		memset(memo, -1, sizeof(memo));
		cin>>N;
		
		for(int i=0; i<N; i++)
		{
			string s;
			cin>>s;
			
			if(M.find(s)==M.end())
			{
				M[s] = tmp;
				tmp++;
			}
			
			int n;
			cin>>n;
			
			for(int j=0; j<n; j++)
			{
				string aux;
				cin>>aux;
				
				if(mix(aux))
				{
					if(M.find(aux)==M.end())
					{
						M[aux] = tmp;
						tmp++;
					}
					adj[M[s]][M[aux]] = 1;
				}
			}
			
		}
		
		int p = 0;
		
		for(int i=0; i<N; i++)
		{
			int num = 0;
			for(int j=0; j<N; j++)
			{
				if(adj[j][i]) num++;
			}
			if(num==0) p = i;
		}
		
		cout<<f(p)<<endl;
	}
	
	return 0;
}
