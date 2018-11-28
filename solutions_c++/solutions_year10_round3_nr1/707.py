#include <stdio.h>
#include <algorithm>
#include <string.h>
#define MAXN 1004
#define _cp(a,b) ((a)<=(b))
using namespace std;

typedef int elem_t;

elem_t _tmp[MAXN];

int inv(int n,elem_t* a){
	int l=n>>1,r=n-l,i,j;
	int ret=(r>1?(inv(l,a)+inv(r,a+l)):0);
	for (i=j=0;i<=l;_tmp[i+j]=a[i],i++)
		for (ret+=j;j<r&&(i==l||!_cp(a[i],a[l+j]));_tmp[i+j]=a[l+j],j++);
	memcpy(a,_tmp,sizeof(elem_t)*n);
	return ret;
}
struct node
{
    int x,y;
}s[1004];
int q[1004];

bool cmp(node x,node y)
{
    return x.x<y.x;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,i,n,j;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d %d",&s[i].x,&s[i].y);
        }
        sort(s,s+n,cmp);
        for(i=0;i<n;i++)
        {
            q[i]=s[i].y;
        }
        printf("Case #%d: %d\n",j,inv(n,q));
    }
    return 0;
}
        
