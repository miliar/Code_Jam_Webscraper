#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstdio>
using namespace std;

int N;
int can[510][22];
string line;
string welcome = "welcome to code jam";

int main()
{
	getline(cin, line);
	istringstream i(line);
	i >> N;
	
	for (int i = 0; i < N; i++) {
		getline(cin, line);
		
		for (int j = 0; j < 510; j++) {
			for (int k = 0; k < 22; k++) {
				can[j][k] = 0;
			}
		}
		
		for (int j = 0; j < (int) line.size(); j++) {
			if (line[j] == welcome[0]) {
				can[j][0] = 1;
			}
		}
		
		for (int l = 0; l < (int) welcome.size() -1; l++) {
			for (int j = 1; j < (int) line.size(); j++) {
				for (int k = 0; k < j; k++) {
					if (can[k][l] && line[j] == welcome[l+1]) {
						can[j][l+1] += can[k][l];
					}
				}
			}
		}
		
		int answ = 0;
		
		for (int j = 0; j < (int) line.size(); j++) {
			answ += can[j][welcome.size()-1];
			answ %= 1000;
		}
		
		printf("Case #%d: %04d\n", i+1, answ);
	}
	return 0;
}
