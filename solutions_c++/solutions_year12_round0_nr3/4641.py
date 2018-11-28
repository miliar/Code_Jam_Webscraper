#if(1)
#include<stdio.h>
#include<string.h>

int main()
{
//	freopen("out.txt","w",stdout);
//	freopen("in.txt","r",stdin);
	int N;
	scanf("%d",&N);
	for(int i=0;i<N;i++)
	{
		int a,b;
		int count=0;
		scanf("%d%d",&a,&b);
		if(a==1000)
			a=999;
		if(b==1000)
			b=999;
		for(int j=a;j<=b;j++)
		{
			int q=j/100,w=(j%100-j%10)/10,e=j%10;
			if(q!=0)
			{
				int jj=e*100+q*10+w;
				int jjj=w*100+e*10+q;
				if(jj>j&&jj<=b)
				{
					count++;
//					printf("%d ",j);
				}
				if(jjj>j&&jjj<=b)
				{
					count++;
//					printf("%d ",j);
				}
			}
			else
				if(w!=0)
				{
					if(e!=0&&(e*10+w)>j&&(e*10+w)<=b)
					{
						count++;
//						printf("%d ",j);
					}
				}
				else
					continue;
		}
		printf("Case #%d: %d\n",i+1,count);
	}
	return 0;
}
#endif