#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;

vector<string> buildDiamond(int k)
{
	vector<string> r(2 * k - 1, string(2 * k - 1, ' '));
	for(int i = 1; i <= k; ++i)
	{
		for(int j = k - i, c = 0; c < i; ++c)
			r[i - 1][j] = '#',
			j += 2;
	}
	for(int i = k + 1; i <= 2 * k; ++i)
	{
		for(int j = i - k, c = 0; c < 2 * k - i; ++c)
			r[i - 1][j] = '#',
			j+= 2;
	}
	return r;
}

void output(vector<string> &a)
{
	for(int i = 0; i < a.size(); ++i)
	{
		cout << a[i] << endl;
	}
}

bool put(vector<string> &w, int x, int y, vector<string> &a)
{
	
	for(int i = x; i < x + (int)a.size(); ++i)
		for(int j = y; j < y + (int)a.size(); ++j)
		{
//			if(a[i-x][j-y] == ' ' && w[i][j] != ' ')
//				return false;
			
			if(a[i-x][j-y] != ' ' && (i < 0 || j < 0 || i >= w.size() || j >= w.size() || w[i][j] == ' '))
				return false;
		}
	
	for(int i = x; i < x + (int)a.size(); ++i)
		for(int j = y; j < y + (int)a.size(); ++j)
			if(a[i-x][j-y] != ' ')
				w[i][j] = a[i-x][j-y];
	return true;
}
void unput(vector<string> &w, int x, int y, vector<string> &a)
{
	

	
	for(int i = x; i < x + (int)a.size(); ++i)
		for(int j = y; j < y + (int)a.size(); ++j)
			if(a[i-x][j-y] != ' ')
				w[i][j] = '#';

}

bool check(vector<string> &a)
{
	/*
	Horizontal symmetry: Let ci be the number of digits on line i. 
	The jth digit on line i (where j=1 for the first digit) must be the same as the ci+1-jth digit.

Vertical symmetry: The jth digit on line i (where i=1 for the first line) must be the same as the jth digit on line 2k-i.
*/
	for(int i = 0; i < a.size(); ++i)
		for(int j = 0; j < a.size(); ++j)
			if(a[i][j] != ' ')
			{
				char &p11 = a[i][j];
				char &p12 = a[i][a[i].length() - j - 1];
				char &p21 = a[a.size() - i - 1][j];
				char &p22 = a[a.size() - i - 1][a[i].length() - j - 1];
				if(p11 == '#' && p12 == '#' && p21 == '#' && p22 == '#')
					continue;
				char t;
				if(p11 != '#') t = p11;
				if(p12 != '#') t = p12;
				if(p21 != '#') t = p21;
				if(p22 != '#') t = p22;

				if((p11 == '#' || p11 == t) && (p12 == '#' || p12 == t) && (p21 == '#' || p21 == t) && (p22 == '#' || p22 == t))
				{
				} else
					return false;
			}
	return true;
}


int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int n; scanf("%d", &n);
		vector<string> a(2*n-1);
		string s;
		getline(cin, s);
		for(int i = 0; i < 2 * n - 1; ++i)
			getline(cin, a[i]);

		int ans = -1;
		int e = 0;
		for(int i = 0; i < a.size(); ++i)
			for(int j = 0; j < a[i].length(); ++j)
				if(a[i][j] != ' ')
					e++;
		for(int i = 0; i < a.size(); ++i)
			while(a[i].length() < a.size()) a[i] += " ";

		for(int i = n; ans == -1; ++i)
		{
			vector<string> w = buildDiamond(i);
			int q = 0;
			for(int j = 0; j < w.size(); ++j)
				for(int k = 0; k < w.size(); ++k)
					if(w[j][k] != ' ')
						q++;

			for(int j = -(int)w.size(); j < (int)w.size() && ans == -1; ++j)
				for(int k = -(int)w.size(); k < (int)w.size() && ans == -1; ++k)
				{
					vector<string> w = buildDiamond(i);
					if(put(w, j, k, a))
					{
						if(check(w))
						{
							ans = q - e;
							break;
						}
						
					}

				}
		}

		printf("Case #%d: %d\n", z + 1, ans);
		
	
	}
	return 0;
}
#endif