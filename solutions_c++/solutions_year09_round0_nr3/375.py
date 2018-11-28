#include<stdio.h>
#include<string>
using namespace std;
#define MOD 10000
FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

int dp[505][20];
char tt[505];
string w = "welcome to code jam";

int solve(int ind , int t)
{
    if(t == w.size()) return 1;
    if(dp[ind][t] != -1) return dp[ind][t];
    int ret = 0;
    for(int i=ind;tt[i] != '\0';i++)
        if(tt[i] == w[t]) ret += solve(i,t+1) , ret %= MOD;
    return dp[ind][t] = ret;
}

int main()
{
    int i , a , k , ret[5] , c = 0;
    char x;
    fscanf(in,"%d\n",&k);
    while(k)
    {
        k-- , c++;
        i = 0;
        memset(tt,0,sizeof tt);
        while(1)
        {
            if(fscanf(in,"%c",&x) == EOF) break;
            if(x == '\n') break;
            tt[i++] = x;
        }
        memset(dp,-1,sizeof dp);
        memset(ret,0,sizeof ret);
        i = solve(0,0);
        a = 0;
        while(i) ret[a] = i % 10 , a++ , i /= 10;
        fprintf(out,"Case #%d: ",c);
        for(i=3;i> -1;i--) fprintf(out,"%d",ret[i]);
        fprintf(out,"\n");
    }
    return 0;
}
