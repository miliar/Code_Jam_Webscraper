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

int n;
string s[200];
double wp[200], owp[200], oowp[200], wwp[200][200];

int main()
{
     freopen("input.txt", "r", stdin);
     freopen("output.txt", "w", stdout);

     int NTests;
     cin >> NTests;

     for (int test = 0; test < NTests; test++)
     {
		 cin >> n;
		 for (int i = 0; i < n; i++)
			 cin >> s[i];
		 for (int i = 0; i < n; i++)
		 {
			 double k = 0;
			 wp[i] = 0;
			 int r = 0;
			 for (int j = 0; j < n; j++)
				 if (s[i][j] == '1')
					 k++;
				 else if (s[i][j] == '0')
					 r++;
			 if (k+r > 0)
				wp[i] = k/(k+r);
			 for (int j = 0; j < n; j++)
			 {
				 wwp[i][j] = 0;
				 if (s[i][j] == '1' && k+r-1 > 0)
					 wwp[i][j] = (k-1)/(k+r-1);
				 else if (s[i][j] == '0' && k+r-1 > 0)
					 wwp[i][j] = k/(k+r-1);
			 }
		 }

		 for (int i = 0; i < n; i++)
		 {
			 owp[i] = 0;
			 int k = 0;
			 for (int j = 0; j < n; j++)
				 if (s[i][j] != '.')
				 {
					 owp[i] += wwp[j][i];
					 k++;
				 }
			if (k > 0)
				owp[i] /= k;
		 }

		 for (int i = 0; i < n; i++)
		 {
			 int k = 0;
			 oowp[i] = 0;
			 for (int j = 0; j < n; j++)
				 if (s[i][j] != '.')
				 {
					oowp[i] += owp[j];
					k++;
				 }
			if (k > 0)
				oowp[i] /= k;
		 }

		 cout << "Case #" << test + 1 << ": " << endl;
		 for (int i = 0; i < n; i++)
			 printf("%.10f\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
     }

     return 0;
}