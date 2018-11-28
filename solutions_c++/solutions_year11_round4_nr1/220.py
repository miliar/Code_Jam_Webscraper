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
double bb[MAX], ee[MAX], ww[MAX];

int main(int argc, char *argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_case_count;
	cin >> test_case_count;
	for (int test_case = 1; test_case<=test_case_count; ++test_case)
	{		 
		double x, s, r, t, n;
		double res = 0;
		cin >> x >> s >> r >> t >> n;
		double hast = t;
		int hasx = x;
		double timehere = 0;
	
		for (int i = 0; i < n; ++i)
		{
			cin >> bb[i] >> ee[i] >> ww[i];
			hasx -= ee[i] - bb[i];
		}
		for (int i = 0; i < n; ++i)
			for (int j = i+1; j < n; ++j)
			if (ww[i] > ww[j])
			{
				double tt = ww[i];
				ww[i] = ww[j];
				ww[j]=tt;
				tt = ee[i];
				ee[i] = ee[j];
				ee[j]=tt;
				tt = bb[i];
				bb[i] = bb[j];
				bb[j]=tt;

			}
		if (hasx > 0){
			if (hasx / (r) <= hast) {
				timehere = hasx / (r);
				hast -= timehere;
			} else {
				double l1 = (r)*hast;
				double l2 = hasx - l1;
				timehere = hast + l2 / (s);
				hast = 0;
			}			
		}
		res += timehere;
		for (int i = 0; i < n; ++i)
		{
			double b, e, w;
			b=bb[i];
			e=ee[i];
			w=ww[i];
			double len = e - b;
			double timehere = 0;
			hasx -= len;
			if (len / (w + r) <= hast) {
				timehere = len / (w + r);
				hast -= timehere;
			} else {
				double l1 = (w+r)*hast;
				double l2 = len -= l1;
				timehere = hast + l2 / (w+s);
				hast = 0;
			}

			res+=timehere;
		}
		
		
		cout.precision(12);
		cout << "Case #" << test_case << ": " << res;

		cout << endl;

	}
	fclose(stdout);
}

