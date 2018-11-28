#include <iostream>
using namespace std;
typedef long long int lli;
#define ZER(X) memset(X,0,sizeof(X));

const int MAX = 100+1;
int M[MAX][MAX];

int parse(char c){
	switch (c){
	case '1':
		return 1;
	case '0':
		return 0;
	case '.':
		return -1;
	}
	cerr << "parse";
	return 0;
}

int win[MAX];
int played[MAX];

typedef long double ld;

ld WP[MAX];
ld OWP[MAX];
ld OOWP[MAX];

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);

	int Cases;
	cin >> Cases;
	for(int Case=1; Case <= Cases; ++Case){
		int N;
		ZER(M);
		ZER(win);
		ZER(played);
		cin >> N;
		for (int i = 0; i < N; ++i){
			for (int j = 0; j < N; ++j){
				char c;
				cin >> c;
				int r= parse(c);
				M[i][j]=r;
				if(r>=0)
					played[i]++;
				if(r>0)
					win[i]++;
			}
		}

		for (int i = 0; i < N; ++i){
			WP[i] = (ld)win[i]/played[i];
		}

		for (int i = 0; i < N; ++i){
			ld owp = 0;
			for (int j = 0; j < N; ++j){
				if (M[j][i] >= 0) {
					int w = win[j];
					int p = played[j]-1;
					if(M[j][i] > 0)
						w--;
					owp += (ld)w/p;
				}

			}
			OWP[i] = owp/played[i];
		}
		
		for (int i = 0; i < N; ++i){
			ld oowp = 0;
			for (int j = 0; j < N; ++j){
				if (M[j][i] >= 0) 
					oowp += OWP[j];
				
			}
			OOWP[i] = oowp/played[i];
		}


		cout << "Case #" << Case << ": " <<endl;
		cout.precision(10);
		for (int i = 0; i < N; ++i){
			cout << 0.25 * WP[i] + 0.50 * OWP[i] + OOWP[i]*0.25 << "\n";
		}

	}
	return 0;
}