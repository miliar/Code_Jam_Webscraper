/*
TASK: rows
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
int n;
int a[100];

int main()
{
    int i,j;
    char temp[100];
    fin = fopen("A-large.in","r");
    fout = fopen("rowslg.out","w");
    fscanf(fin,"%d",&tl);
    
    for(int tt=0;tt<tl;tt++)
    {
        fprintf(fout,"Case #%d: ",tt+1);
        fscanf(fin,"%d",&n);
        for(i=0;i<n;i++)
        {
            fscanf(fin,"%s",temp);
            printf("%s\n",temp);
            a[i] = 0;
            for(j=0;j<n;j++) {if(temp[j]=='1') a[i] = j;}
        }
        for(i=0;i<n;i++) printf("%d\n",a[i]);
        //greedy
        int cnt=0;
        for(i=0;i<n;i++)
        {
            int uu=n;
            for(j=n;j>=i;j--)
            {
                if(a[j]<=i) uu = j;
            }
            for(;uu>i;uu--)
            {
                int cc;
                cc = a[uu]; a[uu] = a[uu-1]; a[uu-1] = cc;
                cnt++;
            }
            for(int ii=0;ii<n;ii++) printf("%d ",a[ii]);printf("\n");
        }
        fprintf(fout,"%d\n",cnt);
    }
    system("PAUSE");
    return 0;
}
