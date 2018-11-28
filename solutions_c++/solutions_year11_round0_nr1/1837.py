#include<stdio.h>
#include<queue>
#include<string.h>
#include<string>
using namespace std;

struct ss
{
    int o,b,t,pos;
};

struct pt
{
    char c;
    int pos;
};

pt P[1000];
int N;

int vis[120][120][120],True;

int bfs()
{
    ss s1,s2,s3;
    s1.o=1;s1.b=1;s1.pos=0;s1.t=0;
    True++;
    vis[s1.o][s1.b][s1.pos]=True;
    queue<ss>Q;
    Q.push(s1);
    while(!Q.empty())
    {
        s1=Q.front();
        Q.pop();
        if(s1.pos==N) return s1.t;
        if(P[s1.pos].c=='O'&&P[s1.pos].pos==s1.o)
        {
            s2.pos=s1.pos+1;
            s2.b=s1.b;s2.o=s1.o;s2.t=s1.t+1;
            if(vis[s2.o][s2.b][s2.pos]!=True) {
                vis[s2.o][s2.b][s2.pos]=True;
                Q.push(s2);
            }
            if(s1.b+1<=100) {
                s2.b=s1.b+1;
                if(vis[s2.o][s2.b][s2.pos]!=True) {
                    vis[s2.o][s2.b][s2.pos]=True;
                    Q.push(s2);
                }

            }
            if(s1.b-1>=1)
            {
                s2.b=s1.b-1;
                if(vis[s2.o][s2.b][s2.pos]!=True) {
                    vis[s2.o][s2.b][s2.pos]=True;
                    Q.push(s2);
                }
            }

        }
        else if(P[s1.pos].c=='B'&&P[s1.pos].pos==s1.b)
        {
            s2.pos=s1.pos+1;
            s2.b=s1.b;s2.o=s1.o;s2.t=s1.t+1;
            Q.push(s2);
            if(s1.o+1<=100) {
                s2.o=s1.o+1;
                if(vis[s2.o][s2.b][s2.pos]!=True) {
                    vis[s2.o][s2.b][s2.pos]=True;
                    Q.push(s2);
                }
            }
            if(s1.o-1>=1)
            {
                s2.o=s1.o-1;
                if(vis[s2.o][s2.b][s2.pos]!=True) {
                    vis[s2.o][s2.b][s2.pos]=True;
                    Q.push(s2);
                }
            }
        }

        for(int i=-1;i<=1;i++)
        {
            for(int j=-1;j<=1;j++)
            {
                if(i==0&&j==0) continue;
                s2.o=s1.o+i;
                s2.b=s1.b+j;
                s2.pos=s1.pos;
                s2.t=s1.t+1;
                if(s2.o>=1&&s2.o<=100&&s2.b>=1&&s2.b<=100)
                {
                    if(vis[s2.o][s2.b][s2.pos]!=True) {
                        vis[s2.o][s2.b][s2.pos]=True;
                        Q.push(s2);
                    }
                }
            }
        }


    }
    return 0;

}

char fao[20];
int main()
{
    int tst,cas;
    freopen("A.in","rt",stdin);
    freopen("A.out","wt",stdout);
    scanf("%d",&tst);
    for(cas=1;cas<=tst;cas++)
    {
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            scanf("%s %d",&fao,&P[i].pos);
            P[i].c=fao[0];
        }
        printf("Case #%d: %d\n",cas,bfs());
    }
    return 0;
}
