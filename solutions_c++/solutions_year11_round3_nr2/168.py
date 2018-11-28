#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;

vector <long long> a;
long long b[2000000];
vector <long long> r;

int main()
{
     freopen("input.txt", "r", stdin);
     freopen("output.txt", "w", stdout);

     int NTests;
     cin >> NTests;

     for (int test = 0; test < NTests; test++)
     {
		 int k, n, c;
		 long long T;
		 cin >> k >> T >> n >> c;
		 a.clear();
		 for (int i = 0; i < c; i++)
		 {
			 int x;
			 cin >> x;
			 a.push_back(x);
		 }

		 while (a.size() < n)
		 {
			 for (int i = 0; i < c; i++)
				 a.push_back(a[i]);
		 }

		 long long len = 0;

		 for (int i = 0; i < n; i++)
			 len += a[i];

		 b[0] = 0;
		 for (int i = 1; i <= n; i++)
			 b[i] = a[i-1]+b[i-1];

		long long res;
		long long now_t = 0;
		long long pos = 0;		

		if (T/2 >= len)
			res = len*2;
		else
		{
			res = T;

			int pos = 0;

			for (int i = 0; i < n; i++)
				if (b[i+1] > T/2)
				{
					pos = i;
					b[i] = T/2;
					break;
				}

			r.clear();

			for (int i = pos; i < n; i++)
				r.push_back(b[i+1]-b[i]);

			sort(r.begin(), r.end());

			for (int i = r.size() - 1; i >= 0; i--)
			{
				if (k > 0)
					res += r[i];
				else
					res += r[i]*2;
				k--;
			}
		}
		
		cout << "Case #" << test+1 << ": ";
		

        cout << res << endl;
		cerr << test+1 << endl;
     }

     return 0;
}