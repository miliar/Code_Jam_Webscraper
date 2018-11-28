#include <string>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
int A[15];
int N;
int mx;
void rec(int i, int L, int R, int P, int S)
{
	if( i == N )
	{
		if( P == 0 || S == 0 )
			return;
		if( L == R ){
			mx = max(mx, P);
			mx = max(mx, S);
		}
		return;
	}

	rec(i + 1, L ^ A[i], R , P + A[i], S);

	rec(i + 1, L , R ^ A[i], P, S + A[i]);
}
int main()
{
	int T;
	cin >> T;
	int C = 1;
	while(T--)
	{
		mx = -1;
		cin >> N;
		for(int i = 0 ; i < N; i++)
			cin >> A[i];
		rec( 0, 0, 0, 0, 0 );
		if( mx == -1 )
			printf("Case #%d: NO\n", C );
		else
			printf("Case #%d: %d\n", C, mx );

		C++;
	}
}