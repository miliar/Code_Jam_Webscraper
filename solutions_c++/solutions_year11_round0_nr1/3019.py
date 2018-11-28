#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int T,N;
const int max_n = 100;
bool R[max_n+1];
int P[max_n+1];

int Solve()
{
	int A = 1, B = 1;
	int A_ans = 0, B_ans = 0;
	int ans = 0;
	for( int i = 0; i < N; i++ ){
		if( R[i] ){
			//cout << i << ": " << A <<" " << A_ans << " "  << ans << " ";
			//ans += abs(P[i]-A)+1;
			if( abs(P[i]-A)-(ans-A_ans) > 0 ) ans += abs(P[i]-A)-(ans-A_ans)+1;
			else ans += 1;
			A_ans = ans;
			A = P[i];
			//cout << ans << endl;
		}
		else{
			//cout << i << ": " <<  B << " " << B_ans << " "<< ans << " ";
			//ans += abs(P[i]-B)+1;
			if( abs(P[i]-B)-(ans-B_ans) > 0 ) ans += abs(P[i]-B)-(ans-B_ans)+1;
			else ans += 1;
			B_ans = ans;
			B = P[i];
			//cout << ans << endl;
		}
	}
	return ans;
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	cin >> T;
	for( int i = 0; i < T; i++ ){
		cin >> N;
		for( int j = 0; j < N; j++ ){
			char c;
			cin >> c;
			if( c == 'O' ){
				R[j] = true;
			}
			else if( c == 'B' ){
				R[j] = false;
			}
			cin >> P[j];
		}
		cout << "Case #" << i+1 << ": " << Solve() << endl;
	}

	return 0;
}
