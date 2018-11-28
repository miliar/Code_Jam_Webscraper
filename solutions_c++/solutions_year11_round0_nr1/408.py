#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int t;// t cases
	fin >> t;
	for (int i = 0 ; i < t; i++) {
		int n;// n buttons
		fin >> n;
		int lastTimeO = 0, lastTimeB = 0, lastPstO = 1, lastPstB = 1, now = 0;
		for (int j = 0 ; j < n; j++) {
			char robot;
			fin >> robot;
			int p;// button p
			fin >> p;
			switch (robot ) {
				case 'O':
					if ( (now - lastTimeO) >= abs(lastPstO - p) ){
						now++;//push
						lastPstO = p;
						lastTimeO = now;
					}
					else {
						now += abs(lastPstO - p) - (now - lastTimeO);//move
						now++;//push
						lastPstO = p;
						lastTimeO = now;
					}
					break;
				case 'B':
					if ( (now - lastTimeB) >= abs(lastPstB - p) ){
						now++;//push
						lastPstB = p;
						lastTimeB = now;
					}
					else {
						now += abs(lastPstB - p) - (now - lastTimeB);//move
						now++;//push
						lastPstB = p;
						lastTimeB = now;
					}
					break;
			}
		}
		fout << "Case #" << i+1 << ": " << now << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
