#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

string inName;
string outName;

#define cin fin
#define cout fout

#define max(a,b)    (((a) > (b)) ? (a) : (b))

int main()
{
	inName = "D-small.in";
	//	inName = "D-large.in";
	outName = "D-small.out";
	//	outName = "D-large.out";

	int tc;
	ifstream fin(inName.c_str());
	ofstream fout(outName.c_str());
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		int n;
		cin >> n;
		int x[3];
		int y[3];
		int r[3];
		for(int i = 0; i < n; ++i)
		{
			cin >> x[i] >> y[i] >> r[i];
		}
		cout<<"Case #"<<Case+1<<": ";
		if(n == 1)
		{
			cout << r[0] << endl;
		}
		else if(n == 2)
		{
			cout << max(r[0], r[1]) << endl;
		}
		else
		{
			double a[3];
			double d[3];
			d[0] = hypot(abs(x[0] - x[1]), abs(y[0]-y[1]));
			d[1] = hypot(abs(x[2] - x[1]), abs(y[2]-y[1]));
			d[2] = hypot(abs(x[0] - x[2]), abs(y[0]-y[2]));
			a[0] = max(max(max((d[0]+r[0]+r[1])/2, r[0]), r[1]), r[2]);
			a[1] = max(max(max((d[1]+r[2]+r[1])/2, r[2]), r[1]), r[0]);
			a[2] = max(max(max((d[2]+r[0]+r[2])/2, r[0]), r[2]), r[1]);
			double res = *min_element(a, a + 3);
			cout << res << endl;
		}
	}
	fout.close();
	fin.close();

	return 0;
}