#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<queue>
using namespace std ;

class node
{
    public:
    int ar[10];
    int cost;
}cur,t;
queue<node>q,tempoq;
bool flag[8][8][8][8][8][8][8][8];
bool mat[10][10];
int ep[10];
int n;

bool check()
{
    int c,c2;
    for (c=0;c<n;c++)
    {
        if (ep[cur.ar[c]]>c)return 0;
    }
    return 1;
}

int main()
{
    FILE *in=fopen("row.in","r");
    freopen("row.out","w",stdout);
    int tests;
    fscanf(in,"%d",&tests);
    int c,c2;
    int testn=1;
    while (tests)
    {
        printf("Case #%d: ",testn);
        testn++;
        tests--;
        fscanf(in,"%d",&n);
        for (c=0;c<n;c++)
        fscanf(in,"%s",mat[c]);
        for (c=0;c<n;c++)
        {
            for (c2=n-1;c2>=0;c2--)
            if (mat[c][c2]=='1')break;
            ep[c]=c2;
        }
        memset(flag,0,sizeof(flag));
        flag[0][1][2][3][4][5][6][7]=1;
        q=tempoq;
        for (c=0;c<8;c++)
        t.ar[c]=c;
        t.cost=0;
        q.push(t);
        while(!q.empty())
        {
            cur=q.front();
            q.pop();
            if (check()){printf("%d\n",cur.cost);break;}
            for (c=0;c<n-1;c++)
            {
                t=cur;
                t.cost++;
                swap(t.ar[c],t.ar[c+1]);
                if (flag[t.ar[0]][t.ar[1]][t.ar[2]][t.ar[3]][t.ar[4]][t.ar[5]][t.ar[6]][t.ar[7]])continue;
                flag[t.ar[0]][t.ar[1]][t.ar[2]][t.ar[3]][t.ar[4]][t.ar[5]][t.ar[6]][t.ar[7]]=1;
                q.push(t);
            }
        }
    }
//    system("pause");
    return 0;
}



































