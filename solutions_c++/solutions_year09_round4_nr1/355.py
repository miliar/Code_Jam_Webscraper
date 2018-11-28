#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <assert.h>
using namespace std;

int t,n;
string s[1000];
int a[1000];

int main()
{
 ifstream cin("data.in");
 ofstream cout("dataL.out");
 cin >> t;
 for (int T=1; T<=t; T++) {
	 cin >> n;
	 for (int i=0; i<n; i++)
		 cin >> s[i];
	 for (int i=0; i<n; i++) {
		 a[i] = 0;
		 for (int j=0; j<s[i].length(); j++)
			 if (s[i][j] == '1')
				 a[i] = j+1;
	 }
	  int ans = 0;
		 for (int j=0; j<n; j++) {
			 int k=j;
			 while (a[k] > j+1) k++;
			 for (int l=k; l>j; l--) {
				 swap(a[l], a[l-1]);
				 ans++;
			 }
		 }
	cout << "Case #" << T << ": " << ans << endl;
 }
 
 return 0;
}