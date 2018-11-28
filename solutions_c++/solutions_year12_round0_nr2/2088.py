#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<sstream>
#include<queue>
#include<cstdio>

using namespace std;
bool ex[33][11][2];

int N,S,P;
const int MX=111;
const int inf=1111111111;

int T[MX];
int POS[MX][2][2];
int DP[MX][MX];
void init()
{
    int a,b,c,d,sur,sum;

    for(a=0;a<=10;a++)
        for(b=a;b<=10&&b<a+3;b++)
            for(c=b;c<=10&&c<b+3;c++)
                if(c-a<3)
            {
                sur=0;
                if(c-a>1) sur=1;

                sum=a+b+c;

                ex[sum][c][sur]=1;
            }
}
void test()
{
    cin>>N>>S>>P;
    int i,s,p,j,cur;
    for(i=0;i<N;i++) cin>>T[i];

    for(i=0;i<N;i++)
        for(s=0;s<2;s++)
            for(p=0;p<2;p++) POS[i][s][p]=0;

    for(i=0;i<N;i++)
        for(j=0;j<=10;j++)
            for(s=0;s<2;s++)
                if(ex[T[i]][j][s])
                {
                    p=(j>=P);
                    POS[i][s][p]=1;
                }
    for(i=0;i<=N;i++)
        for(j=0;j<=N;j++) DP[i][j]=-inf;

    if(POS[0][0][0]) DP[0][0]=0;
    if(POS[0][0][1]) DP[0][0]=1;
    if(POS[0][1][0]) DP[0][1]=0;
    if(POS[0][1][1]) DP[0][1]=1;

    for(i=1;i<N;i++)
        for(j=0;j<=N;j++)
        {
            for(s=0;s<2;s++)
                for(p=0;p<2;p++)
                    if(POS[i][s][p]&&j-s>=0)
                    {
                        cur=DP[i-1][j-s]+p;
                        if(cur>DP[i][j])
                            DP[i][j]=cur;
                    }
        }
    cout<<DP[N-1][S];

}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int i,I;
    cin>>I;

    init();

    for(i=0;i<I;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        test();
        cout<<endl;
    }
    return 0;
}
