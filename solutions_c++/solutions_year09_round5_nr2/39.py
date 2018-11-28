#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

int n;
const int mm = 10009;
int K;
map<string,int> m[11];
int ans[11] = {};
int w[101][26];

int calc(int d, const string& t)
{
	if (t == "") {
		int ret = 1;
		for (int i = 1; i <= d; ++i)
			ret = ret * n % mm;
		return ret;
	}

	map<string,int>::iterator it = m[d].find(t);
	if (it != m[d].end()) {
		return it->second;
	}

	int ret = 0;
	if (d == 1) {
		FI(i,0,n) {
			int z = 1;
			FI(j,0,t.length()) z *= w[i][t[j]-'a'];
			ret = (ret + z)%mm;
		}
	} else {
		int l = t.length();
		int ll = 1<<l;
		FI(i,0,ll) {
			string t1 = "";
			string t2 = "";
			int i1 = i;
			FI(j,0,l) {
				if (i1%2 == 0) t1 += t[j]; else t2 += t[j];
				i1 /= 2;
			}
			ret = (ret + calc(d-1,t1)*calc(1,t2)) % mm;
		}
	}

	m[d][t] = ret;
	return ret;
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
		FI(i,0,11) m[i].clear();
		mset(w, 0);
		//istringstream strin();
		string s;
		fin >> s;
		fin >> K;
		fin >> n;
		for (int i = 0; i < n; ++i) {
			string str;
			fin >> str;
			for (int j = 0; j < str.length(); ++j)
				++w[i][str[j]-'a'];
		}

		mset(ans, 0);
		while (s != "") {
			int i = 0;
			while (i < s.length() && s[i] != '+') ++i;
			string term = s.substr(0,i);

/*			int n1 = term.length();
			FI(i1,0,n1) FI(i2,i1+1,n1)
				if (term[i1] > term[i2]) {
					char ch = term[i1];
					term[i1] = term[i2];
					term[i2] = ch;
				}
*/
			FI(j,1,K+1) {
				ans[j] += calc(j, term);
			}

			if (i >= s.length()) break;
			s = s.substr(i+1);
		}


		fout << "Case #" << tind << ":";
		FI(i,1,K+1) fout << ' ' << ans[i] % mm;
		fout << endl;
	}
	return 0;
}
