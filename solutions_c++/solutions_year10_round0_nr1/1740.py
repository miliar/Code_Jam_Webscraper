//: Piotr Skotnicki
// Google Code Jam 2010
// Qualification Round - A
#include <iostream>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<=(b);++i)

void solve() {
    int N, K;
    cin >> N >> K;
    int p = (1 << N);
    if(K % p == p-1)
    	cout << "ON";
    else
		cout << "OFF";
}

int main(int argc, char* argv[]) {	
	ios_base::sync_with_stdio(false);

#define TASK "A"

//#define OWN 1
//#define SMALL 1
#define LARGE 1
	
#if OWN
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#elif SMALL
	freopen(TASK"-small-attempt0.in", "r", stdin);
	freopen(TASK"-small.out", "w", stdout);
#elif LARGE
	freopen(TASK"-large.in", "r", stdin);
	freopen(TASK"-large.out", "w", stdout);
#endif

	int T;
	cin >> T;
	FOR(i, 1, T) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	
	fflush(stdout);
	return 0;	
}
