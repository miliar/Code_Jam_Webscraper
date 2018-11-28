#include <iostream>
#include <algorithm>
#include <math.h>
#include <set>
#include <iomanip>
using namespace std;

int x[2001];
int h[2001];
int N;

bool solve(int i, int j)
{
	if (i == j || i == j-1)
		return true;

	int m = i+1;
	if (x[m] > j) {
		return false;
	}

	while (x[m] != j) {
		if (x[m] > j) {
			return false;
		}
		m = x[m];
	}

//	} else if (m == x[i]) {
//		h[i+1] = h[i]-1;
//		solve(i+1,j);
//		return true;
//	} else {
//		h[m] = min(h[j],h[i])-1;
//		int hh = h[x[j]];
//		h[m] = min(h[m],h[j]+(hh-h[j])*(j-m)/(x[j]-j));

//		h[i+1] = h[m] - 1 - (i+1-m)/(m-j);


		h[m]--;
		for (int k=i+1; k<m; k++) {
			h[k] = h[m]+(h[m]-h[j])*(k-m)/(m-j);
		}
		if (!solve(i,m))
			return false;
		for (int k=m+1; k<j; k++) {
			h[k] = h[m]+(h[m]-h[j])*(k-m)/(m-j);
		}
		if (!solve(m,j))
			return false;
		return true;
//	}
	
}

void tst()
{
	cin >> N ;

	for (int i=1; i<=N-1; i++) {
		cin >> x[i];
	}

	for (int i=1; i<=N; i++)
		h[i] = 500000000;

	int idx = 1;
	h[1] = 500000000;
	while (idx <N) {
		h[x[idx]] = 500000000;
		if (!solve(idx,x[idx])) {
			cout << "Impossible";
			return;
		}
		idx = x[idx];
	}

	for (int i=1; i<=N; i++) {
		cout << h[i] << " ";
	}

	return ;
}

int main()
{
    int t;
    cin >> t;
    for(int i=0;i<t;i++) {
		cout << "Case #" << i+1 << ": ";
		tst();
		cout << endl;
	}
}



