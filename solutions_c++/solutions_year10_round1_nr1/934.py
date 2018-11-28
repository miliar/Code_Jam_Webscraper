#include<cstdio>
#include<algorithm>
using namespace std;
#define MAX 51
char A[MAX][MAX];
char B[MAX][MAX];
int N,K;
int dp[MAX][MAX][4];
bool Red,Blue;
inline void solve()
{
    register int i,j;
    for(i=0;i<N;i++)
    {
        for(j=0;j<N;j++)
        {
            //check if dot then clear the whole count till now
            if(B[i][j]=='.')
            dp[i][j][0]=dp[i][j][1]=dp[i][j][2]=dp[i][j][3]=0;
            else
            {
                if(B[i][j]=='R')
                {
                    //we have cross here
                    //see if it extends the row
                    if(j>0 && dp[i][j-1][0]>0)
                    dp[i][j][0]=dp[i][j-1][0]+1;
                    else
                    dp[i][j][0]=1;
                    //see for the column
                    if(i>0 && dp[i-1][j][1]>0)
                    dp[i][j][1]=dp[i-1][j][1]+1;
                    else
                    dp[i][j][1]=1;
                    //see for left diagonal
                    if(j>0 && dp[i-1][j-1][2]>0)
                    dp[i][j][2]=dp[i-1][j-1][2]+1;
                    else
                    dp[i][j][2]=1;
                    //see for right
                    if(j<N-1 && dp[i-1][j+1][3]>0)
                    dp[i][j][3]=dp[i-1][j+1][3]+1;
                    else
                    dp[i][j][3]=1;

                }
                else
                {
                    //we have O here
                    //see if it extends the row
                    if(j>0 && dp[i][j-1][0]<0)
                    dp[i][j][0]=dp[i][j-1][0]-1;
                    else
                    dp[i][j][0]=-1;
                    //see for the column
                    if(i>0 && dp[i-1][j][1]<0)
                    dp[i][j][1]=dp[i-1][j][1]-1;
                    else
                    dp[i][j][1]=-1;
                    //see for diagonal
                    if(j>0 && dp[i-1][j-1][2]<0)
                    dp[i][j][2]=dp[i-1][j-1][2]-1;
                    else
                    dp[i][j][2]=-1;
                    if(j<N-1 && dp[i-1][j+1][3]<0)
                    dp[i][j][3]=dp[i-1][j+1][3]-1;
                    else
                    dp[i][j][3]=-1;
                }
            }
            if(dp[i][j][0]==K || dp[i][j][1]==K || dp[i][j][2]==K || dp[i][j][3]==K)
                Red=true;
            else if(dp[i][j][0]==-K || dp[i][j][1]==-K || dp[i][j][2]==-K ||dp[i][j][3]==-K)
                Blue=true;
        }
    }
}
int main()
{
    FILE *in;
    in=fopen("in.txt","r");
    FILE *out;
    out=fopen("out.txt","w");
    int T;
    fscanf(in,"%d",&T);
    int cases;
    for(cases=1;cases<=T;cases++)
    {
        Red=false,Blue=false;
        printf("%d %d\n",cases,T);
        fscanf(in,"%d %d",&N,&K);
        register int i,j;
        for(i=0;i<N;i++)
        fscanf(in,"%s",A[i]);
        //prepare the rotated first
        for(i=N-1;i>=0;i--)
        {
            //ith row in B ith col in A
            for(j=0;j<N;j++)
                B[j][N-1-i]=A[i][j];
            B[i][N]='\0';
        }
        /*for(i=0;i<N;i++)
        {
            printf("%s\n",B[i]);
        }*/
        //check for fall down
        for(j=0;j<N;j++)
        {
            i=N-1;
            int cnt=N-1;
            while(i>=0)
            {
                if(B[i][j]!='.')
                {
                    B[cnt][j]=B[i][j];
                    if(cnt!=i)
                    B[i][j]='.';
                    cnt--;
                }
                i--;
            }
            while(cnt>=0)
            {
                B[cnt][j]='.';
                cnt--;
            }
        }
        /*printf("***F***\n");
        for(i=0;i<N;i++)
        {
            printf("%s\n",B[i]);
        }*/
        //now check for K row
        solve();
        fprintf(out,"Case #%d: ",cases);
        //print ans
        if(Red && Blue )fprintf(out,"Both\n");
        else if( Red && !Blue)fprintf(out,"Red\n");
        else if(!Red && Blue)fprintf(out,"Blue\n");
        else fprintf(out,"Neither\n");

    }
    return 0;
}
