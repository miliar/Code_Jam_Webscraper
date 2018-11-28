#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

class Problem
{
    set<string> dirs;
    vector<string> newdirs;
public:
	void ReadData()
	{
	    int N, M;
	    cin >> N >> M;
	    string s;
	       dirs.clear();  for (int i=0; i<N; ++i)  { cin >> s;  dirs.insert(s); }
	    newdirs.clear();  for (int i=0; i<M; ++i)  { cin >> s;  newdirs.push_back(s); }
	}
	void Solve(int nCase)
	{
		ReadData();

		int n0 = dirs.size();
		for (int i=0; i<newdirs.size(); ++i)
		{
		    for (int j=1; j<newdirs[i].length(); ++j)
		        if (newdirs[i][j]=='/')  dirs.insert(newdirs[i].substr(0, j));
	        dirs.insert(newdirs[i]);
		}
		cout << "Case #" << nCase << ": " << dirs.size()-n0 << endl;
	}
};

int main()
{
	int N;  cin >> N;
	Problem sol;	for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}