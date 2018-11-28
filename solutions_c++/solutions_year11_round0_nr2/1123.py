#include <iostream>
#include <cstdio>

using namespace std;

int ord[2][105], pos[2][105];

bool trymove(int &pos, int tgt)
{
    if(pos == tgt) return true;
    if(pos < tgt) pos++;
    else pos--;
    return false;
}

void process(void)
{
    int N;
    int n[2] = {0,0};
    scanf("%d",&N);
    for(int i=0;i<N;i++)
    {
        char a;
        int b;
        scanf(" %c %d",&a,&b);
        int c = (a=='B'?0:1);

        ord[c][n[c]]=i;
        pos[c][n[c]]=b;
        n[c]++;
    }

    ord[0][n[0]] = 99999;
    ord[1][n[1]] = 99999;

    int p[2] = {0,0};
    int pp[2] = {1,1};
    int cur=0;

    for(int i=0;;i++)
    {
        if(p[0] == n[0] && p[1] == n[1]) 
        {
            printf("%d\n",i);
            break;
        }

        int move = (cur == ord[0][p[0]]?0:1);

        int nmove = !move;
        if(p[nmove] != n[nmove])
        {
            trymove(pp[nmove], pos[nmove][p[nmove]]);
        }

        if(trymove(pp[move], pos[move][p[move]]))
        {
            // push this.
            p[move]++;
            cur++;
        }
    }

}

int main(void)
{
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        printf("Case #%d: ",i+1);
        process();
    }
}
