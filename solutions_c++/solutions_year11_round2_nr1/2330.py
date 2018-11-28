#include <iostream>

using namespace std;


int main(){
	int T, N, schedule[100][100];
	char temp;
	int i, j, k, t;
	double WP[100], WP2[100][100], OWP[100], OOWP[100], RPI[100], sum;
	cin >> T;
	for (i=0; i<T; i++){
		cin >> N;
		for (j=0; j<N; j++){
			for (k=0; k<N; k++){
				cin >> temp;
				if (temp!='.') 	schedule[j][k] = temp-'0';
				else schedule[j][k] = -1;
//				printf("\n%d", schedule[j][k]);
			}
		}
		
		for (j=0; j<N; j++){
			sum =0; t=0;
			for (k=0; k<N; k++){
				if (schedule[j][k]!=-1){
					sum += schedule[j][k];
					t++;
				}
			}
			WP[j] = sum/t; // winning percentage of team j
//			printf("\n%f", WP[j]);
//			system("Pause");
			for (k=0; k<N; k++){
				if (schedule[j][k]!=-1)		WP2[j][k] = (sum-schedule[j][k])/(t-1); // WP of team j without team k
//				printf("\n%f", WP2[j][k]);
			}			
		}
		for (j=0; j<N; j++){	
			sum =0; t=0;
			for (k=0; k<N; k++){
				if (schedule[j][k]!=-1){
					sum += WP2[k][j]; 
					t++;
				}
			}
			OWP[j] = sum/t; // OWP of team j
//			printf("\n%f", OWP[j]);
		}
		
		for (j=0; j<N; j++){
			sum =0; t=0;
			for (k=0; k<N; k++){
				if (schedule[j][k]!=-1)	{
					sum += OWP[k];
					t++;
				}
			}
			OOWP[j] = sum/t; // OOWP of team j
		}

		printf("Case #%d:\n", i+1);
		for (j=0; j<N; j++){			
			RPI[j] = 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j];
			cout << RPI[j]<<endl;
		}
	}	
	return 0;
}
