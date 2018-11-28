#include<stdio.h>
#include<iostream>
#include<string>
#include<cstring>
#include<queue>
#include<vector>
#include<map>
#include<sstream>
#include<math.h>
#include<algorithm>
#define ll long long
#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for(int i=a;i!=b;i++)
#define frr(i,a,b) for(int i=a;i!=b;i--)
#define pf printf
#define sf scanf
#define mp make_pair
#define pb push_back
using namespace std;
int max(int a,int b)
{
	return a>b?a:b;
}
int min(int a,int b)
{
	return a<b?a:b;
}
int a[2510][2510];
int key[100][100];
struct edge
{
    int a,b;
    int next;
    int key;
    edge(){}
    edge(int a,int b,int next):a(a),b(b),next(next){}
}e[1000000];
int tol,p[100000];
void add(int a,int b)
{
    e[tol]=edge(a,b,p[a]);
    p[a]=tol++;
}
int ans;
int dfs(int t)
{
    int ret=1<<29;
    int ok=0;
    for(int i=p[t];i!=-1;i=e[i].next)
    {
        ok=1;
        int t1=dfs(e[i].b);
        ret=min(ret,t1);
    }
    if(ok)
    {
        ret--;
        if(ret<0)ans++;
    }
	else
		ret=e[t].key;
    return ret;
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T;
    int ca=0;
    while(T--)
    {
        int n;
        scanf("%d",&n);
        int id=1;
        tol=0;_clr(p);
		int k=0;
        for(int i=n;i>=0;i--)
        {
            for(int j=0;j<(1<<i);j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
		for(int i=0;i<n+1;i++)
		{
			for(int j=0;j<(1<<i);j++)
			{

				if(i==n)
				{
					e[id].key=a[i][j];
				}
				else
				{
					add(id,id*2);
					add(id,id*2+1);
					e[id].key=0;
				}
				id++;
			}
		}
        ans=0;
		dfs(1);
        pf("Case #%d: %d\n",++ca,ans);
    }
}
