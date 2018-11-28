#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<sstream>
#include<assert.h>
#include<cmath>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<stack>
using namespace std;
typedef long long ll;
const int inf=1000000000;
const double pi=acos(-1.0);
#define eps (1e-15)
#define L(x) ((x)<<1)
#define R(x) ((x)<<1|1)
#ifdef DBG
#define see(x) (cerr<<"[Line : "<< __LINE__<<"] : "<<#x<<"="<<x<<endl)
#define se(x) cerr<<x<<" "
#else
#define see(x) //
#define se(x) //
#endif

#define maxn  5030
int n,m;
struct node
{
	int id,a;
	node(){}
	node(int aa,int bb){a=aa; id=bb;}
}a[maxn],b[maxn],c[maxn];
int aid=0,bid,cid;
char ch[110],s[110];

int solve()
{
	int i,j;
	int nowb=1,nowc=1;
	int bi=0,ci=0;
	int ans=0,t,tp;
	for(i=0; i<n; i++)
	{
		if(a[i].id==0)
		{
			t=fabs(b[bi].a-nowb)+1;
			nowb=b[bi].a;
			ans+=t;
			bi++;
			tp=fabs(c[ci].a-nowc);
			if(t>=tp)
				nowc=c[ci].a;
			else
			{
				if(c[ci].a>nowc)
					nowc+=t;
				else	if(c[ci].a<nowc)
					nowc-=t;
			}
		}
		else
		{
			t=fabs(c[ci].a-nowc)+1;
			nowc=c[ci].a;
			ans+=t;
			ci++;
			tp=fabs(b[bi].a-nowb);
			if(t>=tp)
				nowb=b[bi].a;
			else
			{
				if(b[bi].a>nowb)
					nowb+=t;
				else if(b[bi].a<nowb)
					nowb-=t;
			}
		}
	}
	return ans;
}
int main()
{
 	// freopen("in","r",stdin);
	 //freopen("out","w",stdout);
	int i,j,t,k;
	scanf("%d",&t);
	int cas=0;
	while(t--)
	{
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		memset(c,0,sizeof(c));
		aid=0;bid=0; cid=0;
		int x,y;
		scanf("%d", &n);
		for(i=0;i <n ;i++)
		{
			scanf("%s %d", ch,&x);
			if(ch[0]=='B')
			{
				y=0;
				b[bid++]=node(x,y);
			}
			else
			{
				y=1;
				c[cid++]=node(x,y);
			}
			a[aid++]=node(x,y);
		}
		int ans=solve();
		printf("Case #%d: %d\n",++cas,ans);
	}
}
