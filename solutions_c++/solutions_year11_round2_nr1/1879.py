#include <iostream>

using namespace std;

int main()
{
	int i, j, k, T, N;
	int res[101][101];
	double WP[101], OWP[101], OOWP[101];
	char letra;
	char palabra[103];
	int ganados[103], jugados[103], cg, cj;
	int OW[103][103], POW[103][103];
	double porcentaje;

	cin >> T;
	for (i=1; i<=T; i++) {
		cin >> N;
		for (j=0; j<N; j++) {
			cin>>palabra;
			cj = cg = 0;

			for(k=0; k<N; k++) {
				switch(palabra[k]) {
					case '1': res[j][k] = 1; cj++; cg++; OW[j][k]=-1; POW[j][k]=-1; break;
					case '0': res[j][k] = 0; cj++;       OW[j][k]=0; POW[j][k]=-1; break;
					case '.': res[j][k] = -1;            OW[j][k]=0; POW[j][k]=0; break;
				}
			}
			porcentaje=(double)cg/cj;
			WP[j]=porcentaje;
			ganados[j]=cg;
			jugados[j]=cj;
			for(k=0; k<N; k++) {
				OW[j][k]+=cg;
				POW[j][k]+=cj;
			}
		}
		double acOWP=0;
		for (j=0; j<N; j++) {
			cj = cg = 0;
			double ac=0;
			int c=0;
			for (k=0; k<N; k++) {
				if (res[k][j] != -1) {
					ac += (double)OW[k][j]/POW[k][j] ;
					c++;
				}
			}
			OWP[j] = (double)ac/c;
			acOWP += OWP[j];
		}

		
		for (j=0; j<N; j++) {
			cj = cg = 0;
			double ac=0;
			int c=0;
			OOWP[j] = 0;
			for (k=0; k<N; k++) {
				if (res[k][j] != -1) {
					OOWP[j] += OWP[k];
					c++;
				}
			}
			OOWP[j] /= c;
		}
		
		cout <<"Case #" << i << ": " << endl;
		for (j=0; j<N; j++) {
			double RPI = 0.25 * WP[j] + 0.5 * OWP[j] + 0.25 * OOWP[j] ;
			cout << RPI << endl;
		}
	}
}