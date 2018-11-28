#include<iostream>
#include<stdio.h>
using namespace std;

char masiv[100][100];
char masiv2[100][100];
char masiv3[100][100];
int tests, n, k;

bool check(int x, int y, char c)
{
    int i;

    for(i=0;i<k;++i)
    {
        if(x+i >= n || masiv3[x+i][y] != c)
            break;
    }
    if(i == k)
    {
        //printf("1\n");
        return true;
    }

    for(i=0;i<k;++i)
    {
        if(y+i >= n || masiv3[x][y+i] != c)
            break;
    }

    if(i == k)
    {
        //printf("2\n");
        return true;
    }

    for(i=0;i<k;++i)
    {
        if(y+i >= n || x+i >= n || masiv3[x+i][y+i] != c)
            break;
    }
    if(i == k)
    {
        //printf("3\n");
        return true;
    }

    for(i=0;i<k;++i)
    {
        if(x+i >= n || y-i < 0 || masiv3[x+i][y-i] != c)
            break;
    }
    if(i == k)
    {
        //printf("4\n");
        return true;
    }

    return false;
}

int main()
{
    freopen("A-large.in", "rt", stdin);

    char tmp;
    scanf("%d", &tests);
    for(int t=0;t<tests;++t)
    {
        scanf("%d %d", &n, &k);
        scanf("%c", &tmp);

        for(int x=0;x<n;x++)
        {
            for(int y=0;y<n;y++)
            {
                scanf("%c", &masiv[x][y]);
            }
            scanf("%c", &tmp);
        }
        for(int x=0;x<n;x++)
        {
            for(int y=0;y<n;y++)
            {
                masiv2[x][y] = masiv[n-y-1][x];
            }
        }

        for(int x=n-1;x>=0;x--)
        {
            for(int y=0;y<n;y++)
            {
                int x1 = x;
                while(x1>0 && masiv2[x1][y] == '.')
                    x1--;
                masiv3[x][y] = masiv2[x1][y];
                masiv2[x1][y] = '.';
            }
        }
        bool r = false;
        bool b = false;
        /*
        for(int x=0;x<n;x++)
        {
            for(int y=0;y<n;y++)
            {
                printf("%c", masiv3[x][y]);
            }
            printf("\n");
        }
        */


        for(int x=0;x<n;++x)
        {
            for(int y=0;y<n;++y)
            {
                //cout<<x<<" "<<y<<" "<<check(x, y, 'R')<<" "<<check(x, y, 'B')<<endl;
                r = r || check(x, y, 'R');
                b = b || check(x, y, 'B');
            }
        }
        printf("Case #%d: ", t+1);
        if(!r && !b)
            printf("Neither\n");
        if(r && !b)
            printf("Red\n");
        if(!r && b)
            printf("Blue\n");
        if(r && b)
            printf("Both\n");

    }
    return 0;
}
