#include <stdio.h>
#include <string.h>

int state[25][510];
int main()
{
	int n,len,i,j,k;
	const char wel[20]="welcome to code jam";
	const int wlen = 19;
	char buf[500];
	char output[5] = "0000";
	freopen("out.txt","w",stdout);
	scanf("%d",&n);
	gets(buf);
	for(int count=1;count<=n;count++)
	{
		gets(buf);
		len = strlen(buf);
		memset(state,0,sizeof(state));
		for(i=0;i<=wlen;i++)
			state[0][i] = 1;
		for(i=1;i<=wlen;i++)
		{
			for(j=i;j<=len;j++)
			{
				if(wel[i-1] == buf[j-1])
					state[i][j] = (state[i-1][j-1]+state[i][j-1])%10000;
				else
					state[i][j] = state[i][j-1];
			}
		}
		int ans = state[wlen][len];
		int tmp;		
		for(i=3;i>=0;i--)
		{
			tmp = ans%10;
			output[i] = tmp +'0';
			ans= (ans - tmp)/10;
		}
		printf("Case #%d: %s\n",count,output);
	}
	return 0;
}