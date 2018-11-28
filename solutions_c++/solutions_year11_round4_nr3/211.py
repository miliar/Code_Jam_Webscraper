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

const int MAX = 15000000;

long long pr[MAX];
bool p[MAX];


int main(int argc, char *argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_case_count;
	cin >> test_case_count;
	for (int i = 2; i < MAX; ++i)
		p[i] = true;
	for (int i = 2; i < MAX; ++i)
		for (int j = 2; j < MAX / i; ++j)
			p[i*j] = false;

	int k = 0;
	for (int i = 2; i < MAX; ++i)
		if (p[i])
			pr[k++] = i;
	for (int test_case = 1; test_case<=test_case_count; ++test_case)
	{		 
		long long n;
		cin >> n;
		long long ans = -1;
		if (n == 0)
			ans = 0;
		long long sum = 0;
		for (int i = 0; ans<0 && i < k && pr[i]*pr[i] <=n; ++i)
		{
			long long d = 0;
			long long q = pr[i];
			while (q * pr[i] <= n)
			{
				q*=pr[i];
				++d;
			}
			sum+=d;
		}
		
		cout << "Case #" << test_case << ": ";
		if (n==1LL) sum =-1;
		cout << sum+1;
		cout << endl;

	}
	fclose(stdout);
}

