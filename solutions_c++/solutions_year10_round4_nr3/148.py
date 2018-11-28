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
int r;
int a[102][102]={0};

int main()
{
    int i,j,k;
    fin = fopen("C-small-attempt0.in","r");
    fout = fopen("C-small-attempt0.out","w");
    fscanf(fin,"%d",&tl);
    
    for(int tt=0;tt<tl;tt++)
    {
        printf("Case #%d\n",tt+1);
        fprintf(fout,"Case #%d: ",tt+1);
        fscanf(fin, "%d", &r);
        for(i=0; i<102; i++) for(j=0; j<102; j++) a[i][j] = 0;
        int cnt = 0;
        for(k=0; k<r; k++)
        {
            int x1,y1,x2,y2;
            fscanf(fin, "%d%d%d%d", &x1, &y1, &x2, &y2);
            for(i=x1; i<=x2; i++) for(j=y1; j<=y2; j++)
            {
                if(!a[i][j])
                {
                    a[i][j] = 1;
                    cnt++;
                }
            }
        }
        k = 0;
        while(cnt > 0)
        {
            for(i=100; i>=1; i--) for(j=100; j>=1; j--)
            {
                if(a[i][j] && !a[i-1][j] && !a[i][j-1])
                {
                    a[i][j] = 0;
                    cnt--;
                }
                else if(!a[i][j] && a[i-1][j] && a[i][j-1])
                {
                    a[i][j] = 1;
                    cnt++;
                }
            }
            k++;
        }
        fprintf(fout, "%d\n", k);

    }
    system("PAUSE");
    return 0;
}
