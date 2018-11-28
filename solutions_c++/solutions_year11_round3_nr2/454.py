#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

long long L,t,N,C;
const int maxn = 1000;
int a[maxn+5];
int l[maxn+5];
int build[maxn+5];
int ans;
bool hav[maxn+5];

bool cmp(int a, int b){
	return a<b;
}

void Compute(int n)
{
	/*
		for( int i = 0; i < N; i++ ){
			if( hav[i] ) cout << " have " <<  i << " ";
		}
		cout << endl;
		*/
	int tmp = 0;
	for( int i = 0; i < N; i++ ){
		if( hav[i] ){
			if( tmp >= t ){
				tmp += l[i];
			}
			else if( t < l[i]/0.5+tmp ){
				int _t = t-tmp;
				tmp += _t;
				int len = l[i]-_t*0.5;
				tmp += len;
			}
			else tmp += l[i]/0.5;
		}
		else{
			tmp += l[i]/0.5;
		}
	}
	if( tmp < ans ){
		ans = tmp;
		/*
		cout << "ans = " << ans;
		for( int i = 0; i < N; i++ ){
			if( hav[i] ) cout << " have " <<  i << " ";
		}
		cout << endl;
		*/
	}

	if( n < L ){
		for( int i = 0; i < N; i++ ){
			if( !hav[i] ){
				hav[i] = true;
				Compute(n+1);
				hav[i] = false;
			}
		}
	}
}

void Solve()
{
	ans = 99999999;
	memset(hav, 0, sizeof(hav));
	Compute(0);
	cout << ans << endl;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	int T;
	cin >> T;
	for( int i = 1; i <= T; i++ ){
		cin >> L >> t >> N >> C;
		for( int j = 0; j < C; j++ ){
			cin >> a[j];
		}
		for( int j = 0; j < N; j++ ){
			l[j] = a[j%C];
		}

		cout << "Case #" << i << ": ";
		Solve();
	}


	return 0;
}
