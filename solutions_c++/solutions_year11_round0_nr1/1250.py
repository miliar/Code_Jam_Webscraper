#include <iostream>
using namespace std;

class Problem
{
public:
	void Solve(int nCase)
	{
		int time[2] = { 0, 0 },
		    pos [2] = { 1, 1 };
	    int N;  cin >> N;
		for (int i=0; i<N; ++i)
		{
		    char R; int P;  cin >> R >> P;
		    int ix = R=='O';
		    time[ix] += abs(pos[ix] - P);           // move
		    time[ix] = max(time[0], time[1]) + 1;   // wait and push button
		    pos [ix] = P;
		}
        cout << "Case #" << nCase << ": " << max(time[0], time[1]) << endl;
	}
};

int main()
{
	int T;  cin >> T;
	Problem sol;	for (int i=1; i<=T; ++i)  sol.Solve(i);
	return 0;
}