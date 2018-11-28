#include "iostream"
#include "algorithm"
#include "cstdio"
#include "cstring"
using namespace std;

int LL, N, C;
double t;
int a[2000];
double dist[2000];

double f[2000][2000];

int main(){
	freopen("B.out","w",stdout);
	int cs;
	cin>>cs;
	for(int css=1;css<=cs;css++){
		cin>>LL>>t>>N>>C;
		for(int i=0;i<C;i++) cin>>a[i];

		for(int i=0;i<N;i++){
			dist[i] = a[i%C];
		}

		for(int i=0;i<=N;i++){
			for(int j=0;j<=LL;j++){
				f[i][j] = 1E10;
			}
		}
	
		//for(int i=0;i<=LL;i++) f[0][i] = 0;

		f[0][LL] = 0;

		for(int i=0;i<N;i++){
			for(int j=1;j<=LL;j++){
				double cst;
				if(t<=f[i][j]){
					cst = dist[i];
				}
				else{
					double kt = t-f[i][j];
					if(kt>=dist[i]/0.5){
						// no use;
						cst = dist[i]/0.5;
					}
					else{
						cst = kt+(dist[i]-kt*0.5);
					}
				}
				f[i+1][j-1] = min(f[i+1][j-1], f[i][j]+cst);
				//cout<<f[i+1][j-1]<<endl;
				f[i+1][j] = min(f[i+1][j], f[i][j]+dist[i]/0.5);
				//cout<<f[i+1][j]<<endl;
			}
			f[i+1][0] = min(f[i+1][0], f[i][0]+dist[i]/0.5);
		}

		double ans = 1E10;
		for(int i=0;i<=LL;i++){
			//cout<<":"<<f[N][i]<<endl;
			ans = min(ans,f[N][i]);
		}
		
		printf("Case #%d: %d\n", css, (int)ans);
	}
	return 0;
}