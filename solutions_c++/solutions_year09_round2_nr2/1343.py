#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	freopen("G:\\B-small-attempt0.in","r",stdin);
	freopen("G:\\B-small-attempt0.out","w",stdout);
	int t;
	scanf("%d",&t);
	int num[20];
	int num2[20];
	for(int i=1;i<=t;++i)
	{
		int n;
		memset(num,0,sizeof(num));
		scanf("%d",&n);
		int tt=n;
		while(tt>0)
		{
			num[tt%10]++;
			tt/=10;
		}
		for(int j=n+1;;++j)
		{
			memset(num2,0,sizeof(num2));
			int ttt=j;
			while(ttt>0)
			{
				num2[ttt%10]++;
				ttt/=10;
			}
			int k;
			for(k=1;k<10;++k)
				if(num[k]!=num2[k])
					break;
			if(k>=10)
			{
				printf("Case #%d: %d\n",i,j);
				break;
			}
		}


	}




	return 0;
}