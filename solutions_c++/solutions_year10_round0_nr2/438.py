#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cassert>
using namespace std;
string num[1001];
string diff[1000];

string TRIM(string a)
{
	int pos = a.find_first_not_of('0');
	if (pos == string::npos)
		a = "0";
	else
		a = a.substr(pos);
	return a;
}

bool is_greater(string a, string b)
{
	if (a.size() != b.size()) return a.size() > b.size();
	return a > b;
}

string DIFF(string a, string b)
{
	if (is_greater(b, a)) 
	{
		cout << "ERROR!!\n";
		exit(1);
	}
	if (a.size() > b.size())
		b = string(a.size() - b.size(), '0') + b;
	string c = string(a.size(), '0');
	for(int i = a.size() - 1; i >= 0; i--)
	{
		if(a[i] < b[i])
		{
			int j = i-1;
			while(a[j] == '0') j--;
			a[j++] -= 1;
			while(j != i)
				a[j++] = '9';
			a[i] += 10;
		}
		c[i] = a[i] - b[i] + '0';
	}
	return TRIM(c);
}

string DOUBLE(string a)
{
	string c = string(a.size(), '0');
	int carry = 0;
	for(int i = a.size() - 1; i >= 0; i--)
	{
		c[i] = (a[i] - '0') * 2 + '0' + carry;
		carry = 0;
		if (c[i] > '9')
		{
			c[i] -= 10;
			carry = 1;
		}
	}
	if (carry > 0)
		c = "1" + c;
	return TRIM(c);
}

string MOD(string a, string b)
{
	string bb = b;
	while(is_greater(a, DOUBLE(bb)))
		bb = DOUBLE(bb);
	if (is_greater(bb, a)) return a;
	if (a == bb) return "0";
	return MOD(DIFF(a, bb), b);
}

string GCD(string a, string b)
{
	string rem = MOD(a, b);
	if (rem == "0") return b;
	return GCD(b, rem);
}

int main()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		int N;
		cin >> N;
		for(int j = 0; j < N; j++)
		{
			cin >> num[j];
			num[j] = TRIM(num[j]);
		}
		sort(num, num + N, is_greater);
		for(int j = 0; j < N - 1; j++)
			diff[j] = DIFF(num[j], num[j+1]);
		int j = 0;
		while(diff[j] == "0") j++;
		string ans = diff[j++];
		for(; j < N - 1; j++)
		{
			if (diff[j] == "0") continue;
			ans = is_greater(ans, diff[j])? GCD(ans, diff[j]) : GCD(diff[j], ans);
		}
		string rem = MOD(num[0], ans);
		cout << "Case #" << i << ": " << ((rem == "0") ? "0" : DIFF(ans, rem )) << endl;
	}
	return 0;
}
