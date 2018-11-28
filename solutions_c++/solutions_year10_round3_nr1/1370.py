#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

#define MAXN 1010
#define _cp(a,b) ((a.y)<(b.y))

struct Node{
	int x,y;
}a[MAXN],_tmp[MAXN];

typedef Node elem_t;

int inv(int n,elem_t* a){
	int l=n>>1,r=n-l,i,j;
	int ret=(r>1?(inv(l,a)+inv(r,a+l)):0);
	for (i=j=0;i<=l;_tmp[i+j]=a[i],i++)
		for (ret+=j;j<r&&(i==l||!_cp(a[i],a[l+j]));_tmp[i+j]=a[l+j],j++);
	memcpy(a,_tmp,sizeof(elem_t)*n);
	return ret;
}

bool cmp(Node a, Node b){
     if (a.x==b.x) return a.y<b.y;
     else return a.x<b.x;
}

int main(){
	int cas,k,n,i;
	freopen("A-large.in","r",stdin);
	freopen("ans.out","w",stdout);
	scanf("%d",&cas);
	for (k=1; k<=cas; k++){
		scanf("%d",&n);
		for (i=0; i<n; i++){
			scanf("%d%d",&a[i].x,&a[i].y);
		}
		sort(a,a+n,cmp);
		printf("Case #%d: %d\n",k,inv(n,a));
	}
//	system("pause");
}
