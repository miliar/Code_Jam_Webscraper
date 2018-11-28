#include<iostream>
using namespace std;

int T, win[128], lose[128], match[128][128], N, tempN;
double WP[128], OWP[128], OOWP[128], tempWP;
char ch;

int main() {
	cin>>T;
	for(int tc=1;tc<=T;tc++) {
		cin>>N;
		for(int i=0;i<N;i++) {
			win[i]=0; lose[i]=0;
			WP[i]=0.00; OWP[i]=0.00; OOWP[i]=0.00;
			for(int j=0;j<N;j++) match[i][j]=-1;
		}
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				cin>>ch;
				if(ch=='0') {
					lose[i]++;
					match[i][j]=0;
				}
				else if(ch=='1') {
					win[i]++;
					match[i][j]=1;
				}
			}
		}
		//count WP
		for(int i=0;i<N;i++) {
			WP[i]=(1.00*win[i])/(1.00*(win[i]+lose[i]));
		}
		//count OWP
		for(int i=0;i<N;i++) {
			OWP[i]=0.00;
			tempN=0;
			for(int j=0;j<N;j++) {
				if(i==j) continue;
				if(match[i][j]==-1) continue;
				tempN++;
				tempWP=0.00;
				if(match[j][i]==1) tempWP=(1.00*(win[j]-1))/(1.00*(win[j]+lose[j]-1));
				else if(match[j][i]==0) tempWP=(1.00*win[j])/(1.00*(win[j]+lose[j]-1));
				OWP[i]+=tempWP;
			}
			OWP[i]/=(1.00*tempN);
		}
		//count OOWP
		for(int i=0;i<N;i++) {
			OOWP[i]=0.00;
			tempN=0;
			for(int j=0;j<N;j++) {
				if(i==j) continue;
				if(match[i][j]==-1) continue;
				tempN++;
				OOWP[i]+=OWP[j];
			}
			OOWP[i]/=(1.00*tempN);
		}
		cout<<"Case #"<<tc<<":"<<endl;
		for(int i=0;i<N;i++) {
			//if(i==0) {
				//cout<<"WP, OWP, OOWP: "<<WP[i]<<" "<<OWP[i]<<" "<<OOWP[i]<<endl;
			//}
			printf("%.9lf\n",(0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]));
		}
	}
}
