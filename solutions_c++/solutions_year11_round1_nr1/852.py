#include <iostream>
#include <cstdio>
#include <cassert>
#include <algorithm>

using namespace std;

unsigned long long T, N, Pd, Pg;
int dp[105];

void Resolve()
{
	dp[0] = dp[100] = 1;
	for( int k = 1; k < 100; k++ ){
		int num = 1;
		while(1){
			assert( num > 0 );
			bool flag = false;
			for( int j = 1; j <= num; j++ ){
				for( int i = 0; i <= j; i++ ){
					if( i*100 == k*j ){
						dp[k] = j;
						flag = true;
						break;
					}
				}
				if( flag ){
					break;
				}
			}
			if( flag ){
				break;
			}
			num++;
		}
		//cout << dp[k] << endl;
	}
}

bool Solve()
{
	if( Pd != 100 && Pg == 100 ){
		return false;
	}
	if( Pd != 0 && Pg == 0 ){
		return false;
	}

	/*
	bool flag = false;
	for( int j = 1; j <= N; j++ ){
		for( int i = 0; i <= j; i++ ){
			if( i*100 == Pd*j ){
				flag = true;
				break;
			}
		}
		if( flag ){
			break;
		}
	}

	if( flag == false ){
		return false;
	}
	*/
	if( N >= dp[Pd] ){
		return true;
	}
	else{
		return false;
	}

	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	cin >> T;

	Resolve();

	for( int i = 1; i <= T; i++ ){
		cin >> N >> Pd >> Pg;
		if( Solve() ){
			cout << "Case #" << i << ": Possible" << endl;
		}
		else{
			cout << "Case #" << i << ": Broken" << endl;
		}
	}


	return 0;
}
