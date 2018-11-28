#include <algorithm>
#include <iostream>
#include <fstream> 
#include <iterator>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
#define PB push_back
#define big __int64
#define For(i,n) for (i = 0 ; i < n ; i ++)
#define bend(v) v.begin (), v.end ()
vs split (string s, string delim = " ") {vs res; string t; unsigned int i ; For (i, s.size ()) {if (delim.find (s [i]) != string::npos) {if (! t.empty ()) {res.PB (t); t = "" ;}} else {t += s [i] ; }} if (! t.empty ()) {res.PB (t) ;} return res ;}

int main()
{
	freopen("A-large(2).in","rt",stdin);
	freopen("result.out","wt",stdout);

	int testno;
	cin >> testno;

	for (int tno = 0; tno < testno; tno++)
	{
		cout << "Case #" << tno + 1 << ": ";
		
		int n;
		cin >> n;

		vector<big> x;
		vector<big> y;

		for (int i = 0; i < n; i++)
		{
			big num;
			cin >> num;
			x.PB(num);
		}

		for (int i = 0; i < n; i++)
		{
			big num;
			cin >> num;
			y.PB(num);
		}

		sort(x.begin(), x.end());
		sort(y.begin(), y.end());

		big res = 0;
		for (int i = 0; i < x.size(); i++)
			res += (x[i] * y[y.size() - i - 1]);

		cout << res << endl;
	}
	
	return 0;
}