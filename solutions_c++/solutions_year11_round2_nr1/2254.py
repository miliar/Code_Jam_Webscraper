#include <iostream>

using namespace std;
typedef long long llong;

int n;
int g[1000][1000];
int w[1000];
int gp[1000];
double owp[1000];

int main(){

	int NN;cin>>NN;
	for(int MM=1;MM<=NN;MM++){
		cin >>n;
		memset(g,0,sizeof(g));
		for(int i=0;i<n;i++){
			char t[1001];
			cin>>t;
			for(int j=0;j<n;j++)
				if (t[j]=='.')
					g[i][j]=0;
				else
					g[i][j]=t[j]=='0'?-1:1;
		}
		for(int i=0;i<n;i++){
			w[i]=0;
			gp[i]=0;
			for(int j=0;j<n;j++)
				if(g[i][j]){
					gp[i]++;
					w[i]+=(g[i][j]==1);
				}
		}
		cout<<"Case #"<<MM<<":"<<endl;
		for(int i=0;i<n;i++){
			double x=0;
			for(int j=0;j<n;j++)
				if(g[i][j]){
					x += (double)(w[j]-(g[j][i]==1 ? 1 : 0))/(gp[j]-1); 
				}
			owp[i]=x/gp[i];
		}
		for(int i=0;i<n;i++){
			double x=0;
			for(int j=0;j<n;j++)
				if(g[i][j]){
					x += owp[j];
				}
			double rpi= 0.25 * ((double)w[i]/gp[i]) + 0.5 * (owp[i]) + 0.25 * (x/gp[i]);
			//printf("%lf\n", rpi)
			cout.precision(12);
			cout<<rpi<<endl;
		}
	}
	return 0;
}