#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

class ProblemA
{
	int M, V;
	vector<int> tree;
	vector<int> chg;
	vector<int> val;
public:
	void ReadData()
	{
		cin >> M >> V;
		tree.resize((M-1)/2);  chg.resize((M-1)/2);
		for (int i=0; i<(M-1)/2; ++i)  cin >> tree[i] >> chg[i];
		val.resize((M+1)/2);
		for (int i=0; i<(M+1)/2; ++i)  cin >> val[i];
	}
	void Solve(int nCase)
	{
		ReadData();

		vector<vector<int> > todo(2, vector<int>(M, 100000));
		for (int i=0; i<(M+1)/2; ++i)  todo[val[i]][(M-1)/2+i] = 0;

		for (int i=(M-1)/2; i-->0; )
			if (tree[i])
			{
				todo[0][i] = min(todo[0][i], todo[0][2*i+1]+min(todo[0][2*i+2], todo[1][2*i+2]));
				todo[0][i] = min(todo[0][i], todo[1][2*i+1]+todo[0][2*i+2]);
				todo[1][i] = min(todo[1][i], todo[1][2*i+1]+todo[1][2*i+2]);
				if (chg[i])
				{
					todo[1][i] = min(todo[1][i], todo[0][2*i+1]+todo[1][2*i+2]+1);
					todo[1][i] = min(todo[1][i], todo[1][2*i+1]+todo[0][2*i+2]+1);
				}
			}
			else
			{
				todo[1][i] = min(todo[1][i], todo[1][2*i+1]+min(todo[0][2*i+2], todo[1][2*i+2]));
				todo[1][i] = min(todo[1][i], todo[0][2*i+1]+todo[1][2*i+2]);
				todo[0][i] = min(todo[0][i], todo[0][2*i+1]+todo[0][2*i+2]);
				if (chg[i])
				{
					todo[0][i] = min(todo[0][i], todo[0][2*i+1]+todo[1][2*i+2]+1);
					todo[0][i] = min(todo[0][i], todo[1][2*i+1]+todo[0][2*i+2]+1);
				}
			}

		cout << "Case #" << nCase << ": ";
		if (todo[V][0]<100000)  cout << todo[V][0];  else  cout << "IMPOSSIBLE";
		cout << endl;
	}
};

int main()
{
	int N;  string s;  getline(cin, s);  istringstream(s) >> N;
	ProblemA sol;	for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}