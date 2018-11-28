#include<stdio.h>
#include<memory.h>
char tekst[501];//case
char pattern[20] = "welcome to code jam";
int length;//duzina trenutnog case-a

int solvecase()
{
for(int i = 1; i <= length; i++) printf("%c",tekst[i]);
//getchar(); getchar();
int dp[19];
memset(dp,0,sizeof(dp));
int dp2[19];
for(int i = 1; i <= length; i++)
{
memcpy(dp2,dp,sizeof(dp));
for(int j = 0; j <= 18; j++)
{
if(pattern[j]==tekst[i])
{
if(j==0) dp2[j]++;
else dp2[j]+=dp[j-1];
}
}
memcpy(dp,dp2,sizeof(dp2));
for(int i = 0; i <= 18; i++) dp[i] %= 10000;
}
return dp[18];

}
int main()
{
int n;
FILE *f;
f = fopen("C-small.in","r");
FILE *g = fopen("result.txt","w");
fscanf(f,"%d\n",&n);
char chh;
for(int i = 1; i <= n; i++)
{

fscanf(f,"%c",&chh);

for(length = 1; chh!='\n'; length++)
{  tekst[length] = chh; fscanf(f,"%c",&chh); }
length--;
printf("tag2");
//printf("tag");
int res = solvecase();
//printf("tag1");
//printf("%d\n",res);
fprintf(g,"Case #%d: ",i);
if(res<10) fprintf(g,"000%d\n",res);
else if(res<100) fprintf(g,"00%d\n",res);
else if(res<1000) fprintf(g,"0%d\n",res);
else fprintf(g,"%d\n",res%10000);
}
}
