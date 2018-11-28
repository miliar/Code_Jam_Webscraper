#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<sstream>
#include<map>
#include<queue>
#include<set>
#define vvi vector<vector<int> >
#define co continue
#define pb push_back
#define vi vector<int>
#define vs vector<string>
#define br break
#define re return
#define ALL(v) v.begin(),v.end() 

#define REP(i,n) for(int i=0;i<(int) n;i++)
#define LL long long
#define SZ size()
#define INF 10000000

#define pii pair<int ,int>
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin() ; it!=(c).end() ;it++)
template <class T> inline int BITCNT(T x) { int ret=0; while (x) { ret++; x&=x-1; } return ret; }

using namespace std;
#define MN 10001
int M ,V, G[MN] , C[MN];
int memo[MN][2];
int solve(int node , int V)
{
	
	if(node>=(M-1)/2)
	{
		if(node>=M) return 0;
		return V==C[node]?0:INF;	
	}
	//cout<<node<<endl;
	int & res = memo[node][V];
	if(res==-1)
	{
		//cout<<"ll "<<node<<endl;
		res = INF;
		
		if(V==1)
		{
			if(G[node]==1)
			{
				int ret = solve(node*2+1, 1) ;
				int ret1 = solve(node*2+2 , 1);
				if(ret<INF && ret1<INF)
				{
					res = min(res , ret + ret1);
				}
				
				if(C[node] &&(ret1<INF || ret<INF))
				{
					res = min(res , min(ret , ret1) + 1);
				}
				
			}
			//OR
			else
			{
				int ret = solve(node*2+1, 1) ;
				int ret1 = solve(node*2+2 , 1);
				//cout<<ret<<" " <<ret1<<endl;
				res = min(res , min(ret , ret1));
			}
		}
		else
		{
			if(G[node]==0)
			{
				int ret = solve(node*2+1, 0) ;
				int ret1 = solve(node*2+2 , 0);
				//cout<<ret<<" "<<ret1<<endl;
				if(ret<INF && ret1<INF)
				{
					res = min(res , ret + ret1);
				}
				
				if(C[node] &&(ret1<INF || ret<INF))
				{
					res = min(res , min(ret , ret1) + 1);
				}
				
			}
			//AND
			else
			{
				int ret = solve(node*2+1, 0) ;
				int ret1 = solve(node*2+2 , 0);
				res = min(res , min(ret , ret1));
			}
		}
	}
	return res;
}

int main()
{
    int kases;
    cin>>kases;
    for(int kase = 1 ; kase<=kases; kase++)
    {
		cin>>M>>V;
		int ind;
		REP(i,(M-1)/2)
		{
			ind = i;
			cin>>G[i]>>C[i];
		}
		REP(i,(M+1)/2)
		{
			ind++;
			cin>>C[ind];
		}
		memset(memo , -1 , sizeof(memo));;
		int ret = solve(0 , V);
		
		cout<<"Case #"<<kase<<": ";
		if(ret>=INF) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ret<<endl;
	}
}
