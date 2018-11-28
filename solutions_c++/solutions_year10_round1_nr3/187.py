#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define REP(a,b) for (int a=0; a<b; ++a)

bool test(int a, int b) {
	if (a < b) swap(a,b);
	if (a == b) return false;
	if (a % b == 0) return true;

	bool next = test(b,a%b);
	if (next && a/b < 2) return false;

	return true;
}

int main() 
{
	ifstream fin("c.in");
	ofstream fout("c.out");

	int tc, as, ae, bs, be, res;
	
	fin >> tc;

	REP(t,tc) {
		fin >> as >> ae >> bs >> be;

		res = 0;

		for (int a = as; a <= ae; ++a)
			for (int b = bs; b <= be; ++b) if (test(a,b)) {
				//cout << a << " " << b << endl;
				++res;
			}

		fout << "Case #" << t+1 << ": " << res << endl;
	}


	fout.close();

	return 0;
}