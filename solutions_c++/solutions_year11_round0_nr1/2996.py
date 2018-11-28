#include<stdio.h>
#include<algorithm>
using namespace std;
pair< int, int> cmd[100000];
int togo[100000][2];
int process()
{
	int in,n;
	char str[5];
	scanf("%d",&in);
	for(n=0;n<in;n++)
	{
		scanf("%s %d",str,&(cmd[n].second));
		if(str[0]=='O')
			cmd[n].first=0;
		else
			cmd[n].first=1;
	}
	togo[in][0]=togo[in][1]=-1;
	for(n=in-1;n>=0;n--)
	{
		togo[n][0]=togo[n+1][0];
		togo[n][1]=togo[n+1][1];
		togo[n][cmd[n].first]=cmd[n].second;
	}
	int time=0;
	int at[2];
	at[0]=at[1]=1;
	for(n=0;n<in;n++)
	{
		int usetime=abs(at[cmd[n].first]-cmd[n].second)+1;
		int x=0;

		if(cmd[n].first==0)
			x=1;
		at[cmd[n].first]=cmd[n].second;
		if(abs(at[x]-togo[n][x])<=usetime)
			at[x]=togo[n][x];
		else
		{
			if(at[x]>togo[n][x])
				at[x]-=usetime;
			else
				at[x]+=usetime;
		}
		time+=usetime;
		//printf("%d %d %d\n",time,at[0],at[1]);
	}
	return time;
}
int main()
{
	int ix,n;
	scanf("%d",&ix);
	for(n=0;n<ix;n++)
		printf("Case #%d: %d\n",n+1,process());
}
