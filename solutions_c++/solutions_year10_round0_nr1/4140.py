#include <iostream>
using namespace std;

class Problem
{
public:
	void Solve(int nCase)
	{
        int N, K;  cin >> N >> K;
        for (; N>0 && K%2; --N)  K/=2;
		cout << "Case #" << nCase << ": " << (N?"OFF":"ON") << endl;
	}
};

int main()
{
	int N;  cin >> N;
	Problem sol;  for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}