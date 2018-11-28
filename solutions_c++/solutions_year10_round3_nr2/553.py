#include<stdio.h>
#include<cstring>
#include<algorithm>

using namespace std;

int an[1002][1002];
bool ud[1002][1002];

int aa(int a,int b,int c)
{
   // fprintf(stderr,"a b c %d %d %d\n",a,b,c);
    if(a*c>=b)return 0;
    if(ud[a][b])return an[a][b];
    int i,tan=b;
    for(i=a+1;i<b;i++)
    {
        tan=min(tan,max(aa(a,i,c),aa(i,b,c))+1);
    }
    ud[a][b]=1;
    an[a][b]=tan;
    return tan;
}

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    
    int cases,ii,n,i,j,a,b,c;
    
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d%d%d",&a,&b,&c);
        memset(an,0,sizeof(an));
        memset(ud,0,sizeof(ud));
        printf("Case #%d: %d\n",ii,aa(a,b,c));
        fprintf(stderr,"Case #%d: %d\n",ii,aa(a,b,c));
    }
    
    fprintf(stderr,"END\n");
    while(1);
    return 0;
}
