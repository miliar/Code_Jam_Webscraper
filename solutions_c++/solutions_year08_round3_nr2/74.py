#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

class ProblemB
{
	string num;
	bool ugly(int ops)
	{
		long long res = 0, cur = num[0]-'0';
		bool plus = true;
		for (int i=1; i<num.length(); ++i, ops/=3)
			if (ops%3)
			{
				if (plus)  res += cur;  else  res -= cur;
				cur = num[i]-'0';
				plus = ops%3==1;
			}
			else
				cur = cur*10 + num[i]-'0';
		if (plus)  res += cur;  else  res -= cur;
		return !(res%2 && res%3 && res%5 && res%7);
	}
public:
	void ReadData()
	{
		cin >> num;
	}
	void Solve(int nCase)
	{
		ReadData();

		int ops = 1;  for (int i=num.length()-1; i-->0; )  ops *= 3;

		int cnt = 0;
		while (ops--)  cnt += ugly(ops);

		cout << "Case #" << nCase << ": " << cnt << endl;
	}
};

int main()
{
	int N;  string s;  getline(cin, s);  istringstream(s) >> N;
	ProblemB sol;	for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}