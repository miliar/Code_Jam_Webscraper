#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

struct Pair
{
	int a[3];
	int best;
	bool operator < (const Pair &b) const
	{
		return best<b.best;
	}
	void print()
	{
		printf("{%d,%d,%d} ",a[0],a[1],a[2]);
	}
};

vector<Pair> tot1[50],tot2[50];

void init()
{
	int a[3];
	for(a[0]=0;a[0]<=10;a[0]++)
		for(a[1]=0;a[1]<=10;a[1]++)
			for(a[2]=0;a[2]<=10;a[2]++)
			{
				int flag=0;
				for(int i=0;i<3;i++)
					for(int j=0;j<3;j++)
						flag=max(flag,abs(a[i]-a[j]));
				if (flag<=2)
				{
					Pair to;
					to.a[0]=a[0];to.a[1]=a[1];to.a[2]=a[2];
					to.best=max(max(a[0],a[1]),a[2]);
					int sum=a[0]+a[1]+a[2];
					if (flag==2)
						tot1[sum].push_back(to);
					else
						tot2[sum].push_back(to);
				}
			}
	for(int i=0;i<=30;i++)
		sort(tot1[i].begin(),tot1[i].end());
}

int main()
{
	init();
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		int N,S,P;
		scanf("%d%d%d",&N,&S,&P);
		int rS=N-S;
		int sum[31];
		memset(sum,0,sizeof(sum));
		for(int j=0;j<N;j++)
		{
			int num;
			scanf("%d",&num);
			sum[num]++;
		}
		int ans=0;
		for(int j=0;j<=30;j++)
			if (sum[j])
			{
				Pair with;
				with.best=P;
				vector<Pair>::iterator it1=lower_bound(tot1[j].begin(),tot1[j].end(),with);
				vector<Pair>::iterator it2=lower_bound(tot2[j].begin(),tot2[j].end(),with);
				int have1=tot1[j].end()-it1;
				int have2=tot2[j].end()-it2;
				int add1=0,add2=0;
				if (have1>0)
					add1=min(sum[j],S);	
				ans+=add1;
				S-=add1;
				sum[j]-=add1;
				if (have2>0)
					add2=min(sum[j],rS);
				ans+=add2;
				rS-=add2;
				sum[j]-=add2;
			}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
