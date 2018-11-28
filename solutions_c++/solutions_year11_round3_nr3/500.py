#include <iostream>
#include <fstream>

using namespace std;

int T, N, L, H;
int num[104];
int ans;

bool Proc() {
    for (ans = L; ans <= H; ++ans) {
	bool done = true;
	for (int i=0; i<N; ++i) {
	    if (num[i] % ans == 0 ||
		ans % num[i] == 0)
		continue;
	    else { done = false; break; }
	}
	if (done) return true;
    }
    return false;
}

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);

    cin >> T;
    for (int m=0; m<T; ++m) {
	cin >> N >> L >> H;
	for (int i=0; i<N; ++i) {
	    cin >> num[i];
	}
	cout << "Case #" << m+1 <<": ";
	bool done = Proc();
	if (done) cout << ans << endl;
	else cout << "NO" << endl;
    }

    return 0;
}

