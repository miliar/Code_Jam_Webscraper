#include<cstdio>

int C,D;
int P[202],V[202];

void solve(){
	double sum = 0;
	scanf("%d%d",&C,&D);
	for( int i = 1 ; i <= C ; ++i ){
		scanf("%d%d",&P[i],&V[i]);
		sum += V[i];
	}
	
	double low = 0 , high = sum * D;
	while( high - low > 1e-10 ){
		double mid = (high + low) / 2;
		int l = 1 , r;
		bool ok = true;
		double lmost = -1e30;
		while( l <= C ){
			r = l;
			int num = V[l];
			double delta = 0;
			while( r < C ){
				if( P[r+1] - P[r] < 2*mid ){
					r++;
					num += V[r];
				}else break;
			}
			//printf("%lf %lf\n",P[r],P[l]);
			double range = (P[r] - P[l]) + 2*mid;
			//printf("%d %d : %d %lf\n",l,r,num,range);
			if( (num-1) * D > range ){
				ok = false;
				break;
			}
			if( lmost + num*D > P[r] + mid ){
				ok = false;
				break;
			}
			if( lmost < P[l] - mid ){
				lmost = P[l] - mid + (num-1)*D;
			}else lmost = lmost + (num-1)*D;
			l = r+1;
		}
		//printf("%d\n",ok);
		if( ok ){
			high = mid;
		}else low = mid;
	}
	printf("%.10lf\n",(high+low)/2);
}
int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	for( int i = 1 ; i <= T; ++i ){
		printf("Case #%d: ",i);
		solve();
	}
}