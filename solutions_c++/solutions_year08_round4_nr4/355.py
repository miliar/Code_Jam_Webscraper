#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

int k;
string s;
string s2;
int ans;
int p[20];
bool b[20];

int calc()
{
	s2 = "";
	int l = s.length()/k;
	FI(i,0,l)
		FI(j,0,k) s2 += s[i*k+p[j]];
	int ret = 1;
	l = s.length();
	FI(i,1,l)
		if (s2[i-1] != s2[i]) ret++;
	return ret;
}

void search(int s)
{
	if (s >= k)
	{
		int q = calc();
		if (ans < 0 || q < ans) ans = q;
		return;
	}
	FI(i,0,k) if (!b[i])
	{
		b[i] = true;
		p[s] = i;
		search(s+1);
		b[i] = false;
	}
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
		int i,j;
		//istringstream strin();
		fin >> k >> s;
		s2.reserve(s.length());

		ans = -1;
		mset(b, 0);
		search(0);

		fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}
