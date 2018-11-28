#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

const int SIZE = 1010;
int N, arr[SIZE];

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	//freopen("C-small-attempt0.in", "rt", stdin);
	//freopen("C-small-attempt0.out", "wt", stdout);
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		//cerr << "Solving testcase " << t+1 << endl;

		cin >> N;
		int x = 0, s = 0, mi = 1e9;
		for(int i = 0 ; i < N ; i++){
			cin >> arr[i];
			x ^= arr[i];
			s += arr[i];
			mi <?= arr[i];
		}

		cout << "Case #" << t+1 << ": ";

		if(x)
			cout << "NO" << endl;
		else
			cout << s-mi << endl;
	}

	return 0;
}
