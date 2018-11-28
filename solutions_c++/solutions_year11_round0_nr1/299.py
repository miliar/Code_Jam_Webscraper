#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int command[101];
int main()
{
    int tt;
    scanf("%d",&tt);
	for (int tc=1;tc<=tt;tc++)
    {
    	int n;
    	scanf("%d",&n);
    	for (int i=1;i<=n;i++)
    	{
    		int tmp;
    		char str[3];
    		scanf("%s %d",str,&tmp);
    		if (str[0]=='B') tmp+=1000;
    		command[i]=tmp;
    	}
    	int time[101];
    	memset(time,0,sizeof(time));
    	for (int i=1;i<=n;i++)
    	{
    		int f=0,j;
    		for (j=i-1;j>=1;j--)
				if ((command[i]-1000)*(command[j]-1000)>0) {f=1;break;}
    		if (f) time[i]=abs(command[i]-command[j])+1+time[j];
    		else time[i]=(command[i]-1)%1000+1;
			if (time[i]<=time[i-1]) time[i]=time[i-1]+1;
    	}
    	printf("Case #%d: %d\n",tc,time[n]);
    }
    return 0;
}
