#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
#include <ctime>
using namespace std;

#define all(x) (x).begin(), (x).end()
#define foreach(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define sz(x) ((int)(x).size())
#define init(st) memset(st, 0, sizeof(st)) 
#define ll long long

template<class T>
void splitstr(const string &s, vector<T> &out)
{
    istringstream in(s);
    out.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

ll arr[20];
ll arrt[20];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int cases;
	cin >> cases; cin.get();
	string welc = "welcome to code jam";

	for(int q = 0; q < cases; q++)
	{
		string s;
		getline(cin, s);
		init(arr);
		for(int i = 0; i < s.size(); i++)
		{
			memcpy(arrt, arr, sizeof(arr));

			for(int j = 0; j < 19; j++)
				if(welc[j] == s[i])
					arrt[j] += (!j)?1:arr[j-1];

			for(int j = 0; j < 19; j++)
				arrt[j] %= 10000;
			memcpy(arr, arrt, sizeof(arr));
		}

		printf("Case #%d: %04d\n", q+1, arr[18]);
	}

	return 0;
}