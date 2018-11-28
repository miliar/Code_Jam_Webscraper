#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
typedef vector<int> vi;
typedef long long int64;

int main() {
	int T,N;
	string his;
	char c;
	cin>>T;
	cout.precision(12);
	for(int t=1;t<=T;t++){
		cin>>N;
		int face[N][N];
		double x;
		int64 wp[N][2];
		double owp[N][2];
		double oowp[N][2];
		memset(wp,0,sizeof(int64)*N*2);
		memset(owp,0,sizeof(int64)*N*2);
		memset(oowp,0,sizeof(double)*N*2);
		cout<<"Case #"<<t<<":"<<endl;
		for(int n=0; n<N; n++ ){			
			for(int m=0; m<N; m++ ){			
				cin>>c;
				switch(c){
					case '1':
						wp[n][0]++;
						wp[n][1]++;
						face[n][m]=2;
						break;
					case '0':
						wp[n][1]++;
						face[n][m]=1;
						break;
					case '.':
						face[n][m]=0;
						break;
				}				
			}					
		}
		for(int n=0; n<N; n++ ){
			for(int m=0; m<N; m++ ){
				if(face[n][m]==1){					
					owp[n][0]+=((double)wp[m][0]-1)/(wp[m][1]-1);
					owp[n][1]+=1;
					
				}
				else if(face[n][m]==2){					
					owp[n][0]+=((double)wp[m][0])/(wp[m][1]-1);
					owp[n][1]+=1;
					
				}
			}
		}
		for(int n=0; n<N; n++ ){
			for(int m=0; m<N; m++ ){
				if(face[n][m]>0){
					oowp[n][0]+=((double)(owp[m][0]))/owp[m][1];
					oowp[n][1]+=1;
				}				
			}
		}
		for(int n=0; n<N; n++ ){
			x= 0.25 * (((double)(wp[n][0]))/wp[n][1]) + 0.50 * (((double)(owp[n][0]))/owp[n][1]) +  0.25 * (oowp[n][0]/oowp[n][1]);
			cout << x << endl;
		}
	}
	return 0;
}
