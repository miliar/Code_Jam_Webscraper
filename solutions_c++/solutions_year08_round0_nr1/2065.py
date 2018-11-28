#include <iostream>
#include <string>
#include <map>

using namespace std;

map<string, int> engines;
int dynarray[100];

int main() {
	int N;
	string engine;
	cin >> N;
	getline(cin, engine);
	for (int i = 0; i < N; i++) {
		int S;
		cin >> S;
		getline(cin, engine);
		for (int j = 0; j < S; j++) {
			getline(cin, engine);
			engines[engine] = j;
			dynarray[j] = 0;
		}
		int Q;
		cin >> Q;
		getline(cin, engine);
		for (int j = 0; j < Q; j++) {
			getline(cin, engine);
			int e = engines[engine];
			dynarray[e] = 1000000;
			for (int k = 0; k < S; k++)
				if (dynarray[k]+1 < dynarray[e]) dynarray[e] = dynarray[k]+1;
		}
		int min = 1000000;
		for (int j = 0; j < S; j++)
			if (dynarray[j] < min) min = dynarray[j];
		cout << "Case #" << (i+1) << ": " << min << endl;
	}
}
