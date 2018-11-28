#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

char S[100000], T[100000];
int L, k;

int go( vector<int> &v)
{
	for(int i = 0; i < L; i += k)
		for(int j = 0; j < k; j++)
			T[i+j] = S[i+v[j]-1];

	T[L] = 0;

	int count = 1;
	for(int i = 1; T[i]; i++)
		if( T[i] != T[i-1] )
			count++;

	return count;
}

int main()
{
	int N;
	scanf("%d", &N);
	for(int n = 1; n <= N; n++)
	{
		printf("Case #%d: ", n);

		scanf("%d", &k);
		scanf("%s", S);
		L = strlen( S );

		vector<int> v(k);
		for(int i = 0; i < k; i++)
			v[i] = i+1;

		int bestV = go(v);

		while( next_permutation( v.begin(), v.end() ) )
		{
			bestV = min( bestV, go( v ) );
		}

		printf("%d\n", bestV);
	}
}