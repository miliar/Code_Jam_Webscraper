#include<iostream>
#define Max 501
using namespace std;

char str[Max]="welcome to code jam", input[Max];
int sl, hash[128];
int dp[Max][Max];

int main()
{
	int z, zi, i, j, l, ans, t;
	
	sl=strlen(str);
	for(i=0;i<sl;i++)
	    hash[ str[i] ] =1;
	
	scanf("%d", &z);
	getchar();
	for(zi=1;zi<=z;zi++)
	{
		gets(input);
		
		l=strlen(input);
		for(i=0;input[i] && input[i]!=str[0];i++);
		for(j=0;input[i];i++)
		    if(hash[ input[i] ])
				input[j++]=input[i];
		input[j]=0;
		l=j;
		
		memset(dp, 0, sizeof(dp));
		for(i=0;i<l;i++)
		    if(input[i]==str[0])
		    	dp[0][i]=1;
	    
		for(i=1;i<sl;i++)
		{
            t=ans=0;
            for(j=i;j<l;j++)
            {
                if(dp[i-1][j-1])
                    t=(t+dp[i-1][j-1])%10000;
                if(input[j]==str[i])
                {
                    dp[i][j]=t;
                    ans=(ans+t)%10000;
                }
            }
		}
		printf("Case #%d: %04d\n", zi, ans);
	}
	return 0;
}
