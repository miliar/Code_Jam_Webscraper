#if 1
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
//	freopen("A0.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int u=0;u<T;u++)
	{
		int a,b;
		scanf("%d%d",&a,&b);
		printf("Case #%d: ",u+1);
		int sum=0;
		for(int i=a;i<b;i++)
		{
			if(i<10)
				continue;
			for(int j=i+1;j<=b;j++)
			{
				if(i<100)
				{
					if(j/10+(j%10)*10==i)
						sum++;
				}
				else
				{
					if(j/100+(j%100)*10==i||j/10+(j%10)*100==i)
						sum++;
				}
			}
		}
		printf("%d\n",sum);
	}
}



#endif