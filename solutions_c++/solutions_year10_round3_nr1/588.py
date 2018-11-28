#include <iostream>

using namespace std;
bool Intersecting (int a, int b, int a2, int b2);
int main()
{
	int T, N, ins;
	cin >> T;
	for (int i=0; i<T; i++)
	{
		ins = 0;
		cin >> N;
		int A[N], B[N];
		for (int j=0; j<N; j++)
			cin >> A[j] >> B[j];
		for (int p=0; p<N-1; p++)
			for(int q=p+1; q<N; q++)
			{
				if (Intersecting(A[p], B[p], A[q], B[q]))
					ins++;	
			}
		cout << "Case #" << i+1 << ": " << ins << endl;
	}
	return 0;
}

bool Intersecting (int a1, int b1, int a2, int b2)
{
	return ((a1-a2)*(b1-b2) < 0 );
}
