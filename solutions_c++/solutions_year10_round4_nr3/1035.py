#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <string>
#include <string.h>
#include <stdio.h>
#include <time.h>
#include <algorithm>

#define out(x) (cout<<#x<<" "<<x<<"  ")
#define outln(x) (cout<<#x<<" "<<x<<endl)

using namespace std;
const double eps=1e-6;

typedef long long LL;

const int N =110;

int data[N][N][2];
int result;

    void inputing()
    {
        int r;
        memset(data,0,sizeof(data));
        scanf("%d",&r);
        for (int i=0;i<r;i++)
        {
            int x1,x2,y1,y2;
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            for ( int k=y1;k<=y2;k++ )
                for ( int j=x1;j<=x2;j++ )
                {
                    data[k][j][0] = 1;
                }
        }
    }

    void work()
    {
        int now = 0;
        int next;
        bool exist;
        int r = 0;
        while (1)
        {
            next = 1 - now;
            exist = false;
            for ( int i=1;i<N;i++ )
            {
                for ( int j=1;j<N;j++ )
                {
                    if ( 1 == data[i][j][now] )
                    {
                        if ( 0 == data[i-1][j][now] && 0 == data[i][j-1][now])
                        {

                            data[i][j][next] = 0;
                        }
                        else{ data[i][j][next] = 1;exist = true;}
                    }
                    else
                    {
                        if ( 1 == data[i-1][j][now] && 1 == data[i][j-1][now])
                        {
                            exist = true;
                            data[i][j][next] = 1;
                        }
                        else data[i][j][next] = 0;
                    }
//                    if (data[i][j][next] == 1)
//                    printf("1 ");
//                    else printf("0 ");
                }
//                printf("\n");
            }
//            printf("\n");
            r++;
            if ( !exist ) break;

            now = next;
        }
        result = r;
//        outln(r);
    }


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for ( int i=1;i<=cas;i++ )
    {
        inputing();
        work();
        printf("Case #%d: %d\n",i,result);
    }
    return 0;
}

