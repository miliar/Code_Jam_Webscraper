#include <cstdio>
#include <algorithm>
using namespace std;

struct node {
int from,be,en;
};


int a[500][500],d[500],b[500];
node p[500];

bool cmp(const node &a,const node &b) {
	return (a.be<b.be) || ((a.be==b.be) && (a.en<b.en));
}


int main() {
int z,zz,x,y,t,n,i,j;
	for (scanf("%d",&zz),z=1;z<=zz;++z) {	
		n=0;
		scanf("%d",&t);
		for (scanf("%d%d",&i,&j);i;--i) {
			scanf("%d:%d",&x,&y);
			p[n].be=x*60+y;
			scanf("%d:%d",&x,&y);
			p[n].en=x*60+y;
			p[n++].from=0;
		}
		for (;j;--j) {
			scanf("%d:%d",&x,&y);
			p[n].be=x*60+y;
			scanf("%d:%d",&x,&y);
			p[n].en=x*60+y;
			p[n++].from=1;
		}
		sort(p,p+n,cmp);
		d[0]=d[1]=b[0]=b[1]=0;
		for (i=0;i<n;++i) {
			x=p[i].from;
			if ((d[x]==0) || (a[x][0]>p[i].be)) {
				++b[x];
			}
			else {
				a[x][0]=a[x][--d[x]];
				sort(a[x],a[x]+d[x]);
			}
			a[1-x][d[1-x]++]=p[i].en+t;
			sort(a[1-x],a[1-x]+d[1-x]);
		}
		printf("Case #%d: %d %d\n",z,b[0],b[1]);
	}
	return 0;
}




