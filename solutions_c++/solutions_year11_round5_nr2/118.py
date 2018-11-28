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
int main(int argc, char *argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_case_count;
	cin >> test_case_count;

	for (int test_case = 1; test_case<=test_case_count; ++test_case)
	{	
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> a[i];
		sort(a, a+n);
		vector<vector<int>> v;
		for (int i = 0; i < n; ++i)
		{
			int k = a[i];			
			int ind = -1;
			for (int j = 0; j < v.size(); ++j)
				if (v[j].back() == k - 1)
				{
					if (ind == -1 || v[ind].size() > v[j].size())
						ind = j;
				}
			if (ind != -1)
			{
				v[ind].push_back(k);
			}
			else
			{
				vector<int> vv;
				vv.push_back(k);
				v.push_back(vv);
			}
		}

		int ans = MAX;
		for (int i = 0; i < v.size(); ++i)
			ans = min(ans, (int)v[i].size());
		cout << "Case #" << test_case << ": ";
		if (ans < MAX)
			cout << ans;
		else
			cout << 0;
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