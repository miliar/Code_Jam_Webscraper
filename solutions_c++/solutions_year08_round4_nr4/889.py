#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int N;
	cin >> N;
	for(int nacho = 1; nacho <= N; nacho++) {
		string line;
		int K, sol = 100000;
		cin >> K;
		cin >> line;
		vector<int> perm(K);
		for(int i = 0; i < K; i++)
			perm[i] = i;
		do {
			string temp = line;
			for(int j = 0; j < line.size(); j += K)
				for(int i = 0; i < K; i++)
					temp[j+i] = line[j+perm[i]];
			
			int s = 0;
			int i = 0;
			while(i < temp.size()) {
				s++;
				char c = temp[i];
				while(i < temp.size()) {
					if(temp[i] != c)
						break;
					i++;
				}
			}
			sol = min(sol, s);
		} while(next_permutation(perm.begin(), perm.end()));
	
		cout << "Case #" << nacho << ": " << sol << endl;
	}
	
	return 0;
}
