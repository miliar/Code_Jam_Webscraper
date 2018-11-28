#include<cstdio>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;
int DP[512][24];
int main()
{
    int i,j,T,k,v;
    string A="welcome to code jam";
    scanf("%d\n",&T);
    char W[512];
    for(k=0;k<T;++k)
    {
        gets(W);
        for(i=0;i<strlen(W);++i)
            for(j=0;j<A.length();++j)
            {
                if(i!=0)DP[i][j]=DP[i-1][j];
                else DP[i][j]=0;
                if(W[i]==A[j])
                {
                    if(i!=0&&j!=0)DP[i][j]+=DP[i-1][j-1];
                    if(i==0&&j==0)DP[i][j]+=1;
                    if(i==0&&j!=0)DP[i][j]+=0;
                    if(i!=0&&j==0)DP[i][j]+=1;
                }
                DP[i][j]%=10000;
            }
        printf("Case #%d: ",k+1);
        v=DP[strlen(W)-1][A.length()-1];
        if(v<10)printf("000%d\n",v);
        if(v>=10&&v<100)printf("00%d\n",v);
        if(v>=100&&v<1000)printf("0%d\n",v);
        if(v>=1000&&v<10000)printf("%d\n",v);
    }
    return 0;
}
