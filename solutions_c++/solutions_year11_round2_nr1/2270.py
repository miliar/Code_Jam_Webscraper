#include <iostream>
#include <cmath>
using namespace std;

int main ()
{
	int T,N;
	cin >> T;
	for(int i = 1; i<=T;i++){
		//Get input
		cin >> N;
		int table[N][N];
		char temp;
		for(int j = 0;j<N;j++){
			for(int k = 0; k<N;k++){
				cin >> temp;
				table[j][k] = (int)temp - 48;
			}
		}
		//CaluclateRPI
		
		// calcukate WP
		double WP[N];
		double counter[N];
		for(int j = 0;j<N;j++){
			WP[j] = 0;
			counter[j] = 0;
			for(int k = 0; k<N;k++){
				if(table[j][k] != -2){
					counter[j] += 1;
					WP[j] +=table[j][k];
				}
			}
			WP[j] = WP[j]/counter[j];
		}
		// calculate OWP
		double OWP[N];
		double tempOWP[N];
		for(int j = 0; j<N; j++){
			for (int k = 0; k<N; k++){
				tempOWP[k] = 0;
				if (k != j) {
					if  (table[k][j] != -2){
						tempOWP[k] = (WP[k] - table[k][j]/counter[k])*counter[k]/(counter[k]-1);
					}else{
						tempOWP[k] = 0;
					}
				}
				//cout << tempOWP[k] <<" " <<table[k][j]/counter[k]<<endl;
			}
			//cout <<endl;
			OWP[j] = 0;
			for(int k = 0; k<N;k++)
				OWP[j] += tempOWP[k];
			OWP[j] = OWP[j]/counter[j];
		}
		
		// calculate OOWP
		double OOWP[N];
		for(int j = 0; j<N; j++){
			OOWP[j] = 0;
			for(int k = 0; k<N; k++){
				if ((j!=k) && (table[j][k]!=-2)){
					OOWP[j] += OWP[k];
					//cout << OWP[k];
				}
			}
			//cout<<endl;
			OOWP[j] = OOWP[j]/counter[j];
			//cout << counter[j]<<endl;
		}
		
		//Output
		cout <<"Case #"<<i<<":"<<endl;
		for(int j = 0;j<N;j++){
			cout << 0.25*WP[j]+0.5*OWP[j]+0.25*OOWP[j]<<endl;
			//cout << WP[j] <<" "<<OWP[j]<<" "<<OOWP[j]<<endl;
		}
	}
}
