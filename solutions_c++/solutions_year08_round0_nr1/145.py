#include <iostream>
#include <map>
#include <vector>
#include <string>
using namespace std;

int main() {
	int N;
	cin >> N;
	
	for(int i = 1; i <= N; ++i) {
		cout << "Case #" << i << ": ";
				
		int S;
		cin >> S;
		string line;
		getline(cin, line);
		
		map<string, int> SE;
		for(int j = 0; j != S; ++j) {
			getline(cin, line);
			SE[line] = j;
		}
		
		int Q;
		cin >> Q;
		getline(cin, line);
		
		vector<int> sw(S, 0);
		int best;
		for(int k = 0; k != Q; ++k) {
			getline(cin, line);
			int se = SE[line];
			
			vector<int> sw2(sw);
			best = 1000000;
			for(int j = 0; j != S; ++j)
				if(sw[j] < best) best = sw[j];
			for(int j = 0; j != S; ++j)
				if(sw[j] == 1000000) sw2[j] = best + 1;
			sw2[se] = 1000000;
			sw.swap(sw2);
		}
		best = 1000000;
		for(int j = 0; j != S; ++j)
			if(sw[j] < best) best = sw[j];
		cout << best << endl;
	}
}
