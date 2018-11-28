#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int N;
const int max_n = 16;
int C[max_n];
bool hav[max_n];
int ans = 0;

void Solve(int u)
{
	if( u == N ){
		int sum1 = 0, sum2 = 0;
		int _sum1 = 0, _sum2 = 0;
		for( int i = 0; i < N; i++ ){
			if( hav[i] ){
				sum1 += C[i];
				_sum1 ^= C[i];
			}
			else{
				sum2 += C[i];
				_sum2 ^= C[i];
			}
		}
		if( _sum1 == _sum2 && _sum1 != 0 ){
			if( sum1 > ans ) ans = sum1;
			if( sum2 > ans ) ans = sum2;
		}
		return;
	}
	hav[u] = true;
	Solve(u+1);
	hav[u] = false;
	Solve(u+1);
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int T;
	cin >> T;
	for( int i = 0; i < T; i++ ){
		cin >> N;
		for( int j = 0; j < N; j++ ){
			cin >> C[j];
		}
		ans = 0;
		Solve(0);
		cout << "Case #" << i+1 << ": ";
		if( ans == 0 ){
			cout << "NO" << endl;
		}
		else{
			cout << ans << endl;
		}
	}

	return 0;
}
