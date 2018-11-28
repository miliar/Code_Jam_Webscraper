#include <iostream>
#include <string>
#include <vector>
#define N 100
using namespace std;

int main(){
	int cases;
	cin >> cases;
	for(int i=0;i<cases;i++){
		//..............
		cout << "Case #" << i+1 << ":" << endl;
		int teams;
		char table[N][N] ;
		double wp[N];
		double owp[N];
		double oowp[N];
		int won[N];
		int matches[N];
		cin>>teams;
		for(int j=0;j<N;j++){			//clear
			for(int k=0;k<N;k++){
				table[j][k] = ' ';
			}
			wp[j]=0.0;
			owp[j]=0.0;
			oowp[j]=0.0;
			won[j]=0;
			matches[j]=0;
		}
			
		for(int j=0;j<teams;j++){		// read
			for(int k=0;k<teams;k++){
				cin >> table[j][k];
			}
		}
		for(int j=0;j<teams;j++){
			for(int k=0;k<teams;k++){
				if(table[j][k] != '.'){
					matches[j]++;
					if(table[j][k] == '1'){
						won[j]++;
					}
				}
			}
			wp[j]=(double)won[j]/(double)matches[j];
		}
		// wp 
		for(int a=0;a<teams;a++){			// a az aki mindig kimarad
			double tmpwp[N];
			for(int j=0;j<teams;j++) {tmpwp[j]=0.0;}
			for(int j=0;j<teams;j++){
				if(table[a][j]!='.'){	//jatszottunk
					if(table[a][j]=='0'){	// o nyert
						tmpwp[j]=(double)(won[j]-1)/(double)(matches[j]-1);
					}else{
						tmpwp[j]=(double)won[j]/(double)(matches[j]-1);
					}
				}else{
					tmpwp[j]=wp[j];
				}
			}
			
			int count=0;
			for(int j=0;j<teams;j++){
				if(table[a][j]!='.'){
					count++;
					owp[a]+=tmpwp[j];
				}
			}
			owp[a]/=(double)count;
		}
		// oowp
		for(int j=0;j<teams;j++){
			for(int k=0;k<teams;k++){
				if(table[j][k]!='.')oowp[j]+=owp[k];
			}
			oowp[j]/=(double)matches[j];
		}
		for(int j=0;j<teams;j++){
			//cout<<j+1<<". wp: "<<wp[j]<<"\towp: "<<owp[j]<<"\toowp: "<<oowp[j]<<endl;
			cout<<0.25*wp[j] + 0.5*owp[j] + 0.25*oowp[j]<<endl;
		}
		
	}
	return 0;
}