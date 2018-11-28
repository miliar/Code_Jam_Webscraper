#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

int pos[2] , id[1000] , idcnt , now[2] , up[2]; // 0 -> O 1 -> B

struct Node{
    int kind , pos;
    Node(int kind,int pos):kind(kind),pos(pos){}
    Node(){}
}node[1000];
int  next[2][1000];

int main()
{
    freopen("C:\\Users\\¡ıﬁ…Ó£\\Desktop\\code jam\\A-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\¡ıﬁ…Ó£\\Desktop\\code jam\\A-small-attempt0.out","w",stdout);
    char op[10];
    int i,j,k,N,ncase;scanf("%d",&ncase);
    for(int cas=1;cas<=ncase;++cas)
    {
        scanf("%d",&N);
        up[0]=up[1]=now[0]=now[1]=0;
        for(i=0;i<N;++i)
        {
            scanf("%s%d",op,&k);
            node[i]=Node(op[0]=='B',k-1);
            id[i]=(op[0]=='B');
            next[(op[0]=='B')][up[(op[0]=='B')]++] = k-1;
        }
        idcnt=0;
        pos[0]=pos[1]=0;
        int ret = 0 ;
        while(idcnt < N)
        {
                k=id[idcnt];
                if(pos[k]!=node[idcnt].pos)
                {
                    pos[k] += (pos[k]<node[idcnt].pos?1:-1);
                    ++ret;
                    if(now[k^1]<up[k^1] && pos[k^1] != next[k^1][now[k^1]])
                    {
                        pos[k^1] += ((pos[k^1]<next[k^1][now[k^1]])?1:-1);
                    }
                }
                else
                {
                    now[k] ++ ;
                    ++ret;
                    if(now[k^1]<up[k^1] && pos[k^1] != next[k^1][now[k^1]])
                    {
                        pos[k^1] += ((pos[k^1]<next[k^1][now[k^1]])?1:-1);
                    }
                    idcnt ++ ;
                }
        }
        printf("Case #%d: %d\n",cas,ret);
    }

    return 0;
}
