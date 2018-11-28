#include <iostream>
#include <limits>
using namespace std;

class Problem
{
public:
	void Solve(int nCase)
	{
	    int res = numeric_limits<int>::max(), sum = 0, sumx = 0;
	    int N;  cin >> N;
	    for (int i=0; i<N; ++i)
	    {
	        int C;  cin >> C;
	        res   = min(res, C);
	        sum  += C;
	        sumx ^= C;
	    }
        if (sumx)  cout << "Case #" << nCase << ": " << "NO" << endl;
        else       cout << "Case #" << nCase << ": " << sum-res << endl;
	}
};

int main()
{
	int T;  cin >> T;
	Problem sol;	for (int i=1; i<=T; ++i)  sol.Solve(i);
	return 0;
}