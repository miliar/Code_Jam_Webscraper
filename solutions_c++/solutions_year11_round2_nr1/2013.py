#include <iostream>

using namespace std;

int main(int argc, char ** argv){

int T, N;

cin >> T;

int i,j,k;
char M[100][100];

double RPI[100];

int w[100],g[100];
double owp[100];
double oowp;


for(k=0;k<T;k++){
cin >> N;
for (i=0;i<N;i++)
	for(j=0;j<N;j++){
		cin >> M[i][j];
		//cout << M[i][j];
		}

cout << "Case #" << k+1 <<":" << endl;
for (i=0;i<N;i++){
	w[i] = 0;
	g[i] = 0;
	RPI[i] = 0;
	for(j=0;j<N;j++)
		if(M[i][j] != '.'){
			g[i]++;
			if (M[i][j] == '1')
				w[i]++;

		}
	//cout << w[i] << " " << g[i] << endl;
	RPI[i] = 0.25 *  ((double)w[i]) / g[i];
	//cout << RPI[i] << endl;	
	}

for (i=0;i<N;i++){
	owp[i] = 0;
	for(j=0;j<N;j++){
		if(M[i][j] != '.'){
			if(M[i][j] == '0'){
				owp[i] += ((double)(w[j]-1)) /  (g[j]-1); 
				//cout <<  w[j]-1 << " "  <<g[j]-1 << endl;
				}
			else {
				owp[i] += ((double)(w[j])) /  (g[j]-1); 
				//cout <<  w[j] << " " <<  g[j]-1 << endl;
				} 

		}
			
	}
	//cout<< endl;
	owp[i] = owp[i]/g[i];
	//cout << owp[i] << endl; 
	RPI[i] += 0.50 *  owp[i];
	//cout << RPI[i] << endl ;
}
	
for (i=0;i<N;i++){
	oowp = 0;
	for(j=0;j<N;j++){
		if(M[i][j] != '.'){
		oowp += owp[j]; 
		
		}
	}
	//cout << oowp/g[i]<< endl;
	RPI[i] += 0.25 * (oowp/g[i]);
 
	cout << RPI[i] << endl;
	}	
}


return 0;
}
