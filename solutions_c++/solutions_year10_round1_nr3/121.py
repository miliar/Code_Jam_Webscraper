#include<cstdio>
#include<cmath>
#include<algorithm>
#include<iostream>
using namespace std;

const double rate=(sqrt(5)-1)/2;

int test,A1,A2,B1,B2;

inline bool Can(int i,int j)
{
	if (i<j) swap(i,j);
	if ((int)(i*rate)>j) return true;
	return false;
}
int main()
{
	//freopen("i.txt","r",stdin);
	int cnt=1;
	for (scanf("%d",&test);test--;++cnt)
	{
		scanf("%d%d%d%d",&A1,&A2,&B1,&B2);
		printf("Case #%d: ",cnt);
		long long ans=0;
		for (int i=A1;i<=A2;++i)
		{
			int r=B2,l=max(i,int(floor(i/rate+1)));
			if (B1>l) l=B1;
			if (r>=l) ans+=r-l+1;
			l=B1,r=min(i-1,int(ceil(i*rate-1)));
			if (B2<r) r=B2;
			if (r>=l) ans+=r-l+1;
		}
		cout<<ans<<endl;
	}
	return 0;
}
