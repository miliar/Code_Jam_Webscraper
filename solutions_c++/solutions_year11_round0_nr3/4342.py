#include<stdio.h>
#include<string.h>
#define MAX(X,Y)  (X > Y ? X : Y)
#define PRT2(X,DIGIT)  {for(int _TMP=DIGIT-1; _TMP>=0; _TMP--)  printf("%d",(X&(1<<_TMP))>0);}
int T, N, C[1005];
int sum, max;
char used[1005];
int remain()
{
    int nowXOR = 0;
    for(int i=1; i<=N; i++)
        if(!used[i])
            nowXOR ^= C[i];
//    printf("  ");
//    PRT2(nowXOR, 4);
    return nowXOR;
}
void solve(int at, int now, int nowXOR)
{
    if(at>=N)
    {
//        printf(">> %2d: ",now);
//        PRT2(nowXOR, 4);
        if(now!=sum  &&  now > max  &&  remain()==nowXOR)  max = now;
//        printf("\n");
        return;
    }
    used[at+1] = 1;
    solve(at+1, now+C[at+1], nowXOR^C[at+1]);
    used[at+1] = 0;
    solve(at+1, now, nowXOR);
}
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        printf("Case #%d: ",t);
        memset(used, 0, 1005);
        scanf("%d",&N);
        sum = 0;
        max = 0;
        for(int i=1; i<=N; i++)  scanf("%d",&C[i]);
        for(int i=1; i<=N; i++)  sum += C[i];
        solve(0,0,0);
        if(max>0)  printf("%d\n",max);
        else  printf("NO\n");
    }
    scanf(" ");
    return 0;
}
