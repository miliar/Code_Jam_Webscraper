#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<queue>
#include<map>
#include<set>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
#define Pi acos(-1.0)
#define Eps (1e-9)
#define pb push_back
#define mp make_pair
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define sqr(a) ((a)*(a))
#define ALL(a) (a).begin(),(a).end()
#define SORT(a) sort(ALL(a))
int G[20000];
int C[20000];
int M;
int f(int v,int index)
{
	int x=2*index;
	if(x>(M-1)/2)
	{
		if(G[index]==1)
		{
			int r=G[x]*G[x+1];
			if(r==v)return 0;
			if(!C[index])return -1;
			r=G[x]+G[x+1];
			if(r==2)r=1;
			if(r==v)return 1;
			return -1;
		}
		else
		{
			int r=G[x]+G[x+1];
			if(r==2)r=1;
			if(r==v)return 0;
			if(!C[index])return -1;
			r=G[x]*G[x+1];
			if(r==v)return 1;
			return -1;
		}
	}
	int rl[2];
	rl[0]=f(0,x);
	rl[1]=f(1,x);
	int rr[2];
	if(x+1>(M-1)/2)
	{
		rr[0]=-1;
		rr[1]=-1;
		rr[G[x+1]]=0;
	}
	else
	{
		rr[0]=f(0,x+1);
		rr[1]=f(1,x+1);
	}
	int res=-1;
	int i,j;
	int pot=1000000;
	for(i=0;i<2;i++)
		for(j=0;j<2;j++)
		{
			if(rl[i]==-1 || rr[j]==-1)continue;
			if(G[index]==1)
			{
			int r=i*j;
			if(r==v)pot=MIN(pot, rl[i]+rr[j]);
			if(!C[index])continue;
			r=i+j;
			if(r==2)r=1;
			if(r==v)pot=MIN(pot, rl[i]+rr[j]+1);
			}
			else
			{
			int r=i+j;
			if(r==2)r=1;
			if(r==v)pot=MIN(pot, rl[i]+rr[j]);
			if(!C[index])continue;
			r=i*j;
			if(r==v)pot=MIN(pot, rl[i]+rr[j]+1);
			}
		}
		if(pot<1000000)res=pot;
		return res;
}
int main()
{
	freopen("F.in","r",stdin);
	freopen("F.out","w",stdout);
	int T,ind=0;
	cin>>T;

	while(T)
	{
		T--;
		ind++;
		int V;
		cin>>M>>V;
		int i,j;
		for(i=1;i<=M;i++)
		{
			int g,c;
			if(i<=(M-1)/2)
			{
				scanf("%d %d",&g,&c);
				G[i]=g;
				C[i]=c;
			}
			else
			{
				scanf("%d",&g);
				G[i]=g;
			}
		}
		int r=f(V,1);
		if(r==-1)
		{
			cout<<"Case #"<<ind<<": IMPOSSIBLE"<<endl;
		}
		else cout<<"Case #"<<ind<<": "<<r<<endl;
	}
	return 0;
}

