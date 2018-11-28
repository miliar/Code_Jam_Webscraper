#include <cstdio>
#include <vector>
#include <utility>
#include <iostream>
#include <string>

using namespace std;
const string ON("ON");
const string OFF("OFF");

void test( int N, int K, int number )
{
	bool state[N];
	for( int i = 0; i < N; ++i )
		state[i] = false;

	for( int i = 0; i < K; ++i )
	{
		int j = 0;
		while( state[j] && j < N )
			++j;
		for( ; j >= 0; --j )
			state[j] = !state[j];
	}

	int j = 0;
	while( state[j] && j < N )
		++j;

	cout << "Case #" << number << ": " << (j==N ? ON : OFF) << "\n";
}

int main()
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.txt", "wt", stdout );

	int T;
	scanf("%d", &T);

	for( int i = 0; i < T; ++i )
	{
		int N, K;
		scanf( "%d%d", &N, &K );
		test(N, K, i + 1);
	}
}
