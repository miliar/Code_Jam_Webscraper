#include <cmath>
#include <map>
#include <deque>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
string s;
typedef long long lint;
void Brute(int n, deque<lint> & ret)
{	
	long long mlp = 10;
	long long now = s[n] - '0';	
	deque<lint> tmp;
	for(int i = n - 1; i >= 0; i--)
	{
		tmp.clear();
		Brute(i, tmp);
		for(int j = 0; j < tmp.size(); j++)
		{
			ret.push_back(tmp[j] + now);
			ret.push_back(tmp[j] - now);
		}
		now += (s[i] - '0') * mlp;
		mlp *= 10;
	}
	mlp = 1;
	lint r = 0;
	for(int k = n; k >= 0; k--)
	{
		r += (s[k] - '0') * mlp;
		mlp *= 10;
	}
	ret.push_back(r);
}
int e(int n, int k)
{
	int mlp = 1;
	for(int i = 1; i <= k; i++)
		mlp *= n;
	return mlp;
}
int main()
{	
	int cases;
	string tmp;
	ifstream input("input.txt");	
	ofstream output("output.txt");
	input >> cases;		
	deque<lint> ret;	
	for(int t = 1; t <= cases; t++)
	{	
		input >> s;
		ret.clear();
		Brute(s.size() - 1, ret);
		int ans = 0;
		if( e(3, s.size() - 1) != ret.size())
			cout << 'x';
		for(int i = 0; i < ret.size(); i++)
			if((ret[i] % 2 == 0) || (ret[i] % 5 == 0) || (ret[i] % 3 == 0) || (ret[i] % 7 == 0))
				ans++;
		output << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}