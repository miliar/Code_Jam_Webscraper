#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <math.h>

using namespace std;

class BALL{
    public:
	int i;
	double r;
	bool operator<(const BALL &b) const{
	    return r>b.r;
	}
};

class PT{ public:
    double x,y;
};

#define EPS 1E-4

double cc[10000];
BALL c[10000];
PT pt[10000];
double ans[10000][2];

const double PI = 3.141582653589793238;

int touch(PT p1,PT p2,double r1,double r2){
    double dx,dy,dd;
    dx=p1.x-p2.x;
    dy=p1.y-p2.y;
    dd=r1+r2+EPS;
    return dx*dx+dy*dy<dd*dd;
}

int check(int n){
    int i,j;
    double dx,dy,dd;
    for( i=0; i<n; i++ ){
	for( j=0; j<i; j++ ){
	    dx=ans[i][0]-ans[j][0];
	    dy=ans[i][1]-ans[j][1];
	    dd=cc[i]+cc[j];
	    if(dx*dx+dy*dy<dd*dd){
		return 0;
	    }
	}
    }
    return 1;
}

int main(){
    srand(72332);
    int tt,TT,n,i,j,k,fr,z,jc;
    double L,W,r,g,d,mind,dd;
    PT p;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ){
	scanf("%d %lf %lf",&n,&W,&L);
	for( i=0; i<n; i++ ) {
	    scanf("%lf",&c[i].r);
	    cc[i]=c[i].r;
	    c[i].r+=1;
	    c[i].i=i;
	}
	sort(c,c+n);
retry:
	pt[0].x=0;
	pt[0].y=0;
	ans[c[0].i][0]=0;
	ans[c[0].i][1]=0;
	for( i=1; i<n; i++ ){
	    r=c[i].r;
	    d=c[i-1].r+r+EPS;
	    mind = 1E30;
	    pt[i].x=-1;
	    jc=0;
	    for( j=0; j<10; ){
		jc++;
		if(jc>10000) goto retry;
		g = rand()*PI*2/RAND_MAX;
		p.x = d*cos(g)+pt[i-1].x;
		p.y = d*sin(g)+pt[i-1].y;
		if(p.x<EPS || p.y<EPS || p.x>W-EPS || p.y>L-EPS) continue;
		for( k=i-1; k>=0; k-- ){
		    if(touch(p,pt[k],r,c[k].r)) break;
		}
		if(k<0){
		    j++;
		    dd = p.x*p.x+p.y*p.y;
		    if(dd<mind){
			mind=dd;
			pt[i]=p;
		    }
		}
	    }
	    ans[c[i].i][0]=pt[i].x;
	    ans[c[i].i][1]=pt[i].y;
	}
	printf("Case #%d:",tt+1);
	for( i=0; i<n; i++ ){
	    printf(" %.1f %.1f",ans[i][0],ans[i][1]);
	}
	puts("");
	if(!check(n)){
	    fprintf(stderr,"ERROR #%d\n",tt+1);
	}
    }
    return 0;
}
