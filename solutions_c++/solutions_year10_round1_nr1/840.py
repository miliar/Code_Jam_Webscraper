#include <stdio.h>

int n,kk;

int checkwin(char b[55][55], int r, int c, int k)
{
    if(b[r][c]=='.')return 0;
    int rr,cc;
    int l = 1;
    for(rr=r+1;rr<n;++rr)
        if(b[rr][c]==b[r][c])++l;
        else break;
    for(rr=r-1;rr>=0;--rr)
        if(b[rr][c]==b[r][c])++l;
        else break;
    if ( l >= k ) return (int)b[r][c];
    l = 1;
    for(cc=c+1;cc<n;++cc)
        if(b[r][cc]==b[r][c])++l;
        else break;
    for(cc=c-1;cc>=0;--cc)
        if(b[r][cc]==b[r][c])++l;
        else break;
    if ( l >= k ) return (int)b[r][c];
    l=1;
    cc=c+1;rr=r+1;
    while(cc<n&&rr<n&&b[rr][cc] == b[r][c])
    {
        ++l;
        ++rr;
        ++cc;
    }
    cc=c-1;rr=r-1;
    while(cc>=0 && rr >=0 && b[rr][cc] == b[r][c])
    {
        ++l;
        --rr;
        --cc;
    }
    if ( l >= k ) return (int)b[r][c];
    l=1;
    cc=c+1;rr=r-1;
    while(cc<n&&rr>=0&&b[rr][cc] == b[r][c])
    {
        ++l;
        --rr;
        ++cc;
    }
    cc=c-1;rr=r+1;
    while(cc>=0 && rr < n && b[rr][cc] == b[r][c])
    {
        ++l;
        ++rr;
        --cc;
    }
    if ( l >= k ) return (int)b[r][c];
    return 0;
}

int main()
{
    int t;
    char b[55][55];
    char nb[55][55];
    scanf("%d", &t);
    for (int i = 1;i <=t;++i)
    {
        scanf("%d%d",&n,&kk);
        for(int j=0;j<n;++j)
            scanf("%s",b[j]);
        for(int j=0;j<n;++j)
        {
            for(int k = 0; k<n;++k)
            {
                nb[j][k] = b[n-k-1][j];
                //printf("%c", nb[j][k]);
            }
            //printf("\n");
        }
        for (int c=0;c<n;++c)
        {
            int ta = n-1;
            int sr = n-1;
            while(1)
            {
                for(;ta>=0;--ta)
                    if(nb[ta][c]!='.')
                        break;
                if(ta<0)break;
                if(sr!=ta)
                {
                    nb[sr][c]=nb[ta][c];
                    nb[ta][c]='.';
                }
                sr--;
                ta--;
            }
        }
        int rwin = 0, bwin=0,win=0;
        for(int j=0;j<n;++j)
        {
            for(int k = 0; k<n;++k)
            {
                win = checkwin(nb, j, k, kk);
                if(win=='R')
                {
                    rwin=1;
                    //printf("rwin: %d %d\n", j,k);
                }
                else if(win=='B')bwin=1;
                if(rwin && bwin)break;
                //printf("%c", nb[j][k]);
            }
            if(rwin && bwin)break;
            //printf("\n");
        }
        printf("Case #%d: ", i);
        if(rwin && bwin)printf("Both\n");
        else if(rwin)printf("Red\n");
        else if(bwin)printf("Blue\n");
        else printf("Neither\n");
    }
    return 0;
}
