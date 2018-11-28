#include <iostream>
using namespace std;

class Problem
{
public:
	void Solve(int nCase)
	{
	    int N;  cin >> N;
	    int res = N;
	    for (int i=1; i<=N; ++i)
	    {
	        int n;  cin >> n;
	        res -= n==i;
	    }
		cout << "Case #" << nCase << ": " << res << endl;
	}
};

int main()
{
	int T;  cin >> T;
	Problem sol;	for (int i=1; i<=T; ++i)  sol.Solve(i);
	return 0;
}