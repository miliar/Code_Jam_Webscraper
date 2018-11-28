#include<iostream>
#include<string>
#define MAX 1000005

using namespace std;

int t,a1,a2,b1,b2;
__int64 ans;

int high[MAX];
int low[MAX];

void calc()
{
	for (int i=a1;i<=a2;i++)
	{
		if (b1>=high[i])
		{
			ans+=b2-b1+1;
		}
		else if (b2<=low[i])
		{
			ans +=b2-b1+1;
		}
		else
		{
			if (b2>=high[i])
				ans+=b2-high[i]+1;
			if (b1<=low[i])
				ans+=low[i]-b1+1;
		}
	}
}

int main()
{
	freopen("out.out","w",stdout);
	int i,j;

	int cs;
	cin>>cs;
	for (int cscnt=1;cscnt<=cs;cscnt++)
	{


		cin>>a1>>a2>>b1>>b2;

		high[0]=0;
		high[1]=2;
		int last=0;
		for (i=2;i<MAX;i++)
		{
			for (j=last;j<i;j++)
			{
				if (high[j]>i) break;
			}
			high[i]=j+i;
			low[i]=j-1;
			last=j;
		}
		ans=0;
		calc();
		printf("Case #%d: %I64d\n",cscnt,ans);
	}
}