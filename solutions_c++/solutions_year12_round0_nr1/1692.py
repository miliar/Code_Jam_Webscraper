#include <iostream>
using namespace std;

int main(void) {
	int T;
	string G;
	
	char translations[] = {
		'y', // a
		'h', // b
		'e', // c
		's', // d
		'o', // e
		'c', // f
		'v', // g
		'x', // h
		'd', // i
		'u', // j
		'i', // k
		'g', // l
		'l', // m
		'b', // n
		'k', // o
		'r', // p
		'z', // q
		't', // r
		'n', // s
		'w', // t
		'j', // u
		'p', // v
		'f', // w
		'm', // x
		'a', // y
		'q', // z	
	};
	
	cin >> T;
	getline(cin, G);
	for(int numCase = 1; numCase <= T; numCase++) {
		getline(cin, G);
		
		for(size_t i = 0; i < G.size(); i++) {
			if (G[i] != ' ') {
				G[i] = translations[G[i] - 'a'];
			}
		}
		
		cout << "Case #" << numCase << ": " << G << endl;
	}
}
