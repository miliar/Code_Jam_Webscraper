#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

int cnt[300];


int judge(char a[][5])
{
    int i,j;
    int status = 0;

    memset(cnt, 0, sizeof(cnt));
    for(i=0;i<4;++i)
    {
        cnt['X']=0, cnt['O']=0, cnt['T']=0;
        for(j=0;j<4;++j)
            ++cnt[a[i][j]];
        if(cnt['X']+cnt['T']==4) return 1;
        else if(cnt['O']+cnt['T']==4) return 2;
    }

    for(i=0;i<4;++i)
    {
        cnt['X']=0, cnt['O']=0, cnt['T']=0;
        for(j=0;j<4;++j)
            ++cnt[a[j][i]];
        if(cnt['X']+cnt['T']==4) return 1;
        else if(cnt['O']+cnt['T']==4) return 2;
    }


    cnt['X']=0, cnt['O']=0, cnt['T']=0;
    for(j=0,i=0;j<4 && i<4;++j, ++i)
        ++cnt[a[i][j]];
    if(cnt['X']+cnt['T']==4) return 1;
    else if(cnt['O']+cnt['T']==4) return 2;

    cnt['X']=0, cnt['O']=0, cnt['T']=0;
    for(j=3,i=0;j>=0 && i<4;--j, ++i)
        ++cnt[a[i][j]];
    if(cnt['X']+cnt['T']==4) return 1;
    else if(cnt['O']+cnt['T']==4) return 2;

    if(cnt['.']>0) return 4;
    else return 3;
}

int main()
{
    int T,i,j,ans;
    char a[5][5];
    scanf("%d", &T);
    for(i=1;i<=T;++i)
    {
        for(j=0;j<4;++j)
            scanf("%s", a[j]);
        if(i!=T)
            getchar();
        ans = judge(a);

        printf("Case #%d: ", i);
        if(ans == 1)
            printf("X won\n");
        else if(ans == 2)
            printf("O won\n");
        else if(ans == 3)
            printf("Draw\n");
        else
            printf("Game has not completed\n");
    }
    return 0;
}
