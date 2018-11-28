//#include <iostream>
#include <fstream>
using namespace std;
ifstream cin;
ofstream cout;
int recpow(int x, int po) {
	if (po == 1) return x;
	if (po == 0) return 1;
	int sx = recpow(x,po/2);
	if (po%2 == 0) return sx*sx; else return sx*sx*x;
}
int main() {
	cin.open("A-large.in");
	cout.open("A-large.out");
	int T;
	cin >> T;
	int N,K;
	for (int i=1; i<=T; i++){
	cin >> N >> K;
	cout << "Case #" << i << ": ";
	int ls = recpow(2,N);
	if (K%ls == ls-1) { cout << "ON"; } else { cout << "OFF"; }
	cout << endl;
	}
}