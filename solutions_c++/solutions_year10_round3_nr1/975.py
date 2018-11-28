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
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
//	freopen("A.in","r",stdin);freopen("A.out","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int T,N;
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> N;
		int knots=0;
		vector <int> X(N), Y(N);
		for (int i=0; i<N; i++) cin >> X[i] >> Y[i];
		for (int i=0; i<N;i++) {
			for (int j=0; j<N; j++) {
				if (X[i] < X[j] && Y[i] > Y[j]) knots++;
				if (X[i] > X[j] && Y[i] < Y[j]) knots++;
			}
		}
		knots=knots/2;
		cout << "Case #" << t << ": " << knots << endl;
	}

}