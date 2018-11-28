#include<iostream>
using namespace std;
char sc[103][103];
double wp[103];
double count[103];
double wpt[103][103];
double owp[103];
double oowp[103];
int N,T;

int main(){
	cin >> T;
	for(int t=1;t<=T;t++){
		cin >> N;
		for(int i=1;i<=N;i++){
			count[i]=0;
			for(int j=1;j<=N;j++){
				cin >> sc[i][j];
				count[i] += sc[i][j]=='0' || sc[i][j]=='1';
			}
		}
		
		for(int i=1;i<=N;i++){
			int cnt=0;
			for(int j=1;j<=N;j++)
				cnt+=sc[i][j]=='1';
			wp[i]=cnt/count[i];
		}

		for(int i=1;i<=N;i++){
			owp[i]=0;
			for(int j=1;j<=N;j++)
				if(sc[i][j]!='.'){
					int cnt1=0;
					double cnt2=0;
					for(int k=1;k<=N;k++)
					{
						cnt1+=sc[j][k]=='1' && k!=i;
						cnt2+=(sc[j][k]=='1' || sc[j][k]=='0') && k!=i;
					}
					owp[i]+= cnt1/cnt2;
				}
			owp[i]/=count[i];
		}

		for(int i=1;i<=N;i++){
			oowp[i]=0;
			for(int j=1;j<=N;j++)
				if(sc[i][j]!='.')
					oowp[i]+=owp[j];
			oowp[i]/=count[i];
		}

		cout << "Case #" << t<<":"<<endl;
		for(int i=1;i<=N;i++)
			cout << 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i] << endl;

	}
}
