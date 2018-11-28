#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <set>

using namespace std;

struct node {
	int r,idx;
	int x,y;
};

node a[10000];
int tt;
int n,m,w,l,ii;
int f[10000][3];

bool cmp1(const node &a,const node &b) {
	return a.r>b.r;
}

bool cmp2(const node &a,const node &b) {
	return a.idx<b.idx;
}

void out(int x) {
	sort(a,a+n,cmp2);
	printf("Case #%d:",ii);
	for (int i=0;i<n;++i) {
		if (x!=0) swap(a[i].x,a[i].y);
		printf(" %d.0 %d.0",a[i].x,a[i].y);
	}
	printf("\n");
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	scanf("%d",&tt);

	for (ii=1;ii<=tt;++ii) {
		scanf("%d%d%d",&n,&w,&l);
		for (int i=0;i<n;++i) {
			scanf("%d",&a[i].r);
			a[i].idx=i;
			a[i].x=-1; a[i].y=-1;
		}

		sort(a,a+n,cmp1);
		m=1;
		f[0][0]=0; f[0][1]=w; f[0][2]=0;
		bool flag=true;
		for (int i=0;i<n;++i) {
			int tmp=-1,now=l;
			for (int j=0;j<m;++j) {
				if (f[j][1]-f[j][0]>=2*a[i].r) {
					int cur=f[j][2];
					if (cur!=0) cur+=a[i].r;
					if (cur<=now) {
						tmp=j; now=cur;
					}
				}
			}
			if (tmp==-1) {
				flag=false;
				break;
			}
			a[i].x=f[tmp][0]+a[i].r;
			a[i].y=now;
			f[m][0]=f[tmp][0];
			f[m][1]=f[tmp][0]+2*a[i].r;
			f[m][2]=now+a[i].r;
			f[tmp][0]=f[tmp][0]+2*a[i].r;
			m++;
		}
		if (flag) out(0);
		else {
			swap(w,l);
			m=1;
			f[0][0]=0; f[0][1]=w; f[0][2]=0;
			bool flag=true;
			for (int i=0;i<n;++i) {
				int tmp=-1,now=l;
				for (int j=0;j<m;++j) {
					if (f[j][1]-f[j][0]>=2*a[i].r) {
						int cur=f[j][2];
						if (cur!=0) cur+=a[i].r;
						if (cur<=now) {
							tmp=j; now=cur;
						}
					}
				}
				if (tmp==-1) {
					flag=false;
					break;
				}
				a[i].x=f[tmp][0]+a[i].r;
				a[i].y=now;
				f[m][0]=f[tmp][0];
				f[m][1]=f[tmp][0]+2*a[i].r;
				f[m][2]=now+a[i].r;
				f[tmp][0]=f[tmp][0]+2*a[i].r;
				m++;
			}
			if (!flag) {
				cout << "Error\n";
				continue;
			}
			out(1);
		}
	}

	return 0;
}

