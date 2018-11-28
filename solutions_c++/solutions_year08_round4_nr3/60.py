#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
using namespace std;

#define FORALL(var,x) for (typeof(x.begin()) var=x.begin(); var!=x.end(); var++)
#define FOR(var,lo,hi) for (int var=(lo); var<(hi); var++)
#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef vector<int> vi;

double x[1024][3], p[1024];

int main(void)	{
	int numTestCases, N;
	cin >> numTestCases;
	
	for (int nc = 1; nc <= numTestCases; nc++)	{
		cin >> N;
		for (int i = 0; i < N; i++)	{
			for (int k = 0; k < 3; k++)		cin >> x[i][k];
			cin >> p[i];
		}

		double low = 1e-10;
		double high = low;

		for (int i = 0; i < N; i++)	for (int j = i+1; j < N; j++)	{
			double dis = 0;
			for (int k = 0; k < 3; k++)	dis += 1.0 * abs(x[i][k] - x[j][k]);
			high = max(high, dis / (p[i] + p[j]));
		}
		high *= 2.0;

		for (int iter = 1; iter <= 1000; iter++)		{
			double P = (low + high) / 2.0;

			bool ok = true;
			for (int i = 0; i < N && ok; i++)	for (int j = i+1; j < N && ok; j++)	{
				double dis = 0;
				for (int k = 0; k < 3; k++)	dis += 1.0 * abs(x[i][k] - x[j][k]);
				if (dis > P * (p[i] + p[j]))	ok = false;	
			}
			//cout << low << "\t" << high << "\t" << P << "\t" << ok << endl;
			if (ok)	high = P;
			else	low = P;
		}
	

		cout << "Case #" << nc << ": ";
		printf ("%0.6lf\n", (low+high)/2.0);
	}
}
