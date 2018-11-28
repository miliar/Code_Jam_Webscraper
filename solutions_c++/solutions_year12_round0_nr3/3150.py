#include<iostream>
#include<cstring>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

int dd[10];

long long cashe[2000010];

void main(){

#ifdef INPUT_VAR
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
#endif
	int T,a,b;
	int k=1;
	for (int i=0;i<10;i++)
	{
		dd[i]=k;
		k*=10;
	}
	scanf("%d",&T);
	for (int I=1;I<=T;I++)
	{
		scanf("%d%d",&a,&b);
		int l=0;
		int t=a;
		while (t)
		{
			t/=10;
			l++;
		}
		long long rez=0;
		for (int i=a;i<b;i++)
		{
			t=i/10+i%10*dd[l-1];
			for (int j=0;j<l;j++)
			{
				if (cashe[t]!=I*10000000+i)
				{
					cashe[t]=I*10000000+i;
					if (i<t&&t<=b)
					{
						rez++;
					}
					t=t/10+t%10*dd[l-1];
				}
			}
		}
		printf("Case #%d: %lld\n",I,rez);
	}
}