#include<stdio.h>
#include<string.h>
char data[200][200],ne[200][200];
bool have(int x,int y)
{
	if(x<0||y<0)
		return false;
	return data[x][y];
}
int dd()
{
	int in,n,m;
	for(n=0;n<200;n++)
		for(m=0;m<200;m++)
			data[n][m]=0;
	scanf("%d",&in);
	for(n=0;n<in;n++)
	{
		int a,b,c,d,m,o;
		scanf("%d %d %d %d",&a,&b,&c,&d);
		for(m=a;m<=c;m++)
		{
			for(o=b;o<=d;o++)
				data[m][o]=1;

		}
	}
	/*for(n=0;n<200;n++)
	{
		for(m=0;m<200;m++)
			printf("%d",data[n][m]);
		printf("\n");
	}*/
	int cnt=0;
	while(1)
	{
		bool fin=true;
		//printf("End Sec %d\n",cnt);
		for(n=0;n<200;n++)
		{
			for(m=0;m<200;m++)
			{
				bool a=have(n-1,m),b=have(n,m-1);
				if(a&&b)
				{
					ne[n][m]=1;
				}else if((!a)&&(!b))
				{
					ne[n][m]=0;
				}else {
					ne[n][m]=data[n][m];
				}
				if(ne[n][m])
					fin=false;
				//printf("%d",ne[n][m]);
			}
		//printf("\n");
		}
		memcpy(data,ne,sizeof(data));
		cnt++;
		if(fin)
			break;
	}
	return cnt;
}
int main()
{
	int in,n;
	scanf("%d",&in);
	for(n=0;n<in;n++)
	{
		printf("Case #%d: %d\n",n+1,dd());
	}
}
