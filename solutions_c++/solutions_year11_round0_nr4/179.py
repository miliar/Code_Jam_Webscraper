#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
#define MAXN 1010

//long double fact[MAXN];
//long double f[MAXN];

int main()
{
//	fact[0]=1;
//	for (int i=1;i<MAXN;i++)
//	{
//		fact[i]=i*fact[i-1];
//		cerr<<fact[i]<<endl;
//	}
//	f[1]=0.0;
//	for (int n=2;n<MAXN;n++)
//	{
//		f[n]=1.0/n;
//		for (int k=1;k<n;k++)
//		{
//			double prob=1.0/n;
//			double next=f[n-k];
//			if (k>1)
//				next+=1+f[k];
//			f[n]+=prob*next;
//		}
//		f[n]*=n;
//		f[n]/=n-1;
//		cerr<<n<<' '<<f[n]<<endl;
//	}

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int caseN;
	scanf("%d",&caseN);
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		int n;
		int a[MAXN];
		scanf("%d",&n);
		for (int i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			a[i]--;
		}
		double ans=0;
		bool flag[MAXN];
		memset(flag,true,sizeof(flag));
		for (int i=0;i<n;i++)
			if (flag[i])
			{
				int l=0;
				for (int k=i;flag[k];k=a[k])
				{
					flag[k]=false;
					l++;
				}
				if (l>1)
					ans+=l;
			}
		printf("Case #%d: %.9lf\n",caseI,ans);
	}
	return 0;
}
