#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;
int mod = 10009;
struct monom
{
	vector<int> v;
	monom(string str)
	{
		v.resize(26, 0);
		for(int i = 0; i < str.size(); i++)
			v[str[i] - 'a']++;
	}
	int eval(const vector<int>& p)
	{
		int res = 1;
		for(int i =0; i < 26; i++)
		{
			for(int j = 0; j < v[i]; j++)
				res = (res * p[i]) % mod;
		}
		return res;
	}
};
vector<monom> v;
int eval(const vector<int>& ve)
{
	int res = 0;
	for(int i = 0; i < v.size(); i++)
		res = (res + v[i].eval(ve)) % mod;
	return res;
}
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d:", testCounter + 1);
		string poli;
		int k;
		cin >> poli >> k;
		for(int i = 0; i < poli.size(); i++)
		{
			if(poli[i] == '+')
				poli[i] = ' ';
		}
		stringstream ss;
		ss << poli;
		v.clear();
		while(ss >> poli)
		{
			monom m(poli);
			v.push_back(m);
		}
		int n;
		cin >> n;
		vector<string> words(n);
		for(int i = 0; i < n; i++)
			cin >> words[i];
		vector<vector<int> > repres(n);
		for(int  i= 0; i < n ;i++)
		{
			repres[i].resize(26, 0);
			for(int j = 0; j < words[i].size(); j++)
				repres[i][words[i][j] - 'a']++;
		}
		map<vector<int>, int> cur;
		vector<int> temp2(26, 0);
		cur[temp2] = 1;
		vector<int> res(k, 0);
		for(int i = 0; i < k; i++)
		{
			map<vector<int>, int> temp;
			for(int j = 0; j < n; j++)
			{
				for(map<vector<int>, int>::iterator itr = cur.begin(); itr != cur.end(); ++itr)
				{
					for(int q = 0; q < 26; q++)
						temp2[q] = itr->first[q] + repres[j][q];
					temp[temp2] += itr->second;
				}
			}
			for(map<vector<int>, int>::iterator itr = temp.begin(); itr != temp.end(); ++itr)
			{
				res[i] = (res[i] + itr->second * eval(itr->first)) % mod;
			}
			cur = temp;
		}
		for(int i = 0; i < k ;i++)
			cout << " " << res[i];
		cout << endl;
		
	}
	return 0;
}
