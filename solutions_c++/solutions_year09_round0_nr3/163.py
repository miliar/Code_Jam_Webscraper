

#include <iostream>

using namespace std;

char buf[32];
char str[1024];

int ff[32][1024];

int fun(int i,int j)
{
	if(str[j]==0) return buf[i]==0;
	if(ff[i][j]!=-1) return ff[i][j];
	int ret=0;
	if(buf[i]&&buf[i]==str[j]) ret+=fun(i+1,j+1);
	ret+=fun(i,j+1);
	if(ret>=10000) ret-=10000;
	return ff[i][j]=ret;
}
int main()
{
	int t;
	strcpy(buf,"welcome to code jam");
	scanf("%d",&t);
	int i;
	gets(str);
	for(i=1;i<=t;i++)
	{
		gets(str);
		memset(ff,0xff,sizeof(ff));
		int ret=fun(0,0);
		printf("Case #%d: %04d\n",i,ret);
	}
	
	return 0;
}
