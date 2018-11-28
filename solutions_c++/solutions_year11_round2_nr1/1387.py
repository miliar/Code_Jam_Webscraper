#include <iostream>
#include <cstdio>

using namespace std;

struct fraction{
	int n,d;
};

int main(){
	int nCases, iCases;
	cin >> nCases;
	
	for (iCases=1; iCases<=nCases; iCases++){
		int n, i, j, c;
		cin>>n;
		
		char string[n][n+1];
		fraction WP[n];
		double OWP[n];
		double OOWP[n];
		
		for (i=0; i<n; i++){
			scanf("%s", string[i]);
			
			WP[i].n=0;
			WP[i].d=0;
			for (j=0; j<n; j++){
				if (string[i][j]!='.'){
					WP[i].d++;
					if (string[i][j]=='1'){
						WP[i].n++;
					}
				}
			}
		}
		
		for (i=0; i<n; i++){
			OWP[i]=0;
			c=0;
			
			for (j=0; j<n; j++){
				if (string[j][i]!='.'){
					c++;
				
					if (string[j][i]=='1'){
						OWP[i] += double(WP[j].n-1)/(WP[j].d-1);
					}
					else{
						OWP[i] += double(WP[j].n)/(WP[j].d-1);
					}
				}
			}
			
			OWP[i] /= c;
		}
		
		for (i=0; i<n; i++){
			OOWP[i]=0;
			c=0;
			
			for (j=0; j<n; j++){
				if (string[j][i]!='.'){
					c++;
					OOWP[i] += OWP[j];
				}
			}
			
			OOWP[i] /= c;
		}
		
		cout << "Case #" << iCases << ":" << endl;
		for (i=0; i<n; i++){
			cout.precision(8);
			cout << ( 0.25*double(WP[i].n)/WP[i].d + 0.5*OWP[i] + 0.25*OOWP[i] ) << endl;
		}
				
	}
	
	return 0;
}
