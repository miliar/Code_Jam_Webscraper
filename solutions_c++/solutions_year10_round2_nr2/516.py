#include <iostream>
#include <vector>
using namespace std;

class Problem
{
    int N, K, B, T;
    vector<int> X, V;
public:
	void ReadData()
	{
	    cin >> N >> K >> B >> T;
	    X.resize(N);  for (int i=0; i<N; ++i)  cin >> X[i];
	    V.resize(N);  for (int i=0; i<N; ++i)  cin >> V[i];
	}
	void Solve(int nCase)
	{
		ReadData();

		int swaps=0, pass=0;
		for (int i=N; i-->0 && K; )
		    if (X[i]+T*V[i] < B)  ++pass;
		    else  { --K;  swaps += pass; }

		cout << "Case #" << nCase << ": ";
		if (K)  cout << "IMPOSSIBLE" << endl;
		else    cout << swaps << endl;
	}
};

int main()
{
	int N;  cin >> N;
	Problem sol;	for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}