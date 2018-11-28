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

int a[100000];

int main()
{
     freopen("input.txt", "r", stdin);
     freopen("output.txt", "w", stdout);

     int NTests;
     cin >> NTests;

     for (int test = 0; test < NTests; test++)
     {
		 int n, l, h;
		 cin >> n >> l >> h;
		 for (int i = 0; i < n; i++)
			 cin >> a[i];

         cout << "Case #" << test + 1 << ": ";
		 
		 bool q = true;
		 
		 for (int i = l; i <= h; i++)
		 {
			 q = true;
			 for (int j = 0; j < n; j++)
				 if (a[j]%i != 0 && i%a[j] != 0)
					 q = false;
			 if (q)
			 {
				cout << i << endl;
				break;
			 }
		 }

		 if (!q)
			 cout << "NO" << endl;
     }

     return 0;
}