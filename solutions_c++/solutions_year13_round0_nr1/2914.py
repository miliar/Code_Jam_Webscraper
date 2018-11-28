#include <cstdio>
char a[7][7];
int main ()
{
    //freopen("a.out","r",stdin);
    //freopen("b.out","w",stdout);
    int cas, t = 0;
    int sum, ans, sum_, _sum, dot;
    scanf("%d",&cas); getchar();
    while(t++<cas)
    {
        ans = -1;
        for(int i = 0; i < 4; i++, getchar()) scanf("%s",a[i]);getchar();
        sum_ = _sum = 0;dot = 0;
        for(int i = 0; ans==-1&&i < 4; i++)
        {

            sum = 0;
            for(int j = 0; j < 4; j++) {sum += a[i][j]; if(a[i][j]=='.') dot = 1;}
            if(sum=='X'*4||sum=='X'*3+'T') ans = 'X';
            if(sum=='O'*4||sum=='O'*3+'T') ans = 'O';
            sum = 0;
            for(int j = 0; j < 4; j++) sum += a[j][i];
            if(sum=='X'*4||sum=='X'*3+'T') ans = 'X';
            if(sum=='O'*4||sum=='O'*3+'T') ans = 'O';
            _sum += a[i][i];
            sum_ += a[i][3-i];
        }
        if(ans==-1)
        {
            if(_sum=='X'*4||_sum=='X'*3+'T'||sum_=='X'*4||sum_=='X'*3+'T') ans = 'X';
            if(_sum=='O'*4||_sum=='O'*3+'T'||sum_=='O'*4||sum_=='O'*3+'T') ans = 'O';
        }
        printf("Case #%d: ",t);
        if(ans==-1&&dot==1) puts("Game has not completed");
        else if(ans==-1&&dot==0) puts("Draw");
        else printf("%c won\n", ans);
    }
    return 0;
}
