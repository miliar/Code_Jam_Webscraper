#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

class POINT
{
    public:
        int i,j,h;
}pnt[10005];
int mat[105][105];
int n,m;
int cnt;
int bas;
bool cmp(POINT a,POINT b)
{
    if (a.h!=b.h)return a.h<b.h;
    if (a.i!=b.i)return a.i<b.i;
    return a.j<b.j;
}
int flag[105][105];
int row[]={-1,0,0,1};
int col[]={0,-1,1,0};
int lx,ly;
void flood(int i,int j)
{
    if (flag[i][j]!=-1)return;
    int c,c2;
    int mv=1<<30,mi,mj;
    if (lx!=n)
    {
        for (c=0;c<4;c++)
        {
            int i2=i+row[c],j2=j+col[c];
            if (i2<0||j2<0||i2>=n||j2>=m)continue;
            if (mat[i2][j2]<mv){mv=mat[i2][j2];mi=i2;mj=j2;}
        }
    }
    else {mi=lx;mj=ly;}
    if (lx!=mi||ly!=mj)return;
    flag[i][j]=bas;
    for (c=0;c<4;c++)
    {
        lx=i;
        ly=j;
        int i2=i+row[c],j2=j+col[c];
        if (i2<0||j2<0||i2>=n||j2>=m)continue;
        if (mat[i2][j2]>mat[i][j])
        flood(i2,j2);
    }
    return;
}
int print[30];

int main()
{
    FILE *in=fopen("bas.in","r");
    freopen("bas.out","w",stdout);
    int tests;
    int c,c2;
    fscanf(in,"%d",&tests);
    int testn=1;
    while(tests)
    {
        tests--;
        printf("Case #%d:\n",testn);
        testn++;
        fscanf(in,"%d %d",&n,&m);
        cnt=0;
        for (c=0;c<n;c++)
        for (c2=0;c2<m;c2++)
        {
            fscanf(in,"%d",&mat[c][c2]);
            pnt[cnt].i=c;
            pnt[cnt].j=c2;
            pnt[cnt].h=mat[c][c2];
            cnt++;
        }
        sort(pnt,pnt+cnt,cmp);
        memset(flag,-1,sizeof(flag));
        bas=0;
        mat[n][m]=-1;
        for (c=0;c<cnt;c++)
        {
            if (flag[pnt[c].i][pnt[c].j]!=-1)continue;
            lx=n;
            ly=m;
            flood(pnt[c].i,pnt[c].j);
            bas++;
        }
        memset(print,-1,sizeof(print));
        bas=0;
        for (c=0;c<n;c++)
        for (c2=0;c2<m;c2++)
        {
            if (print[flag[c][c2]]==-1){print[flag[c][c2]]=bas;bas++;}
        }
        for (c=0;c<n;c++)
        {
        for (c2=0;c2<m;c2++)
        {
            if (c2)printf(" ");
            printf("%c",print[flag[c][c2]]+'a');
        }
        printf("\n");
        }
    }
//    system("pause");
    return 0;
}
