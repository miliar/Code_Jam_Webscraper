#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

bool comp(string a, string b)
{
	if (a.size() < b.size()) return true;
	else if (a.size() > b.size()) return false;
	else return (a < b);
}

string subt(string a, string b)
{
	string s, s1;
	int i, j;
	int x;
	for (i = a.size() - 1, j = b.size() - 1; j >= 0; j--, i--)
	{
		x = a[i] - b[j];
		if (x < 0) 
		{
			x += 10;
			a[i-1] -= 1;
		}
		s += (x + '0');
	}
	for (; i >= 0; i--)
	{
		if (a[i] < '0')
		{
			a[i] += 10;
			a[i-1] -= 1; 
		}
		s += a[i];
	}
	for (i = s.size() - 1; s[i] == '0'; i--);
	for (; i >= 0; i--) s1 += s[i];
	if (s1.empty()) s1 = "0";
	return s1;
}

string msub(string a, string b)
{
	while ( !comp(a, b) ) a = subt(a, b);
	return a;
}

string modl(string a, string b)
{
	string s;
	for (int i = 0; i < a.size(); i++)
	{
		if (s == "0") s = "";
		s += a[i];
		s = msub(s, b);
	}
	return s;
}
string gcd(string a, string b)
{
	if (b == "0") return a;
	else return gcd(b, modl(a,b));
}

int main()
{
	int t;
	cin >> t;
	int n;
	string *ar;
	vector<string> v;
	for (int i = 1; i <= t; i++)
	{
		cin >> n;
		ar = new string[n];
		for (int j = 0; j < n; j++)
		{
			cin >> ar[j];
		}
		sort(ar, ar+n, comp);
		for (int j = 0; j < n-1; j++)
		{
			for (int k = j+1; k < n; k++)
			{
				v.push_back(subt(ar[k], ar[j]));
			}
		}
		sort(v.begin(), v.end(), comp);
		string T;
		T = v[0];
		for (int j = 1; j < v.size(); j++)
		{
			T = gcd(v[j], T);
		}
		string ans, r;
		if ((r = modl(ar[0], T)) != "0")
		{
			ans = subt(T, r);
		}
		else ans = "0";
		cout << "Case #" << i << ": " << ans << endl;
		v.clear();
	}
	return 0;
}
