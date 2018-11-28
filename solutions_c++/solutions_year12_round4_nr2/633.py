#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;

double r[1005];
double x[1005], y[1005];
int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	
	int t, cas=0;
	scanf("%d",&t);
	srand(13);
	while(t--){
		int n;
		double w,l;
		scanf("%d%lf%lf",&n,&w,&l);
		for(int i=0;i<n;i++){
			scanf("%lf",&r[i]);
		}
		
		for(int i=0;i<n;i++){
			double tx, ty;
			while(true){
				tx = (rand()*1LL*rand()*rand()*rand()%((long long)w*100))*0.01;
				ty = (rand()*1LL*rand()*rand()*rand()%((long long)l*100))*0.01;
				//printf("= %f %f\n", tx, ty);
				bool flag = true;
				int cnt=0;
				for(int j=0;j<i;j++){
					cnt++;
					if((tx-x[j])*(tx-x[j])+(ty-y[j])*(ty-y[j])<(r[i]+r[j])*(r[i]+r[j])){
						//printf("%lf, %lf\n", (tx-x[j])*(tx-x[j])+(ty-y[j])*(ty-y[j]), (r[i]+r[j])*(r[i]+r[j]));
						flag = false;
						break;
					}
				}
				//printf("%d\n", cnt);
				//getchar();
				if(flag) break;
			}
			x[i] = tx;
			y[i] = ty;
		}
		
		printf("Case #%d:",++cas);
		for(int i=0;i<n;i++){
			printf(" %f %f", x[i], y[i]);
		}
		puts("");
	}
}