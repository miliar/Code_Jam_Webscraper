#include <iostream>
#include <stdio.h>
#include <Cstring>
using namespace std;
main()
{
	int i,n,t,m,a,b,ta[1001][2],tb[1001][2],time[2000][4],sa,sb,left,right;
	char s[101];
	cin >>n;
	for(m=0;m<n;m++)
	{
		cin >>t;
		cin >>a>>b;
		gets(s);
		memset(time,0,sizeof(time));
		for(i=1;i<=a;i++)
		{
			gets(s);
			ta[i][1]=(s[0]-48)*600+(s[1]-48)*60+(s[3]-48)*10+(s[4]-48);
			ta[i][2]=(s[6]-48)*600+(s[7]-48)*60+(s[9]-48)*10+(s[10]-48)+t;
			time[ta[i][1]][1]++;
			time[ta[i][2]][2]++;
		}
		for(i=1;i<=b;i++)
		{
			gets(s);
			tb[i][1]=(s[0]-48)*600+(s[1]-48)*60+(s[3]-48)*10+(s[4]-48);
			tb[i][2]=(s[6]-48)*600+(s[7]-48)*60+(s[9]-48)*10+(s[10]-48)+t;
			time[tb[i][1]][3]++;
			time[tb[i][2]][4]++;
		}
		sa=0;sb=0;left=0;right=0;
		for(i=0;i<1500;i++)
		{
			right=right+time[i][2];
			left=left+time[i][4];
			while(time[i][1])
			{
				if(left==0)sa++;
				else left--;
				time[i][1]--;
			}
			while(time[i][3])
			{
				if(right==0)sb++;
				else right--;
				time[i][3]--;
			}
		}
		printf("Case #%i: %i %i\n",m+1,sa,sb);
	}
}

		