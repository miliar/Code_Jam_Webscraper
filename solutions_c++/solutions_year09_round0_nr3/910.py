#include<stdio.h>
#include<algorithm>
#include<string>
using namespace std;
#define MOD 10000

char pat[23]="welcome to code jam";//len=19;

int len;

int ans[510][22];
char in[510];

int Get(int fir,int sec)
{
    if(ans[fir][sec]>-1)
		return ans[fir][sec];
	ans[fir][sec]=0;
	int i;
	if(sec==0)
	{
	   for(i=0;i<=fir;i++)
	   {
		   if(in[i]==pat[sec])
			   ans[fir][sec]++;
	   }
	   ans[fir][sec]%=MOD;
	   return ans[fir][sec];
	}
    if(fir==sec)
	{
	   if(in[fir]==pat[sec])
		   ans[fir][sec]+=Get(fir-1,sec-1);
	   ans[fir][sec]%=MOD;
	   return ans[fir][sec];
	}
	ans[fir][sec]+=Get(fir-1,sec);
	if(in[fir]==pat[sec])
		ans[fir][sec]+=Get(fir-1,sec-1);
	ans[fir][sec]%=MOD;
	return ans[fir][sec];
}
 
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t;
	int k;
	int i;
	int j;
	scanf("%d",&t);
	getchar();
	for(k=0;k<t;k++)
	{
		
	    gets(in);
		len=strlen(in);
		printf("Case #%d: ",k+1);
		if(len<19)
		{
			printf("%04d\n",0);
			continue;
		}
		for(i=0;i<len;i++)
			for(j=0;j<19;j++)
			{
			    ans[i][j]=-1;
			}
		printf("%04d\n",Get(len-1,18));

	}
    
    return 0;
}