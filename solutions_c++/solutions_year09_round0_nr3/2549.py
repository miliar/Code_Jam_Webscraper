#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int n;
int a[501][20];
string s = "maj edoc ot emoclew";//""welcome to code jam";
int M = 1000;

string solve(string str)
{
	memset(a, 0, sizeof(a));
	for (int i = str.size(); i >= 0; i--)
		a[i][0] = 1;
	for (int i = str.size()-1; i >= 0; i--)
	{
		for (int j = 0; j < s.size(); j++)
		{
			a[i][j+1] = a[i+1][j+1];
			if (str[i] == s[j])
			{
				a[i][j+1] += a[i+1][j];
			}
			a[i][j+1] %= 1000;
		}
	}
	int r = a[0][s.size()];
	string res = "1234";
	for (int i = 3; i >= 0; i--)
	{
		res[i] = '0' + r % 10;
		r /= 10;
	}
	return res;
}

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	cin >> n;
	cin.get();
	char cc[500];
	for (int i = 0 ; i < n; i ++)
	{
		cin.getline(cc, 500);
		string str = cc;
		cout << "Case #" << i+1 << ": " << solve(str) << endl;
	}
}