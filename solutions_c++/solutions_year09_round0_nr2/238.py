#include <iostream>
#include <fstream>

using namespace std;

int height[10100], father[10100];

int find(int);

int main() {
	ifstream fin("B-large.in");
	ofstream fout("B-large.txt");
	int caseNum, h, w;
	fin >> caseNum;
	for (int cases = 1; cases <= caseNum; cases ++) {
		fin >> h >> w;
		for (int i = 0; i < h * w; i++) 
			fin >> height[i];
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++) {
				int now = i * w + j, next, min;
				min = height[now];
				father [now] = -1;
				//north west east south
				if (i > 0) {
					next = now - w;
					if (height[next] < min) {
						min = height[next];
						father[now] = next;
					}
				}
				if (j > 0) {
					next = now - 1;
					if (height[next] < min) {
						min = height[next];
						father[now] = next;
					}
				}
				if (j < w - 1) {
					next = now + 1;
					if (height[next] < min) {
						min = height[next];
						father[now] = next;
					}
				}
				if (i < h - 1) {
					next = now + w;
					if (height[next] < min) {
						min = height[next];
						father[now] = next;
					}
				}
			}
		fout << "Case #" << cases << ": " << endl;
		char name = 'a';
		char ans[10100];
		for (int i = 0; i < h * w; i++)
			ans[i] = ' ';
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				int now = i * w + j, zuxian;
				if (father[now] < 0 && ans[now] == ' ') {
					ans[now] = name;
					name ++;
				} else {
					zuxian = find(now);
					if (ans[zuxian] == ' ') {
						ans[zuxian] = name;
						name ++;
					}
					ans[now] = ans[zuxian];
				}
				fout << ans[now];
				if (j < w - 1) fout << ' ';
			}
			fout << endl;
		}
	}
	fout.close();
	return 0;
}

int find(int now) {
	if (father[now] < 0) return now;
	int ans = find(father[now]);
	father[now] = ans;
	return ans;
}