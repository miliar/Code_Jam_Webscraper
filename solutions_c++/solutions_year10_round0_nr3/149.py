#include <iostream>

using namespace std;

int r,k,n;
int num[1010];
int next[1010];
int sum[1010];
__int64 total;

int main()
{
	freopen("result.txt","w",stdout);
	int cs;
	cin>>cs;
	for(int ii=1;ii<=cs;ii++)
	{
		cin>>r>>k>>n;
		for(int i=0;i<n;i++)
			cin>>num[i];
		for(int i=0;i<n;i++)
		{
			next[i]=-1;
			int t=0;
			for(int j=i;j<i+n;j++)
			{
				t+=num[j%n];
				if(t>k)
					break;
				next[i]=(1+j)%n;
				sum[i]=t;
			}
		}
		total=0;
		int cur=0;
		while(r--)
		{
			total+=sum[cur];
			cur=next[cur];
		}
		printf("Case #%d: %I64d\n",ii,total);
	}
}