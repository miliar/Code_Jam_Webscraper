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

struct nodo
{
	bool G, C;
	bool I;
	nodo(bool b1, bool b2)
	{
		G = b1;
		C = b2;
	}
	nodo(bool b1)
	{
		I = b1;
	}
	nodo()
	{
	}
};

int M;

nodo V[10000];

bool eval(int a)
{
	if(a >= (M-1)/2) return V[a].I;
	else
	{
		bool b1 = eval(2*a+1), b2 = eval(2*a+2);
		if(V[a].G) return b1&&b2;
		else return b1||b2;
	}
}

int memo[10000][2];

int f(int a, bool v)
{
	bool B = eval(a);
	if(B==v) return 0;
	else if(a >= (M-1)/2) return 1<<15;
	else
	{
		if(memo[a][v]!=-1) return memo[a][v];
		
			int N1 = 1<<15; // AND
			
			if(v)
			{
				N1 = min(N1, f(2*a+1, 1) + f(2*a+2, 1));
			}
			else
			{
				N1 = min(N1, f(2*a+1, 0) + f(2*a+2, 0));
				N1 = min(N1, f(2*a+1, 0) + f(2*a+2, 1));
				N1 = min(N1, f(2*a+1, 1) + f(2*a+2, 0));
			}
			
			int N2 = 1<<15; // OR
			
			if(v)
			{
				N2 = min(N2, f(2*a+1, 1) + f(2*a+2, 1));
				N2 = min(N2, f(2*a+1, 0) + f(2*a+2, 1));
				N2 = min(N2, f(2*a+1, 1) + f(2*a+2, 0));					
			}
			else N2 = min(N2, f(2*a+1, 0) + f(2*a+2, 0));
			
			int x;
			
			if(V[a].C)
			{
				if(V[a].G) x = min(N1, 1 + N2);
				else x = min(1 + N1, N2);
			}
			else
			{
				if(V[a].G) x = N1;
				else x = N2;			
			}
			
			memo[a][v] = x;
			return x;
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int N;
	cin>>N;
	
	for(int i=0; i<N; i++)
	{
		bool v;
		cin>>M>>v;
		
		for(int j=0; j<(M-1)/2; j++)
		{
			bool b1, b2;
			cin>>b1>>b2;
			V[j] = nodo(b1, b2);
		}
		for(int j=(M-1)/2; j<M; j++)
		{
			bool b1;
			cin>>b1;
			V[j] = nodo(b1);
		}
		
		memset(memo, -1, sizeof(memo));
		
		int x = f(0, v);
		cout<<"Case #"<<i+1<<": ";
		if(x>=(1<<15)) cout<<"IMPOSSIBLE"<<endl;
		else cout<<x<<endl;
		
	}
	return 0;
}
