#include<stdio.h>
#include<map>

char v[10][10];
int nr[1010];
int ok,prt,T,case1;
int init()
{
    for(int i=0;i<=256;++i)
        nr[i]=0;
}
void verif()
{
if(prt==1)
    return;
//printf("%d %d\n",nr['X'],nr['T']);
    if(nr['X']==4 || (nr['X'] == 3 && nr['T']==1))
            {
            printf("Case #%d: X won\n",case1);
            prt=1;
            }

    if(nr['O']==4 || (nr['O'] == 3 && nr['T']==1))
            {
            prt=1;
            printf("Case #%d: O won\n",case1);
            }
    init();
}
void check()
{
ok=0;
prt=0;
    for(int i=1;i<=4;++i)
        {
        init();
            for(int j=1;j<=4;++j)
            {
            //printf("%c",v[i][j]);
            if(v[i][j]!='.')
                nr[v[i][j]]++;
            else ok=1;
            }
            verif();
        }
        init();
    for(int i=1;i<=4;++i)
        {
            init();
            for(int j=1;j<=4;++j)
            {
            if(v[j][i]!='.')
            nr[v[j][i]]++;
            else ok=1;
            }
            verif();
        }
    init();
    for(int i=1;i<=4;++i)
    {
        nr[v[i][i]]++;
    }
    verif();

    for(int i=1;i<=4;++i)
    nr[v[i][5-i]]++;
    verif();
    if(prt==0)
    {
    if(ok)
        printf("Case #%d: Game has not completed\n",case1);
    else printf("Case #%d: Draw\n",case1);
    }
}

int main()
{
freopen("A.in","r",stdin);
freopen("test.txt","w",stdout);
    scanf("%d\n",&T);
    while(T--)
    {++case1;
        for(int i=1;i<=4;++i)
            scanf("%s\n",v[i]+1);
            init();
        check();
    }
}
