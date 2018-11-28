#include <algorithm>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

bool map[1005][1005];

int judge(int a,int b)
{
	int r=b,t=b,k=1,i=1;
	while(r/10)
	{
		r/=10;
		k*=10;
		++i;
	}
	for(int j=0;j<i;j++)
	{
		t=t/10+(t%10)*k;
		if(t==a && map[a][b]==0 &&map[t][b]==0)
		{
			map[a][t]=1;
			map[t][a]=1;
			return 1;
		}
	}
	return 0;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int T,a,b,sum;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>a>>b;
		memset(map,0,sizeof(map));
		sum=0;
		for(int i=a;i<=b;++i)
			for(int j=i+1;j<=b;++j)
			{
				sum+=judge(i,j);
			}
		cout<<"Case #"<<t<<": "<<sum<<endl;
	}
	return 0;
}
