#include<iostream>
using namespace std;
#define INF 1<<20
#define N 1008
#define M 108

char s[M][M],st[M];

void getch(char *s)
{
    char c;
    int k = 0;
    while((c=getchar())!='\n')
    {
        s[k++] = c;
    }
    s[k] = '\0';
} 
    

int main()
{
	freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\A-large.in","r",stdin);
	freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\A.out","w",stdout);
	int i,j,k,r,t,S,Q,a[N];
	int dp[N][M];
	scanf("%d",&t); 
	for(i=0; i<t; i++)
    {
        scanf("%d",&S);
        getchar();
        for(j=1; j<=S; j++)
        {
            getch(s[j]);
        }
        scanf("%d",&Q);
        getchar();
        for(j=1; j<=Q; j++)
        {
            getch(st);
            for(k=1; k<=S; k++)
                if(strcmp(st,s[k])==0) break;
            a[j] = k;
        }
        //for(j=1; j<=Q; j++) cout<<a[j]<<" "; cout<<endl;
        
        for(j=0; j<=S; j++) dp[0][j] = 0;
        for(j=1; j<=Q; j++)
        {
            for(k=1; k<=S; k++)
            {
                if(a[j]==k){ dp[j][k] = INF; continue;}
                dp[j][k] = j;
                for(r=1; r<=S; r++)
                {
                    if(r==k) dp[j][k] = min(dp[j][k],dp[j-1][r]);
                    else dp[j][k] = min(dp[j][k],dp[j-1][r]+1);
                }
            }
           // for(k=1; k<=S; k++) cout<<dp[j][k]<<" "; cout<<endl;
        }
        int res = INF;
        for(j=1; j<=S; j++) res<?=dp[Q][j];
		printf("Case #%d: %d\n",i+1,res);
	}
	return 0;
}

