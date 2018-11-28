/*
TASK: stock
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
int n,k,maxi,cnt;
int a[102][30];
int g[102][102];
int d[102];

int pui(int now)
{
    cnt++; d[now]=1;
    int i,j;
    for(i=now+1;i<n;i++)
    {
        for(j=0;j<n;j++) if(d[j] && !g[j][i]) break;
        if(j==n) pui(i);
    }
    if(cnt>maxi) maxi = cnt;
    cnt--; d[now]=0;
}

int main()
{
    int i,j;
    fin = fopen("C-small-attempt1.in","r");
    fout = fopen("stocksm.out","w");
    fscanf(fin,"%d",&tl);
    
    for(int tt=0;tt<tl;tt++)
    {
        fprintf(fout,"Case #%d: ",tt+1);
        fscanf(fin,"%d %d",&n,&k);
        for(i=0;i<n;i++)
        {
            for(j=0;j<k;j++)
            {
                fscanf(fin,"%d",&a[i][j]);
            }
        }
        for(i=0;i<102;i++) for(j=0;j<102;j++) g[i][j]=0;
        for(i=0;i<102;i++) d[i] = 0;
        
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                int ii,sn; ii=0;
                sn = a[i][0] - a[j][0];
                if(sn>0) sn=1; else if(sn<0) sn=-1;
                if(sn!=0)
                {  
                    for(ii=1;ii<k;ii++)
                    {
                        if(sn*(a[i][ii]-a[j][ii])<=0) break;
                    }
                }
                if(ii<k) g[i][j] = 1;
            }
        }
        //for(i=0;i<n;i++) { for(j=0;j<n;j++) printf("%d ",g[i][j]); printf("\n");}
        maxi = 0; cnt = 0;
        for(i=0;i<n;i++)
        pui(i);
        fprintf(fout,"%d\n",maxi);
    }
    system("PAUSE");
    return 0;
}
