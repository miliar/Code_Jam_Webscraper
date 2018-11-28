/*

TASK:
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<set>
#include<algorithm>
#define INF 123456789

using namespace std;
FILE *fin,*fout;

inline int MAXX(int x,int y) {return x > y ? x : y ;}
inline int MINN(int x,int y) {return x < y ? x : y ;}
int comparez(const void *x, const void *y)
{
    return (*(int*)x - *(int*)y);
}

//-----------------------------------------------------

int tl;
int p;
int want[1100];
int price[11][520];
int ans[11][520][11];

int main()
{
    int i,j,k;
    int a,b;
    fin = fopen("B-large.in","r");
    fout = fopen("B-large.out","w");
    fscanf(fin,"%d",&tl);
    
    for(int tt=0;tt<tl;tt++)
    {
        printf("Case #%d\n",tt+1);
        fprintf(fout,"Case #%d: ",tt+1);
        fscanf(fin, "%d", &p);
        for(i=0; i<(1<<(p-1)); i++)
        {
            fscanf(fin, "%d%d", &a, &b);
            want[i] = MAXX(p-a, p-b);
            //printf("%d ", want[i]);
        }
        for(i=p-1; i>=0; i--)
        {
            for(j=0; j<(1<<i); j++)
            {
                fscanf(fin, "%d", &a);
                price[i][j] = a;
            }
        }
        //printf("\n");
        
        //for(i=0; i<11; i++) for(j=0; j<520; j++) for(k=0; k<11; k++) ans[i][j][k] = INF;
        i = p-1;
        for(j=0; j<(1<<i); j++)
        {
            for(k=0; k<=i; k++)
            {
                ans[i][j][k] = INF;
                if(want[j] == k+1)
                    ans[i][j][k] = price[i][j];
                else if(want[j] <= k)
                    ans[i][j][k] = 0;
                //printf("ans %d %d %d %d\n", i,j,k,ans[i][j][k]);
            }
        }
        for(i=p-2; i>=0; i--)
        {
            for(j=0; j<(1<<i); j++)
            {
                for(k=0; k<=i; k++)
                {
                    ans[i][j][k] = INF;
                    //not buy
                    ans[i][j][k] = MINN(ans[i][j][k], ans[i+1][j*2][k] + ans[i+1][j*2+1][k]);
                    //buy
                    ans[i][j][k] = MINN(ans[i][j][k], ans[i+1][j*2][k+1] + ans[i+1][j*2+1][k+1]
                                                      + price[i][j]);
                    //printf("ff %d %d\n", ans[i+1][j*2][k], ans[i+1][j*2+1][k]);
                }
            }
        }
        /*
        for(i=p-1; i>=0; i--)
        {
            for(k=0; k<=i; k++)
            {
                for(j=0; j<(1<<i); j++)
                {
                    printf("%d ", ans[i][j][k]);
                }
                printf("\n");
            }
            printf("\n");
        }
        printf("\n");
        */
        fprintf(fout, "%d\n", ans[0][0][0]);

    }
    system("PAUSE");
    return 0;
}
