#include <cstdio>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
#define size 505

char name[] = "welcome to code jam";
int dp[size][21];
char str[size];
int len;

void init()
{
	int i, j;
	for(i=0; i<=len; i++)
	for(j=0; j<=19; j++)
	dp[i][j] = 0;
}

int main()
{
  int i, j, T,len,  casenum = 0;
  
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  
  
  scanf("%d", &T);
  for(casenum=1; casenum<=T; casenum++)
  	{
	 scanf(" ");
	 fgets(str, size, stdin);
	 
	  len = strlen(str);
	  len--;
	  init();
	  
	  
	  for(i=0; i<20; i++)
	  dp[i][0] = 1;
	  for(i=1; i<=len; i++)
	  for(j=1; j<=19; j++)
	  {
		if(name[j-1]==str[i-1])
		{
		 dp[i][j] = (dp[i-1][j]+dp[i-1][j-1])%10000;
		}
		else
		dp[i][j] = dp[i-1][j];
	  }	 
	  printf("Case #%d: %04d\n", casenum, dp[len][19]);
	}	
	return 0;
}
