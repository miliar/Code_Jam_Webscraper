#include <iostream>

using namespace std;

int main(){
	int TEST; cin >> TEST;
	double l[1001], u[1001];
	int x[100], y[100];		
	for(int test=1;test<=TEST;test++){
		int W, L, U, G; cin >> W >> L >> U >> G;
		for(int i=0;i<L;i++) cin >> x[i] >> y[i];
		for(int i=0;i+1<L;i++)
			for(int j=x[i];j<=x[i+1];j++)
				l[j] = (double)(y[i+1]-y[i])/(x[i+1]-x[i])*(j-x[i])+y[i];
		for(int i=0;i<U;i++) cin >> x[i] >> y[i];
		for(int i=0;i+1<U;i++)
			for(int j=x[i];j<=x[i+1];j++)
				u[j] = (double)(y[i+1]-y[i])/(x[i+1]-x[i])*(j-x[i])+y[i];
		double S = 0.0;
		for(int i=0;i<=W;i++) u[i] = u[i]-l[i];
		for(int i=0;i<W;i++) S += 0.5*(u[i]+u[i+1]);
		printf("Case #%d:\n", test);
		for(int i=1;i<G;i++){
			double t = S*i/G;
			double cur = 0.0;
			for(int j=0;j<W;j++){
				if(cur+0.5*(u[j]+u[j+1]) > t){
					double low = 0.0, high = 1.0;
					for(int cnt=0;cnt<100;cnt++){
						double mid=(low+high)*0.5;
						double a = (u[j+1]-u[j])*mid+u[j];
						if(0.5*mid*(u[j]+a) < t-cur) low  = mid;
						else                         high = mid;
					}
					printf("%.8lf\n", j+0.5*(low+high));
					break;
				} else {
					cur += 0.5*(u[j]+u[j+1]);
				}
			}
		}
	}
}
