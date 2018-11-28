#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <cmath>
using namespace std;

#define FORZ(i,n) for(typeof(n)i=0;i<n;i++)
#define all(x) (x).begin(),(x).end()
#define PB push_back
#define sz size()
#define FF first
#define SS second
typedef vector<int> VI;
typedef pair<int,int> pII;
typedef vector<string> VS;
typedef long long LL;

int main () {
	int T;
	cin >> T;
	
	for (int t = 1 ; t <= T ; t ++) {
		int a, b;
		cin >> a >> b;
		
		map <pII, int> mp;
		
		for (int N = a ; N <= b ; N ++) {
			int n = N;
			ostringstream oss;
			oss << n;
			string str = oss.str();
			if (str.sz == 1)
				continue;
			
			FORZ (i, str.sz) {
				string x = str.substr(0, i + 1);
				string y = str.substr(i + 1);
				string z = y + x;
					
				int p = 0;
				while (p < z.sz && z[p] == '0')
					p ++;
				z = z.substr(p);
				
				istringstream iss (z);
				int m;
				iss >> m;
				if (m >= a && m <= b && str.sz == z.sz && str != z) {
					if (m < n) swap(m, n);
					mp [ pII(m, n) ] = 1;
				}
			}
		}
		
		cout << "Case #" << t << ": " << mp.sz << "\n";
	}
	
	return 0;
}
