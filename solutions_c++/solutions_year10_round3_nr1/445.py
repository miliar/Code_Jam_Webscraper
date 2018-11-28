#include <iostream>

using namespace std;

int main()
{

	int T, t, N, n, A[1000], B[1000], y;
	int i, j;
	cin >> T;
	for(t=1; t<=T; ++t)
	{
		cout << "Case #" << t <<": ";
		cin >> N;
		for(n=0; n<N; ++n)
			cin >> A[n] >> B[n];
		y=0;
		for(i=0; i<N; ++i)
		{
			for(j=i+1; j<N; ++j)
				if( (A[i]<A[j] && B[i]>B[j])
					|| (A[i]>A[j] && B[i]<B[j]) )
					++y;
		}
		cout << y << endl;
	}
}

