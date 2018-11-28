#include <iostream>
#include <fstream>
using namespace std;

#define Orange 0
#define Blue 1

struct instruct {
	char c;
	int no;
} I[500];

int main() {
	int unuse[2], time[2], pos[2], n, t, Walk;
	bool tmp;
	
	ifstream fin("input.txt");
	ofstream fout("ans.txt");
	fin >> t;
	for (int x = 1; x <= t; x++) {
		fin >> n;
		for (int y = 0; y < n; y++)
			fin >> I[y].c >> I[y].no;
		if (n == 0) {
			fout << "Case #" << x << ": 0\n";
			continue;
		}
		
		// Initialization
		tmp = (I[0].c == 'B');
		Walk = I[0].no - 1;
		unuse[!tmp] = Walk + 1;
		unuse[tmp] = 0;
		time[!tmp] = 0;
		time[tmp] = Walk + 1;
		pos[!tmp] = 1;
		pos[tmp] = I[0].no;
		
		for (int i = 1; i < n; i++) {
			tmp = (I[i].c == 'B');
			if (I[i].c == I[i-1].c) {
				Walk = abs(I[i].no - pos[tmp]);
				unuse[!tmp] += Walk + 1;
			}
			else {
				Walk = max(abs(I[i].no - pos[tmp]) - unuse[tmp], 0);
				unuse[tmp] = 0;
				unuse[!tmp] = Walk + 1;
			}
			time[tmp] += Walk + 1;
			pos[tmp] = I[i].no;
//			printf("After instruction %d, time[O] = %d, time[B] = %d, unuse[O] = %d, unuse[B] = %d, pos[O] = %d, pos[B] = %d\n", i, time[0], time[1], unuse[0], unuse[1], pos[0], pos[1]);
		}
		fout << "Case #" << x << ": " << (time[0]+time[1]) << "\n";
	}
}
