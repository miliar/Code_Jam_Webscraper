#include <iostream>
#include <stdlib.h>
#include <vector>
#include <string.h>
using namespace std;

int pos[2] = {1,1};
int ptr[2] = {0,0};
int cmd_nums[100];
char cmd_names[100];

int main() {
	int testcases;
	cin >> testcases;
	for (int tc=0;tc<testcases;tc++) {
		char mapCombine[256][256];
		char listOppose[28][2];

		for (int i=0;i<256;i++) {
			for (int j=0;j<256;j++) mapCombine[i][j] = 0;
		}

		int combines;
		cin >> combines;
		for (int i=0;i<combines;i++) {
			char c,d,e;
			cin >> c >> d >> e;
			mapCombine[c][d] = e;
			mapCombine[d][c] = e;
		}
		int opposes;
		cin >> opposes;
		for (int i=0;i<opposes;i++) {
			char c,d;
			cin >> c >> d;
			listOppose[i][0] = c;
			listOppose[i][1] = d;
		}
		
		char line[256] = {0};
		char counts[256] = {0};
		for (int i=0;i<256;i++) counts[i] = 0;
		for (int i=0;i<256;i++) line[i] = 0;
		int chars;
		cin >> chars;
		int pos = 0;
		for (int i=0;i<chars;i++) {
			char c;
			cin >> line[pos];
			counts[line[pos]]++;
			if (line[0]=='I') {
				int asdt =0;
			}
			pos++;
			bool combined = false;
			while (pos>=2) {
				char r = mapCombine[line[pos-1]][line[pos-2]];
				if (r!=0) {
					combined = true;
					counts[line[pos-1]]--;
					counts[line[pos-2]]--;
					pos--;
					line[pos-1] = r;
					counts[r]++;
				} else break;
			}
			if (!combined && pos>=2) {
				for (int p=0;p<opposes;p++) {
					if (counts[listOppose[p][0]] && counts[listOppose[p][1]]) {
						for (int t = 0;t<256;t++) counts[t] = 0;
						pos = 0;
						break;
					}
				}
			}
		}
				
		cout << "Case #" << (tc+1) << ": [";
		for (int i=0;i<pos;i++) {
			if (i==0) {
				cout << line[i];
			} else {
				cout << ", " << line[i];
			}
		}
			
		cout << "]\n";
	}
}