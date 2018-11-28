#include<iostream>
using namespace std;

char ar[100][100];
bool bol[100][100];
int t,T,N,K;
char crnt;
bool rwin,bwin;

int main() {
	cin>>T;
	for(t=1;t<=T;t++) {
		cin>>N>>K;
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) cin>>ar[i][j];
		}
		for(int i=0;i<N;i++) {
			int j=N-1;
			int k=N-1;
			while(k>=0) {
				if(ar[i][k]!='.') {
					ar[i][j]=ar[i][k];
					if(j!=k) ar[i][k]='.';
					j--;
				}
				k--;
			}
		}
		rwin=false; bwin=false;
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				if(ar[i][j]=='.') continue;
				crnt=ar[i][j];
				for(int k=0;k<K;k++) {
					if(j+k>=N) break;
					if(ar[i][j+k]!=crnt) break;
					if(k==K-1) {
						if(crnt=='R') rwin=true;
						else if(crnt=='B') bwin=true;
					}
				}
				for(int k=0;k<K;k++) {
					if(i+k>=N) break;
					if(ar[i+k][j]!=crnt) break;
					if(k==K-1) {
						if(crnt=='R') rwin=true;
						else if(crnt=='B') bwin=true;
					}
				}
				for(int k=0;k<K;k++) {
					if(i+k>=N||j+k>=N) break;
					if(ar[i+k][j+k]!=crnt) break;
					if(k==K-1) {
						if(crnt=='R') rwin=true;
						else if(crnt=='B') bwin=true;
					}
				}
				for(int k=0;k<K;k++) {
					if(i-k<0||j+k>=N) break;
					if(ar[i-k][j+k]!=crnt) break;
					if(k==K-1) {
						if(crnt=='R') rwin=true;
						else if(crnt=='B') bwin=true;
					}
				}
			}
		}
		cout<<"Case #"<<t<<": ";
		if(bwin&&rwin) cout<<"Both";
		else if(bwin) cout<<"Blue";
		else if(rwin) cout<<"Red";
		else cout<<"Neither";
		cout<<endl;
	}
}
