#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Problem
{
public:
	void Solve(int nCase)
	{
		int R, C;  cin >> R >> C;
		vector<string> T(R);  for (int i=0; i<R; ++i)  cin >> T[i];

        for (int i=0; i<R-1; ++i)
        for (int j=0; j<C-1; ++j)
            if (T[i][j]=='#' && T[i][j+1]=='#' && T[i+1][j]=='#' && T[i+1][j+1]=='#')
            {
                T[i][j] = T[i+1][j+1] = '/';
                T[i][j+1] = T[i+1][j] = '\\';
            }
            
        bool ok = true;
        for (int i=0; i<R; ++i)  if (T[i].find('#')!=string::npos)  ok = false;

		cout << "Case #" << nCase << ": " << endl;
		if (ok)  for (int i=0; i<R; ++i)  cout << T[i] << endl;
		else     cout << "Impossible" << endl;
	}
};

int main()
{
	int T;  cin >> T;
	Problem task;	for (int i=1; i<=T; ++i)  task.Solve(i);
	return 0;
}