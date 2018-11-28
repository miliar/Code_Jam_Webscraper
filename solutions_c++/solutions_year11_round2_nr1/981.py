#include "iostream"
#include "algorithm"
#include "cstdio"
#include "cstring"
using namespace std;

char m[200][200];

int oppcnt[200];
int opp[200][200];
double wp[200], owp[200], oowp[200];
double w[200], tot[200];
double rpi[200];

int main(){
	freopen("A.out","w",stdout);
	int cs;
	int n;
	cin>>cs;
	
	for(int css=1;css<=cs;css++){
		cin>>n;
		for(int i=0;i<n;i++) scanf("%s",m[i]);

		for(int i=0;i<n;i++){
			oppcnt[i] = 0;
			w[i] = 0;
		    tot[i] = 0;
			for(int j=0;j<n;j++){
				if(m[i][j]!='.'){
					opp[i][oppcnt[i]++] = j;
					tot[i] ++;
					if(m[i][j]=='1') w[i]++;
				}
			}
			wp[i] = w[i]/tot[i];
		}
		for(int i=0;i<n;i++){
			double pp = 0;
			for(int j=0;j<oppcnt[i];j++){
				int oppid = opp[i][j];
				if(m[i][oppid]=='1'){
					if(tot[oppid]-1>0){
						pp += w[oppid]/(tot[oppid]-1);
					}
				}
				else if(m[i][oppid]=='0'){
					if(tot[oppid]-1>0){
						pp += (w[oppid]-1)/(tot[oppid]-1);
					}
				}
			}
			pp /= oppcnt[i];
			owp[i] = pp;
		}
		for(int i=0;i<n;i++){
			double pp = 0;
			for(int j=0;j<oppcnt[i];j++){
				int oppid = opp[i][j];
				pp += owp[oppid];
			}
			pp /= oppcnt[i];
			oowp[i] = pp;
		}
		for(int i=0;i<n;i++){
			rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
		}
		printf("Case #%d:\n",css);
		for(int i=0;i<n;i++){
			printf("%.12f\n",rpi[i]);
		}
	}
	return 0;
}