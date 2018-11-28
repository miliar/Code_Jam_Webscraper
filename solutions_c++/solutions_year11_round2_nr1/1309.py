#include <iostream>
#include <cstdio>

using namespace std;

const int maxn = 100;
char G[maxn+5][maxn+5];
int T,N;
double w[maxn+5];
double l[maxn+5];
double wp[maxn+5];
double owp[maxn+5];
double oowp[maxn+5];

void Solve()
{
	memset(w, 0, sizeof(w));
	memset(l, 0, sizeof(l));
	memset(wp, 0, sizeof(wp));
	memset(owp, 0, sizeof(owp));
	memset(oowp, 0, sizeof(oowp));
	for( int i = 0; i < N; i++ ){
		for( int j = 0; j < N; j++ ){
			if( G[i][j] == '1' ) w[i]++;
			else if( G[i][j] == '0' ) l[i]++;
		}
	}
	for( int i = 0; i < N; i++ ){
		wp[i] = w[i]/(w[i]+l[i]);
	}
	for( int i = 0; i < N; i++ ){
		for( int j = 0; j < N; j++ ){
			if( G[i][j] == '1' ){
				owp[i] += w[j]/(w[j]+l[j]-1);
			}
			else if( G[i][j] == '0' ){
				owp[i] += (w[j]-1)/(w[j]+l[j]-1);
			}
		}
		owp[i] /= (w[i]+l[i]);
	}
	for( int i = 0; i < N; i++ ){
		for( int j = 0; j < N; j++ ){
			if( G[i][j] != '.' )
				oowp[i] += owp[j];
		}
		oowp[i] /= (w[i]+l[i]);
	}
	for( int i = 0; i < N; i++ ){
		//cout << wp[i] << " " << owp[i] << " " << oowp[i] << endl;
		printf("%.12f\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}

}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	cin >> T;

	for( int i = 1; i <= T; i++ ){
		cin >> N;
		for( int j = 0; j < N; j++ ){
			cin >> G[j];
		}
		printf("Case #%d:\n",i);
		Solve();
	}

	return 0;
}
