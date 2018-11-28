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
inline int btw(int x,int s1,int s2) {return (x >= s1 && x < s2);}
int comparez(const void *x, const void *y)
{
    return (*(int*)x - *(int*)y);
}

//-----------------------------------------------------

int tl;
int k;
int d[110][110];

int mimi()
{
    int n,a,b;
    int i,j,ok;
    n = k;
    while(1)
    {
        printf("%d\n", n);
        for(a=0;a<=n-k;a++) for(b=0;b<=n-k;b++)
        {
            //printf("- %d %d\n", a, b);
            ok = 1;
            for(i=0;i<k;i++)
            {
                for(j=0;j<k;j++)
                {
                    if(btw(j+b-a, 0, k) && btw(i+a-b, 0, k) && d[i][j] != d[j+b-a][i+a-b])
                        ok = 0;
                    if(btw(n-1-a*2-i, 0, k) && btw(n-1-b*2-j, 0, k) && d[i][j] != d[n-1-a*2-i][n-1-b*2-j])
                        ok = 0;
                    if(btw(n-1-b-a-j, 0, k) && btw(n-1-b-a-i, 0, k) && d[i][j] != d[n-1-b-a-j][n-1-b-a-i])
                        ok = 0;
                }
                if(!ok) break;
            }
            if(ok) return n;
        }
        n++;
    }
}

int main()
{
    int i,j,a;
    fin = fopen("A-large.in","r");
    fout = fopen("A-large.out","w");
    fscanf(fin,"%d",&tl);
    
    for(int tt=0;tt<tl;tt++)
    {
        printf("Case %d\n", tt+1);
        fprintf(fout,"Case #%d: ",tt+1);
        //for(i=0; i<110; i++) for(j=0; j<110; j++) d[i][j] = 0;
        fscanf(fin, "%d", &k);
        //for(i=0;i<k;i++) for(j=0;j<k;j++) fscanf(fin, "%d", &d[i][j]);
        for(i=0; i<k; i++)
        {
            for(j=0; j<=i; j++)
            {
                fscanf(fin, "%d", &a);
                d[j][i-j] = a;
            }
        }
        for(i=k-2; i>=0; i--)
        {
            for(j=0; j<=i; j++)
            {
                fscanf(fin, "%d", &a);
                d[j+k-i-1][k-j-1] = a;
            }
        }
        for(i=0;i<k;i++) {for(j=0;j<k;j++) printf("%d ", d[i][j]); printf("\n");}
        i = mimi();
        fprintf(fout, "%d\n", i*i - k*k);


    }
    system("PAUSE");
    return 0;
}
