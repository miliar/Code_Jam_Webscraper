#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<complex>
#include<iostream>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>


using namespace std;

__int64 n;

__int64 go[12000];

__int64 a[1200000];
__int64 b[1200000];
int main()
{
	freopen("C:\\GGGG\\B-large.in","r",stdin);
	freopen("C:\\GGGG\\ooo.txt","w",stdout);
	__int64 i,j,k;
	__int64 c,cc,h1,g;
	__int64 l,h,t;
	scanf("%I64d",&h);
	for (cc=1;cc<=h;cc++)
	{
		scanf("%I64d%I64d%I64d%I64d",&l,&t,&n,&c);
		for (i=0;i<c;i++)scanf("%I64d",go+i);
		for (i=0;i<n;i+=c)
		{
			for (j=0;j<c&&i+j<n;j++)
			{
				a[i+j]=go[j];
			}
		}
		for (i=0;i<n;i++)
		{
			a[i]*=2;
			b[i]=a[i];
		}
		for (i=1;i<n;i++)a[i]+=a[i-1];
		for (i=0;i<n;i++)
		{
			if (a[i]>t)break;
		}
		__int64 ans=a[n-1];
		vector<__int64>tt;
		if (i==n)
		{
			ans=a[n-1];
		}
		else 
		{
			tt.push_back(a[i]-t);
			__int64 cnt=1;
			for (;i+1<n;i++)
			{
				//if (cnt==l)break;
				tt.push_back(a[i+1]-a[i]);
				//cnt++;
			}
			sort(tt.begin(),tt.end(),greater<__int64>());
			for (i=0;i<tt.size()&&i<l;i++)
			{
				//pr__int64f("%I64d\n",tt[i]);
				ans-=tt[i]/2;
			}
		}
		printf("Case #%I64d: %I64d\n",cc,ans);
	}
	return 0;
}
			
						
	
