#include<iostream>
using namespace std;
#include<string.h>
const int MAXN = 600;
const int mol = 10000;
char dic[] = "welcome to code jam";
const int len = strlen(dic);
bool visited[MAXN][MAXN];
int dps[MAXN][MAXN];
int n;
char str[MAXN];
int dp(int depth,int pos)
{
    if(pos == len) return 1;
    if(depth == n) return 0;
    if(visited[depth][pos]) return dps[depth][pos];
    visited[depth][pos] = true;
    
    dps[depth][pos] = dp(depth + 1,pos) % mol;
    if(str[depth] == dic[pos]) 
    dps[depth][pos] = (dps[depth][pos] + dp(depth + 1,pos + 1)) % mol;
   
   return dps[depth][pos];
}
char s[1000]; 
int main()
{
    int i,J,k;
    int res;
    int ncase,casenum = 1;
    freopen("c.txt","w",stdout);
    scanf("%d",&ncase);
    while(ncase--)
    {
          scanf("\n");
          gets(str);
          n = strlen(str);
          memset(visited,false,sizeof(visited));
          res = dp(0,0) % mol;
          if(res >= 1000)
          printf("Case #%d: %d\n",casenum++,res);
          else if(res >= 100)
          printf("Case #%d: %d%d\n",casenum++,0,res);
          else if(res >= 10)
          printf("Case #%d: %d%d%d\n",casenum++,0,0,res);
          else
          printf("Case #%d: %d%d%d%d\n",casenum++,0,0,0,res); 
    } 
  //  system("pause");       
    return 0;
}
