#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <string>
#include <algorithm>
#include <functional>
#include <utility>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define _bpc __builtin_popcount
#define pb push_back
#define MP make_pair
#define For(a,b,c) for(typeof(b)a=(b); a<(c); ++a)
#define ALL(a) a.begin(),a.end()
#define DBG(a) cout << #a << ": " << a << endl
#define FORE(i, v) for(typeof(v.begin()) i = v.begin(); i != v.end(); ++i)

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");
	
	int T;
	fin >> T;
	For (lol, 1, T+1)
	{
		int N; fin >> N;
		
		int a[1111], b[1111];
		
		For (i, 0, N) fin >> a[i];
		For (i, 0, N) fin >> b[i];
		sort(a, a+N);
		sort(b, b+N);
		
		ll res = 0;		
		
		int st = 0, end = N-1;
		for (int i = N-1; i >= 0; i--)
			if (a[i])
				if (a[i] > 0)
					res += a[i] * (ll)b[st++];

		for (int i = 0; i < N; i++)
			if (a[i])
				if (a[i] < 0)
					res += a[i] * (ll)b[end--];
					
		fout << "Case #" << lol << ": " << res << endl;
	}
}
