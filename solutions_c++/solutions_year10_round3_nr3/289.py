#include<stdio.h>
#include<algorithm>
using namespace std;

FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

int n , m , rank[200] , arr[40][40] , ret[40] , vis[40][40];

bool check(int x , int y , int xx , int yy)
{
    int i , a;
    if(xx >= n || yy >= m) return 0;
    for(i=x;i<=xx;i++)
        for(a=y;a<=yy;a++)
        {
            if(vis[i][a]) return 0;
            if(i+1 <= xx && arr[i][a] == arr[i+1][a]) return 0;
            if(a+1 <= yy && arr[i][a] == arr[i][a+1]) return 0;
        }
    for(i=x;i<=xx;i++)
        for(a=y;a<=yy;a++)
            vis[i][a] = 1;
    return 1;
}

int main()
{
    int i , a , k , caseID = 0 , j , c;
    char x[1000];
    for(i='0';i<='9';i++) rank[i] = i - '0';
    for(i='A';i<='Z';i++) rank[i] = i - 'A' + 10;
    fscanf(in,"%d",&k);
    while(k--)
    {
        fprintf(out,"Case #%d: ",++caseID);
        fscanf(in,"%d %d",&n,&m);
        for(i=0;i<n;i++)
        {
            fscanf(in,"%s",x);
            for(a=0;a<m/4;a++)
            {
                int mask = rank[x[a]];
                arr[i][a*4] = mask & (1 << 3);
                arr[i][a*4+1] = mask & (1 << 2);
                arr[i][a*4+2] = mask & (1 << 1);
                arr[i][a*4+3] = mask & (1 << 0);
            }
            for(a=0;a<m;a++) if(arr[i][a]) arr[i][a] = 1;
        }
        memset(ret,0,sizeof ret);
        memset(vis,0,sizeof vis);
        c = 0;
        for(j=n;j>-1;j--)
            for(i=0;i<n;i++)
                for(a=0;a<m;a++)
                    if(check(i,a,i+j,a+j))
                    {
                        if(!ret[j]) c++;
                        ret[j]++;
                    }
        fprintf(out,"%d\n",c);
        for(i=n;i>-1;i--)
            if(ret[i]) fprintf(out,"%d %d\n",i+1,ret[i]);
    }
    return 0;
}
