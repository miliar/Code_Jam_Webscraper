#include <iostream>
using namespace std;
int N,M,V;
int s[20000][2];
int G[20000],C[20000];
void print()
{
    int i,j;
        for (j=0;j<2;j++)
        {
            for (i=0;i<M;i++)
                cout<<s[i][j]<<' ';
            cout<<endl;
        }

}
void DP(int x)
{
    int i,j;
    if (s[x*2+1][0]==-1 && s[x*2+1][1]==-1)
        DP(x*2+1);
    if (s[x*2+2][0]==-1 && s[x*2+2][1]==-1)
        DP(x*2+2);
    for (i=0;i<2;i++) if (s[x*2+1][i]!=-1)
        for (j=0;j<2;j++) if (s[x*2+2][j]!=-1)
            if (G[x]==1)
            {
                if (s[x][i & j]==-1 || s[x*2+1][i]+s[x*2+2][j]<s[x][i & j])
                    s[x][i & j]=s[x*2+1][i]+s[x*2+2][j];
            }
            else
            {
                if (s[x][i | j]==-1 || s[x*2+1][i]+s[x*2+2][j]<s[x][i | j])
                    s[x][i | j]=s[x*2+1][i]+s[x*2+2][j];
            }
    if (C[x]==1)
    {
        for (i=0;i<2;i++) if (s[x*2+1][i]!=-1)
            for (j=0;j<2;j++) if (s[x*2+2][j]!=-1)
                if (G[x]==0)
                {
                    if (s[x][i & j]==-1 || s[x*2+1][i]+s[x*2+2][j]+1<s[x][i & j])
                        s[x][i & j]=s[x*2+1][i]+s[x*2+2][j]+1;
                }
                else
                {
                    if (s[x][i | j]==-1 || s[x*2+1][i]+s[x*2+2][j]+1<s[x][i | j])
                        s[x][i | j]=s[x*2+1][i]+s[x*2+2][j]+1;
                }
    }
    //cout<<x<<": "<<endl;
    //print();
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k,Ni;
    cin>>N;
    for (Ni=1;Ni<=N;Ni++)
    {
        cin>>M>>V;
        memset(s,-1,sizeof(s));
        for (i=0;i<(M-1)/2;i++)
            cin>>G[i]>>C[i];
        for (i=(M-1)/2;i<M;i++)
        {
            cin>>k;
            s[i][k]=0;
        }
        DP(0);
        //print();
        cout<<"Case #"<<Ni<<": ";
        if (s[0][V]==-1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<s[0][V]<<endl;
    }
    //system("pause");
    return 0;
}
