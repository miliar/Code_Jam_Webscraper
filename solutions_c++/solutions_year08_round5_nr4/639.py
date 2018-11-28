#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
const int c=100;
const int base=10007;
struct point {
	int x,y;
	point (int a=0, int b=0) {
		x=a;
		y=b;
	}
};
bool operator < (const point &a, const point &b) {
	return a.x<b.x || a.x==b.x && a.y<b.y;
}
int h,w,n,r;
int r1,r2,ans;
point a[c];
point b[c];
int p[base];
int f(int i) {
	int k=0;
	while (i>0) {
		k+=i%2;
		i/=2;
	}
	return k;
}
int get(int h, int w) {
	if ((h+w-2)%3) return 0;
	int k=(h+w-2)/3;
	int q1,q2;
	q1=q2=0;
	if (h<k+1 || w<k+1 || h>2*k+1 || w>2*k+1) return 0;
	int x=h-1-k;
	int y=w-1-k;
	int r=1;
	int j;
	for (j=x+1; j<=x+y; ++j) {
		if (j%base==0) ++q1; else r=(r*(j%base))%base;
	}
	for (j=1; j<=y; ++j) {
		if (j%base==0) ++q2; else r=(r*(p[j%base]))%base;
	}
	if (q1>q2) return 0; else return r;
}
int go(int i) {
	int j=0;
	int k=2;
	if (h==1 && w==1) return 1;
	b[0]=point(1,1);
	b[1]=point(h,w);
	while (i>0) {
		if (i%2) {
			b[k]=a[j];
			++k;
		}
		++j;
		i/=2;
	}
	sort(&b[0],&b[k]);
	for (j=0; j<k-1; ++j) if (b[j].x>=b[j+1].x || b[j].y>=b[j+1].y) return 0;
	int r=1;
	for (j=0; j<k-1; ++j) r=(r*get(b[j+1].x-b[j].x+1,b[j+1].y-b[j].y+1))%base;
	return r;
}	
int main() {
	int ii,i,j;
	for (i=1; i<base; ++i)
		for (j=1; j<base; ++j) if ((i*j)%base==1) p[i]=j;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&n);
	for (ii=1; ii<=n; ++ii) {
		scanf("%d%d%d",&h,&w,&r);
		for (i=0; i<r; ++i) scanf("%d%d",&a[i].x,&a[i].y);
		r1=0;
		r2=0;
		for (i=0; i<(1<<r); ++i) if (f(i)%2==0) r1=(r1+go(i))%base; else r2=(r2+go(i))%base;
		ans=(r1+base-r2)%base;
		printf("Case #%d: %d\n",ii,ans);
   	}
   	return 0;
}
                          	