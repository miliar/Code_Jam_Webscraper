#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int n;
char standing[100][100];
int allGame[100];
double WP[100][100];
double OWP[100];
double OOWP[100];

int main(){
	int tc;
	int i,j,k,l;
	double tmp;
	double RPI;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> tc;
	for (i=0; i<tc; i++){
		cin >> n;
		for (j=0; j<n; j++)
			cin >> standing[j];

		memset(allGame, 0, sizeof allGame);
		memset(WP, 0, sizeof WP);
		memset(OWP, 0, sizeof OWP);
		memset(OOWP, 0, sizeof OOWP);

		for (j=0; j<n; j++){
			tmp = 0;
			for (k=0; k<n; k++)
				if (standing[j][k]!='.')
					allGame[j]++;
		}

		for (j=0; j<n; j++)
			for (k=0; k<n; k++){
				tmp = 0;
				for (l=0; l<n; l++)
					if ((standing[j][l]=='1')&&(l!=k))
						tmp++;
				if (j==k)
					WP[j][k] = tmp/allGame[j];
				else
					WP[j][k] = tmp/(allGame[j]-1);
			}


		for (j=0; j<n; j++){
			tmp = 0;
			for (k=0; k<n; k++)
				if (standing[j][k]!='.')
					tmp+=WP[k][j];
			OWP[j] = tmp/allGame[j];
		}

		for (j=0; j<n; j++){
			tmp = 0;
			for (k=0; k<n; k++)
				if (standing[j][k]!='.')
					tmp+=OWP[k];
			OOWP[j] = tmp/allGame[j];
		}

		printf("Case #%d:\n", i+1);
		for (j=0; j<n; j++){
			 RPI = 0.25 * WP[j][j] + 0.50 * OWP[j] + 0.25 * OOWP[j];
			 cout << RPI << endl;
		}
	}
}