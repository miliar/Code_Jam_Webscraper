#include <iostream>
#include <iomanip>

using namespace std;

const int MaxN= 100 + 5;
int n;
char g[MaxN][MaxN];
long double wp[MaxN], owp[MaxN], oowp[MaxN];

long double findOWP(int r, int c){
	long double res= 0, sum= 0;
	for (int i=0 ; i<n ; i++){
		if (i==c)
			continue;
		if (g[r][i]!='.')
			sum++;
		if (g[r][i]=='1')
			res++;
	}
	return res/sum;
}

int main(){
	cout << fixed << setprecision(10);
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		cout << "Case #" << t << ":\n";
		cin >> n;
		for (int i=0 ; i<n ; i++)
			for (int j=0 ; j<n ; j++)
				scanf(" %c", &g[i][j]);
		for (int i=0 ; i<n ; i++){
			long double WP= 0, sum= 0;
			for (int j=0 ; j<n ; j++){
				if (g[i][j]=='1')
					WP++;
				if (g[i][j]!='.')
					sum++;
			}
			WP/= sum;
			wp[i]= WP;
		}
		for (int i=0 ; i<n ; i++){
			long double OWP= 0, sum= 0;
			for (int j=0 ; j<n ; j++)
				if (g[i][j]!='.'){
					OWP+= findOWP(j, i);
					sum++;
				}
			OWP/= sum;
			owp[i]= OWP;
		}
		for (int i=0 ; i<n ; i++){
			long double OOWP= 0, sum= 0;
			for (int j=0 ; j<n ; j++)
				if (g[i][j]!='.'){
					OOWP+= owp[j];
					sum++;
				}
			OOWP/= sum;
			oowp[i]= OOWP;
		}
		for (int i=0 ; i<n ; i++)
			cout << (wp[i]/2 + owp[i] + oowp[i]/2)/2 << endl;
	}
	return 0;
}