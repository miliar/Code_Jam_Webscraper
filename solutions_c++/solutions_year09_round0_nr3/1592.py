#include <iostream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

#include <cmath>
#include <cstdio>

typedef unsigned long long ULL;
typedef long long LL;

using namespace std;

int main(void)
{
	int n;
	cin >> n;
	cin.ignore();
	for(int nn = 0; nn < n; ++nn) {
		string s;
		getline(cin, s);
		int sum[520][20];
		for(int i=0;i<520;++i) for(int j=0;j<20;++j) sum[i][j]=0;
		for(int idx = s.size() - 1; idx >= 0; --idx) {
			for(int i=0;i<20;++i) sum[idx][i] = sum[idx+1][i];
			switch(s[idx]) {
			case 'w': // 0
				sum[idx][0] += sum[idx+1][1];
				break;
			case 'e': // 1, 6, 14
				sum[idx][1] += sum[idx+1][2];
				sum[idx][6] += sum[idx+1][7];
				sum[idx][14] += sum[idx+1][15];
				break;
			case 'l': // 2
				sum[idx][2] += sum[idx+1][3];
				break;
			case 'c': // 3, 11
				sum[idx][3] += sum[idx+1][4];
				sum[idx][11] += sum[idx+1][12];
				break;
			case 'o': // 4, 9, 12
				sum[idx][4] += sum[idx+1][5];
				sum[idx][9] += sum[idx+1][10];
				sum[idx][12] += sum[idx+1][13];
				break;
			case 'm': // 5, 18
				sum[idx][5] += sum[idx+1][6];
				sum[idx][18] += 1;
				break;
//			case 'e': // 6
			case ' ': // 7, 10, 15
				sum[idx][7] += sum[idx+1][8];
				sum[idx][10] += sum[idx+1][11];
				sum[idx][15] += sum[idx+1][16];
				break;
			case 't': // 8
				sum[idx][8] += sum[idx+1][9];
				break;
//			case 'o': // 9
//			case ' ': // 10
//			case 'c': // 11
//			case 'o': // 12
			case 'd': // 13
				sum[idx][13] += sum[idx+1][14];
				break;
//			case 'e': // 14
//			case ' ': // 15
			case 'j': // 16
				sum[idx][16] += sum[idx+1][17];
				break;
			case 'a': // 17
				sum[idx][17] += sum[idx+1][18];
				break;
//			case 'm': // 18
			
			}
			for(int i=0;i<20;++i) sum[idx][i] %= 10000;
		}
		printf("Case #%d: %04d\n", nn+1, sum[0][0] % 10000);
	}
	
	return 0;
}
