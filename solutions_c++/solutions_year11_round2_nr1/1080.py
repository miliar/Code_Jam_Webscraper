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
#include <cstdio>
#include <ctime>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("3l.out", "w", stdout);

	int t; cin>>t;
	int n, w[100], l[100];
	long double wp[100], owp[100], oowp[100];
	char s[100][100];
	for (int k=1; k<=t; k++) {
		cin>>n;
		for (int i=0; i<n; i++) {
			w[i]=l[i]=0;
			for (int j=0; j<n; j++) {
				cin>>s[i][j];
				if (s[i][j]=='1') w[i]++;
				if (s[i][j]=='0') l[i]++;
			}
			wp[i] = 1.0*w[i]/(w[i]+l[i]);
		}
		for (int i=0; i<n; i++) {
			owp[i]=0;
			for (int j=0; j<n; j++) {
				if (s[i][j]=='1') owp[i] += 1.0*(w[j])/(w[j]-1+l[j])/(w[i]+l[i]);
				if (s[i][j]=='0') owp[i] += 1.0*(w[j]-1)/(w[j]+l[j]-1)/(w[i]+l[i]);
			}
		}

		printf("Case #%d:\n",k);
		for (int i=0; i<n; i++) {
			oowp[i]=0;
			for (int j=0; j<n; j++) {
				if (s[i][j]!='.') oowp[i] += owp[j]/(w[i]+l[i]);
			}
			cout<<wp[i]/4+owp[i]/2+oowp[i]/4<<endl;
		}
	}

	return 0;
}
