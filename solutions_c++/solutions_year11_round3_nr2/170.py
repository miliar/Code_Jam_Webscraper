#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int row,cul,n;
const int size=1000005,inf=1<<26;
long long L,T,N,C;
long long arr[size];
struct star_struct
{
	long long dis;
	long long arr_time;
	long long can;
	bool used;
};
star_struct star[size];

inline bool rule(const star_struct &a,const star_struct &b)
{
	return a.can>b.can;
}

int main()
{
	int t,e=1;

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	scanf("%d",&t);
	while(t--)
	{
		int i,j;
		long long ans=0;

		scanf("%lld%lld%lld%lld",&L,&T,&N,&C);
		for(i=0;i<C;i++)
			scanf("%lld",&arr[i]);
		star[0].can=star[0].dis=star[0].arr_time=0;
		for(i=1,j=0;i<=N;i++,j=(j+1)%C)
		{
			star[i].dis=arr[j];
			star[i].arr_time=star[i-1].arr_time+arr[j]*2;
			star[i].used=false;
			if(star[i].arr_time>=T)
			{
				if(star[i-1].arr_time>=T)
					star[i].can=star[i].dis;
				else star[i].can=star[i].dis-(T-star[i-1].arr_time)/2;
			}
			else star[i].can=0;
		}

		ans=star[N].arr_time;

		sort(star+1,star+1+N,rule);

		for(i=1;i<=L;i++)
			ans-=star[i].can;

		printf("Case #%d: %lld\n",e++,ans);
	}
	return 0;
}