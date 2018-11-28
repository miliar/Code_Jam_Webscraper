#include<cstdio>
#include<queue>
#include<algorithm>
using namespace std;
#define MAX 1000
int R,K,N;
int g[MAX];
unsigned long long int dp[MAX][2];
void pre_compute()
{
    //solve for all N states
    int i,j,cnt;
    for(i=0;i<N;i++)
    {
        //starting is ith group
        int twt=0,price=0;
        for(j=i,cnt=0;cnt<N;cnt++)
        {
            //find the cost and groups that can be carried
            twt+=g[j];
            if(twt>K)break;
            price+=g[j];
            j=(j+1)%N;
        }
        dp[i][0]=price;
        dp[i][1]=cnt;
    }
    /*for(i=0;i<N;i++)
    printf("%d %d %d\n",i+1,dp[i][0],dp[i][1]);*/
}
int main()
{
    FILE *fin,*fout;
    fin=fopen("C-large-ravi.in","r");
    fout=fopen("C-large-ravi.out","w");
    int T;
    fscanf(fin,"%d",&T);
    int tcase=1;
    while(T--)
    {
        fscanf(fin,"%d %d %d",&R,&K,&N);
        for(int i=0;i<N;i++)
            fscanf(fin,"%d",&g[i]);
        pre_compute();
        unsigned long long money_earnt=0;
        int indx=0;
        while(R--)
        {
            //calculate cost for Ride R
            money_earnt=money_earnt+dp[indx][0];
            indx=(indx+dp[indx][1])%N;
        }
        fprintf(fout,"Case #%d: %llu\n",tcase++,money_earnt);
    }
    return 0;
}
