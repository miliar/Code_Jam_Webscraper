#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

#define mset(c, val) memset((c), (val), sizeof((c)))
#define all(v) v.begin(), v.end()
#define INF 1000000000
#define EPS 1e-10

typedef vector<int> vi;
typedef long long lint;

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int test, tnum;
	lint res;

	void outputdata()
	{
		fout << "Case #" << (test + 1) << ": " << res << endl;
	}

int main()
{
    fin >> tnum;
	for (test = 0; test < tnum; test++) {
		int n, t;
		fin >> n;
		vector<lint> a;
		vector<lint> b;
		for (int i = 0; i < n; i++) {
			fin >> t;
			a.push_back(t);
		}
		for (int i = 0; i < n; i++) {
			fin >> t;
			b.push_back(t);
		}		
		sort(all(a));
		sort(all(b));
		reverse(all(b));
		res = 0;
		for (int i = 0; i < n; i++)
			res += a[i] * b[i];
		outputdata();
	}
	return 0;
}
