#include<stdio.h>
#include<string.h>

int ans[30];
int ret;
char line[600];
char pt[] = "welcome to code jam";
//			 0123456789012345678
void add(int i)
{
	if (i) ans[i]+= ans[i-1];
	else ans[i]++;
	ans[i] = ans[i]%10000;
	if (i==18) ret=ans[i];
}

void handle(int id)
{	
	char c= line[id];
	for (int i=0;i<19;i++)
	{
		if (c==pt[i]) add(i);
	}
}
int main()
{
	int T,I;
//	freopen("R:\\in3.txt","r",stdin);
//	freopen("R:\\out3.txt","w",stdout);
	scanf("%d\n",&T);
	for (int I=0;I<T;I++)
	{
		ret = 0;
		memset(ans,0,sizeof(ans));
		gets(line);
		int l = strlen(line);
		for (int i=0;i<l;i++)
		{
			handle(i);
		}
		printf("Case #%d: ",I+1);
		char pts[16];
		sprintf(pts,"%d",ret);
		l = 4-strlen(pts);
		while(l--) putchar('0');
		printf("%d\n",ret);
	}
	return 0;
}
