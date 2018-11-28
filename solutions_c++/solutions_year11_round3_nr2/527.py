#include <iostream>
#include <fstream>

using namespace std;

const int maxn = 1005;
long long  T, t, L, N, C;
long long  dist[maxn];
long long  ans;

void Proc0() {
    int len = 0;
    int index = 0;
    for (int i=0; i<N; ++i) {
	len += dist[index];
	index = (index == C-1 ? 0 : index+1);
    }
    ans = len * 2;
}

int Calc(int p1, int p2) {
    int temp = 0;
    for (int i=0; i<N; ++i) {
	if (i == p1 || i == p2) {
	    int index = i % C;
	    int tm = dist[index] * 2;
	    if (tm + temp <= t) {
		temp += tm;
	    } else {
		if (temp >= t)
		    temp += dist[index];
		else {
		    int left = t - temp;
		    temp += left;
		    temp += dist[index] - left / 2;
		}
	    }
	}
	else {
	    int index = i % C;
	    int tm = dist[index] * 2;
	    temp += tm;
	}
    }
    return temp;
}

void Proc1() {
    ans = 999999999;
    for (int i=0; i<N; ++i) {
	int temp = Calc(i, i);
	if (temp < ans) ans = temp;
    }
}

void Proc2() {
    ans = 999999999;
    for (int i=0; i<N; ++i)
	for (int j=i+1; j<N; ++j) {
	    int temp = Calc(i, j);
	    if (temp < ans) ans = temp;
	}
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);

    cin >> T;
    for (int m=0; m<T; m++) {
	cin >> L >> t >> N >> C;
	for (int i=0; i<C; ++i)
	    cin >> dist[i];
	if (L == 0) {
	    Proc0();
	} else if (L == 1) {
	    Proc1();
	} else if (L == 2) {
	    Proc2();
	}
	cout << "Case #" << m+1 << ": " << ans << endl;
    }

    return 0;
}
