#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <limits>
using namespace std;

class TaskA
{
	vector<string> se;
	vector<int> queries;
public:
	void ReadData()
	{
		string s;
		int S, Q;
		getline(cin, s);  istringstream(s) >> S;
		se.resize(S);
		for (int i=0; i<se.size(); ++i)  getline(cin, se[i]);
		getline(cin, s);  istringstream(s) >> Q;
		queries.resize(Q);
		for (int i=0; i<queries.size(); ++i)
		{
			getline(cin, s);
			queries[i] = find(se.begin(), se.end(), s) - se.begin();
		}
	}
	void Solve(int nCase)
	{
		ReadData();

		vector<int> a(se.size(), 0);			// a[i] - min seq length ending with i-th search engine
		int m = 0;								// current min seq length
		for (int i=0; i<queries.size(); ++i)
		{
			a[queries[i]] = numeric_limits<int>::max();
			m = *min_element(a.begin(), a.end());
			for (int j=0; j<a.size(); ++j)  a[j] = min(a[j], m+1);
		}

		cout << "Case #" << nCase << ": " << m << endl;
	}
};

int main()
{
	int N;  string s;  getline(cin, s);  istringstream(s) >> N;
	TaskA sol;	for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}