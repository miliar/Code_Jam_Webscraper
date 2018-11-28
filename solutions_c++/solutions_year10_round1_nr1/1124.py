#include <iostream>
#include <cmath>
using namespace std;
int Change[4][2]={{1,0},{0,1},{1,1},{1,-1}};
int graph[100][100],afterR[100][100],afterG[100][100];
int N,K;
bool flagR,flagB;
bool CheckOK(int a,int b)
{
    return a>=0&&a<N&&b>=0&&b<N;
}
void CheckR(int a,int b)
{
    int i,c;
    bool flag;
    for (c=0;c<4;c++)
    {
        flag=true;
        for (i=1;i<K;i++)
        {
            if (CheckOK(a+i*Change[c][0],b+i*Change[c][1]))
            {
                if (afterG[a+i*Change[c][0]][b+i*Change[c][1]]!=1)
                {
                    flag=false;
                    break;
                }
            }
            else
            {
                flag=false;
                break;
            }
        }
        if (flag) flagR=true;
    }


}


void CheckB(int a,int b)
{
    int i,c;
    bool flag;
    for (c=0;c<4;c++)
    {
        flag=true;
        for (i=1;i<K;i++)
        {
            if (CheckOK(a+i*Change[c][0],b+i*Change[c][1]))
            {
                if (afterG[a+i*Change[c][0]][b+i*Change[c][1]]!=2)
                {
                    flag=false;
                    break;
                }
            }
            else
            {
                flag=false;
                break;
            }
        }
        if (flag) flagB=true;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas,t;
    int i,j;
    scanf("%d",&cas);
    for (t=1;t<=cas;t++)
    {
        memset(graph,0,sizeof(graph));
        memset(afterR,0,sizeof(afterR));
        memset(afterG,0,sizeof(afterG));
        scanf("%d %d",&N,&K);
        for (i=N-1;i>=0;i--)
        {
            char temp[100];
            scanf("%s",temp);
            for (j=0;j<N;j++)
            {
                if (temp[j]=='.') graph[i][j]=0;
                else if (temp[j]=='R') graph[i][j]=1;
                else if (temp[j]=='B') graph[i][j]=2;
            }
        }
        for (i=0;i<N;i++)
            for (j=0;j<N;j++)
            {
                afterR[i][j]=graph[j][N-1-i];
            }

        int tempcou=0;
        for (i=0;i<N;i++) //iÎªÁÐ
        {
            tempcou=0;
            for (j=0;j<N;j++)
            {
                if (afterR[j][i]!=0) afterG[tempcou++][i]=afterR[j][i];
            }
        }

        flagR=false,flagB=false;
        for (i=0;i<N;i++)
            for (j=0;j<N;j++)
            {
                if (!flagR&&afterG[i][j]==1) CheckR(i,j);
                if (!flagB&&afterG[i][j]==2) CheckB(i,j);
            }
        printf("Case #%d: ",t);
        if (flagR&&flagB) printf("Both");
        if (flagR&&!flagB) printf("Red");
        if (!flagR&&flagB) printf("Blue");
        if (!flagR&&!flagB) printf("Neither");
        printf("\n");

    }
    return 0;
}
