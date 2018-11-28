#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int dp[500][20];

int main() {
	//ifstream cin("C-small.in");
	ifstream cin("C-large.in");
	//ofstream cout("c-out");
	freopen("c-out","w",stdout);
	int N, Case;
	int i, j, k;
	string S;
	string L = "welcome to code jam";
	for (cin>>N,getline(cin,S),Case=1; N; N--,Case++) {
		getline(cin,S);
		memset(dp, 0, sizeof(dp));
		int res = 0;
		for (i=0; i<S.length(); i++) {
			if (S[i] == 'w') dp[i][0] += 1;
			for (j=1; j<L.length(); j++) {
				if (S[i] == L[j]) {
					for (k=0; k<S.length(); k++)
						dp[i][j] += dp[k][j-1]%10000;
				}
			}
			res += dp[i][L.length()-1];
		}
		printf("Case #%d: %04d\n",Case,res%10000);
	}

}