#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<cstdlib>
#include<iomanip>
#include<sstream>
using namespace std;

//============================================================
// Welcome
//============================================================
class Welcome
{
public:
	Welcome(const string &s,const string &t)
		:str(s),target(t){}

	string Solve()
	{
		memo.assign(str.size(),vector<int>(target.size(),-1));

		ostringstream oss;
		oss << setfill('0') << setw(4) << SolveP();
		return oss.str();
	}

private:
	string str,target;

	vector<vector<int> > memo;

	int SolveP(int str_pos=0,int target_pos=0)
	{
		if(target_pos >= (int)target.size()) return 1;
		if(str_pos >= (int)str.size()) return 0;

		int &m = memo[str_pos][target_pos];
		if(m != -1) return m;

		int sum = 0;
		// Find next target char.
		int ch = target[target_pos];
		// Try all str_pos with this char.
		for(int k = str_pos;k < (int)str.size();++k){
			if(str[k] == ch){
				sum += SolveP(k+1,target_pos+1);
				sum %= 10000;
			}
		}

		return m = sum;
	}
};
//============================================================

int main()
{
	string s;
	getline(cin,s);
	int N = atoi(s.c_str());
	for(int k = 0;k < N;++k){
		getline(cin,s);
		Welcome problem(s,"welcome to code jam");
		cout << "Case #" << k+1 << ": " << problem.Solve() << '\n';
	}
}
