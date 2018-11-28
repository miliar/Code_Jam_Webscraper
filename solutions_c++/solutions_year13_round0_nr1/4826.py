#include <stdio.h>
#define CLEAR count['X']=count['O']=count['T']=0;

char map[6][6];
int count[255];

void solve()
{
    int i,j,Xwon=0,Owon=0;

    count['.']=0;
    for(i=1;i<=4;++i)
    {
        CLEAR;
        for(j=1;j<=4;++j) count[map[i][j]]++;
        if(count['X']+count['T']==4 && count['T']<=1) Xwon=1;
        if(count['O']+count['T']==4 && count['T']<=1) Owon=1;

        CLEAR;
        for(j=1;j<=4;++j) count[map[j][i]]++;
        if(count['X']+count['T']==4 && count['T']<=1) Xwon=1;
        if(count['O']+count['T']==4 && count['T']<=1) Owon=1;
    }
    CLEAR;
    for(j=1;j<=4;++j) count[map[j][j]]++;
    if(count['X']+count['T']==4 && count['T']<=1) Xwon=1;
    if(count['O']+count['T']==4 && count['T']<=1) Owon=1;

    CLEAR;
    for(j=1;j<=4;++j) count[map[j][5-j]]++;
    if(count['X']+count['T']==4 && count['T']<=1) Xwon=1;
    if(count['O']+count['T']==4 && count['T']<=1) Owon=1;

    if(Xwon == Owon)
    {
        if(count['.'])
            printf("Game has not completed\n");
        else
            printf("Draw\n");
    }
    else if(Xwon) printf("X won\n");
    else if(Owon) printf("O won\n");
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k,t,T=0;

    scanf("%d",&t);
    while(t--)
    {
        for(i=1;i<=4;++i) scanf("%s",map[i]+1);
        printf("Case #%d: ",++T);
        solve();
    }

    return 0;
}
