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

int minsw[101][1011];

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");
	
	int T;
	fin >> T;
	For (LOL, 1, T+1)
	{
		int S, Q;
		fin >> S;
		
		map<string,int> id;
		int cid = 0;
		string t;
		For (i, 0, S) {
			t = "";
			while (t == "")
				getline(fin, t);
			if (!id.count(t))
				id[t] = cid++;
		}
		
		memset(minsw, 0x7f, sizeof(minsw));
		
		For (i, 0, S)
			minsw[i][0] = 0;
		
		fin >> Q;
		For (i, 0, Q)
		{
			t = "";
			while (t == "")
				getline(fin, t);
			int hit = id[t];
			For (j, 0, S)
				if (j != hit)
					minsw[j][i+1] <?= minsw[j][i];
				else
					For (k, 0, S)
						if (k != hit)
							minsw[k][i+1] <?= minsw[j][i]+1;
		}
		
		int res = 0x7f7f7f7f;
		For (i, 0, S)
			res <?= minsw[i][Q];
			
		fout << "Case #" << LOL << ": " << res << endl;
	}
	
	return 0;
}