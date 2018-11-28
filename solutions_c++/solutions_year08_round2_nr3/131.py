#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef int resulttype;

int next[1000000];
int sorted[1000000];
void skipEOL() { string foo; getline(cin,foo); }
resulttype OneCase() {
	cerr << "ONE CASE" << endl;

	int K;

	cin >> K;

	next[K] = K;
	int head = K;
	int count = 1;
	for (int T=K-1; T>0; --T) {
		// walkback T+1  = Walk ahead -(T+1) % count  (and one more)
		int steps = (count-((T+1) % count)) % count;
		//cerr << "walk ahead " <<  steps << endl;
		while (steps >0) {
			head = next[head]; --steps;
		}
		//cerr << "ins " << T << " between " << head << " and " << next[head] << endl;// insert T before next
		next[T] = next[head];
		next[head] = T;
		head = T;
		++count;
	}
	for (int i=0; i<K; ++i) {
		sorted[i] = head;
		head = next[head];
	}
	int n;
	cin >> n;

	for (int i=0; i<n; ++i) {
		int di;
		cin >> di;
		cout << " " << sorted[di-1];
	}
	return -1;
}

int main() {
	int Anz;
	cin >> Anz;
	skipEOL();
	for (int run=1; run<=Anz; ++run) {
		cout << "Case #" << run << ":";
		resulttype result = OneCase();

		cout << endl;
	}
	return 0;
};
