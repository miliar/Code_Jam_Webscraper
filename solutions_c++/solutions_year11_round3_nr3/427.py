#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

int N;
long long L,H;
const int maxn = 10000;
long long f[maxn+5];

bool cmp(int a, int b){
	return a<b;
}

void Solve()
{
	int ans = -1;
	for(int i = L; i <= H; i++ ){
		bool flag = true;
		for(int j = 0; j < N; j++ ){
			if( (f[j]%i) != 0 && (i%f[j]) != 0 ){
				flag = false;
				break;
			}
		}
		if( flag ){
			cout << i << endl;
			return;
		}
	}
	cout << "NO" << endl;

}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

	int T;
	cin >> T;
	for( int i = 1; i <= T; i++ ){
		cin >> N >> L >> H;
		for( int j = 0; j < N; j++ ){
			cin >> f[j];
		}

		cout << "Case #" << i << ": ";
		Solve();
	}


	return 0;
}
