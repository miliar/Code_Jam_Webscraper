#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
#include <iomanip>
#include <fstream>
#include <cstdio>
using namespace std;

int L;
ifstream in("in.txt");
ofstream out("out.txt");

char str[508];
#define MOD 10000

int CNT[508][19];

int main() {
	scanf("%d\n", &L);

	char ch[22] = "welcome to code jam";

	for(int i = 0; i < L; ++i) {
		gets(str);
		memset(CNT, 0, sizeof(CNT));
		for(int j = 0; str[j]; ++j) {
			if(j == 0) {
				if(str[j] == ch[0]) {
					CNT[0][0] = 1;
				}
			} else {
				for(int k = 0; ch[k]; ++k) {
					CNT[j][k] = CNT[j-1][k];
					CNT[j][k] %= MOD;
					if(str[j] == ch[k]) {
						if(k == 0) {
							CNT[j][0] += 1;
						} else {
							CNT[j][k] += CNT[j - 1][k - 1];
						}
					}
				}
			}
		}
		int ans = (CNT[strlen(str) - 1][strlen(ch) - 1] % MOD);
		out << "Case #" << (i+1) << ": " << setw(4) << setfill('0') << ans << endl;
		
	}
	return 0;

}