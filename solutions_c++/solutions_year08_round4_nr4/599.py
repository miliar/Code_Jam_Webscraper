#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <set>
#include <iterator>
#include <map>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
	int C;
	cin >> C;
	for (int c=0;c<C;c++) {

		cout << "Case #" << c+1 << ": ";
	
		int k;
		string s;
		
		cin >> k >> s;

		vector<int> perm(k);
		for (int i=0;i<k;i++) perm[i]=i;
		
		int minRLE = INT_MAX;
		
		do {
			char c[s.length()];
			for (int i=0;i<s.length(); i+=k) {
				for (int j=0;j<k;j++) c[i+j]=s[i+perm[j]];
			}
			
			int rle = 1;
			for (int i=1;i<s.length();i++) {
				if (c[i] != c[i-1]) rle++;
			}
			
			minRLE = min(rle, minRLE);
		} while (next_permutation(perm.begin(),perm.end()));

		cout << minRLE << endl;
	}
}
