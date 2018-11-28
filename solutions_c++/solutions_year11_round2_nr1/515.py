#include <iostream>

using namespace std;

double ccount[100];
double win[100];
double WP[100];
double OWP[100];
double OOWP[100];
int data[100][100];

int main (int argc, char const *argv[])
{
	int T, N;
	
	cin>>T;
	for(int t = 0; t< T; t++){
		cout<<"Case #"<<t+1<<": "<<endl;
		cin>>N;
		memset(data, 0, sizeof(int)*100*100);
		memset(WP, 0, sizeof(int)*100);
		memset(OWP, 0, sizeof(int)*100);
		memset(OOWP, 0, sizeof(int)*100);
		memset(ccount, 0, sizeof(int)*100);
		memset(win, 0, sizeof(int)*100);
		for(int i=0; i<N; i++){
			int w = 0,c = 0;
			char tmp;
			for(int j=0; j<N; j++){
				cin>>tmp;
				if(tmp != '.'){
					data[i][j] = tmp-'0';
					c++;
					w += data[i][j];
				}else{
					data[i][j] = -1;
				}
			}
			
			ccount[i] = c;
			win[i] = w;
			if(c != 0){
				WP[i] = (win[i])/ccount[i];
//				cout<<i<<" "<<WP[i]<<endl;
			}
		}	
		for(int i=0; i<N; i++){
			double avg = 0;
			for(int j = 0; j<N; j++){
				if(data[i][j] != -1){
					avg += (win[j] - data[j][i])/(ccount[j]-1);
				}
			}
			OWP[i] = avg/ccount[i];
//			cout<<i<<" "<<OWP[i]<<endl;
		}	
		
		for(int i=0; i<N; i++){
			double avg = 0;
			for(int j = 0; j<N; j++){
				if(data[i][j] != -1){
					avg += OWP[j];
				}
			}
			OOWP[i] = avg/ccount[i];
//			cout<<i<<" "<<OOWP[i]<<endl;
			cout<<0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]<<endl;
		}
	}
	return 0;
}