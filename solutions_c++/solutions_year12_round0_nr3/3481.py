#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

bool checked[2000000];

int main() {
    ofstream fout ("QC.out");
    ifstream fin ("QC.in");
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		int A,B;
		fin >> A >> B;
		if (A < 10 || A == B) {
			fout << "Case #" << t << ": " << 0 << endl;
			continue;
		}
		for (int i = 0; i < 2000000; i++) checked[i] = false;
		int length = 0;
		for (length = 0; A/pow(10.,length) >= 1; length++);
		int answer = 0;
		for (int i = A; i <= B; i++) {
			if (checked[i]) continue;
			checked[i] = true;
			vector<int> number;
			for (int j = 0; j < length; j++) {
				number.push_back(i/(int)pow(10.,j)%10);
			}
			int temp = number[0];
			number.erase(number.begin());
			number.push_back(temp);
			int count = 0;
			while (true) {
				int n = 0;
				for (int j = 0; j < length; j++) n+=(int)pow(10.,j)*number[j];
				if (A <= n && n <= B){
					if (checked[n]) break;
					count++;
					checked[n] = true;
				}
				temp = number[0];
				number.erase(number.begin());
				number.push_back(temp);
			}
			answer += count*(count+1)/2;
		}
		fout << "Case #" << t << ": " << answer << endl;
	}
    return 0;
}