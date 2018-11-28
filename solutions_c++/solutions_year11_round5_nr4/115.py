// Paste me into the FileEdit configuration dialog

#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <iostream>
#include <cmath>
#include <ctime>
#include <queue>

using namespace std;

const int MAX = 10000;
int W = 0;
double lx[MAX], ly[MAX], ux[MAX], uy[MAX];
double x[MAX];
int n = 0;
int L, U, G;
int a[MAX];
long long ans;
/*bool good (int q)
{
	for (int i = 2; i*i <= q; ++i)
		if (q % i == 0)
			return false;
	return true;
}*/
bool check(string& s)
{
	ans = 0;
	int p = s.length();
	for (int i = 0; i < p; ++i)
		if (s[i] == '1')
			ans = ans + (1LL << (p - i - 1));	
	long long q = floor(sqrt((double) ans) + 0.5);

	bool b = (q * q == ans);
	return b;
}
int main(int argc, char *argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_case_count;
	cin >> test_case_count;

	for (int test_case = 1; test_case<=test_case_count; ++test_case)
	{	
		string s;
		cin >> s;
		n = s.length();
		long long k = 0;
		for (int i = 0; i < n; ++i)
			if (s[i] == '?'){
				++k;
			}
		string ss;
		for (long long i = 0; i < 1LL << k; ++i)
		{
			ss = s;
			long long d = i;
			int p = 0;
			for (int j = 0; j < n; ++j)			
			if (s[j] == '?')
			{				
				ss[j] = ((d >> p) & 1LL) + '0';
				p++;
			}
			if (ss=="1011110110000100001")
			{
				int t = 0;
			}
			if (check(ss)) {
				break;
			}
		}

		cout << "Case #" << test_case << ": ";
		cout << ss;
		cout << endl;

	}
	fclose(stdout);
}

/*
cin >> W >> L >> U >> G;
		n = L+U;

		for (int i = 0; i < L: ++i)
		{
			cin >> lx[i] >> ly[i];
			x[i] = lx[i];
		}
		
		for (int i = 0; i < U: ++i)
		{
			cin >> ux[i] >> uy[i];
			x[i+L] = ux[i];
		}
		
		sort(x, x+n);

		double sumq = 0;
		for (int i = 0; i < n-1; ++i)
			sumq+=get_square(x[i], x[i+1]);

		double need = sumq / (G-1);

		int cutn = 0;
		int c=0; double cx= 0;
		while (cutn < G-1)
		{
		
			double has = loca
			while (fabs(has-local_need) > 1e-8) {
				double cc = (lo + high) / 2;
				has = get_square(x[c], x[c] + cc); 
				if (has > local_need)
					high = cc;
				else
					lo = cc;
			}
		}
		*/