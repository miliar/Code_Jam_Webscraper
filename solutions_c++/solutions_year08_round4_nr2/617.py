#include <cstdio>
int C;
int N,M,A;
struct point {
	long long int x,y;
	point operator-(const point& a) {
		point la;
		la.x=x-a.x;
		la.y=y-a.y;
		return la;
	}
};

long long cross(const point& a, const point& b) {
	long long ans=(a.x*b.y-a.y*b.x);
	if(ans<0)
		return ans*-1;
	return ans;
}
int main(void) {
	scanf("%d",&C);
	for(int T=1;T<=C;T++) {
		printf("Case #%d:",T);
		scanf("%d %d %d",&N,&M,&A);
		bool foi=false;

		point p0,p1,p2;
		p0.y = p1.x = 0;

        for(p0.x = 0; p0.x <= N; p0.x++) {
            for(p1.y = 0; p1.y <= M; p1.y++) {
				for(p2.x=0;p2.x<=N;p2.x++) {
					for(p2.y=0;p2.y<=M;p2.y++) {
						if(p2.x ==0 and p2.y==p1.y)
							continue;
						if(p2.y ==0 and p2.x==p0.x)
							continue;
						if(cross(p2-p1,p0-p1) == (long long)(A)) {
							foi =true;
							goto final;
						}
					}
				}
            }
        }

final:
		if(foi)
			printf(" %lld %lld %lld %lld %lld %lld\n",p0.x,p0.y,p1.x,p1.y,p2.x,p2.y);
		else
			printf(" IMPOSSIBLE\n");
	}

	return 0;
}
