#include <iostream>
using namespace std;
int t,a1,a2,b1,b2;
__int64 result;
const int maxs=1000001;
int high[maxs];
int low[maxs];
void init()
{
	high[0]=0;
	high[1]=2;
	int i,j;
	int last=0;
	for (i=2;i<maxs;i++)
	{
		for (j=last;j<i;j++)
		{
			if (high[j]>i) break;
		}
		high[i]=j+i;
		low[i]=j-1;
		last=j;
	}
}

void calc()
{
	for (int i=a1;i<=a2;i++)
	{
		if (b1>=high[i])
		{
			result+=b2-b1+1;
		}
		else if (b2<=low[i])
		{
			result+=b2-b1+1;
		}
		else
		{
			if (b2>=high[i])
				result+=b2-high[i]+1;
			if (b1<=low[i])
				result+=low[i]-b1+1;
		}
	}
}

int main()
{
	freopen("outC.txt","w",stdout);
	init();
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		result=0;
		cin>>a1>>a2>>b1>>b2;
		calc();
		cout<<"Case #"<<i<<": "<<result<<endl;
	}
}