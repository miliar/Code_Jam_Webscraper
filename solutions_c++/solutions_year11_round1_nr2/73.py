#include <iostream>
#include <cstring>

using namespace std;

const int POW[11] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};

char dic[10000][11];
int lenth[10000];

void cal(int group[], int count, char cmd[], int index, int score[]) {
	int num[10000] = {0};
	int flag[10000] = {0};
	int exists = 0;
	if (index == 26) {
		return;
	}
	int newgroup[10000] = {0};
	for(int i = 0; i < count; i++) {
		int cword = group[i];
		for(int j = 0; j < lenth[cword]; j++) {
			if (dic[cword][j] == cmd[index]) {
				num[i] += POW[j];
				exists = 1;
			}
		}
	}
	if (exists == 0) cal(group,count,cmd,index+1,score);
	else {
		for(int i = 0; i < count; i++) {
			if (num[i] == 0) score[group[i]]++;
			if (!flag[i]) {
				int newcount = 0;
				for(int j = i; j < count; j++) {
					if (num[j] == num[i]) {
						flag[j] = 1;
						newgroup[newcount++] = group[j];
					}
				}
				if (count > 1) cal(newgroup, newcount, cmd, index+1, score);
			}
		}
	}
}

int main (int argc, char const *argv[])
{
	int t;
	cin >> t;
	for(int index = 1; index <= t; index++) {
		int n, m;
		cin >> n >> m;
		for(int i = 0; i < n; i++) {
			cin >> dic[i];
			lenth[i] = strlen(dic[i]);
		}
		char cmd[30];
		int order[26];
		cout << "Case #" << index << ":";
		for(int i = 0; i < m; i++) {
			cin >> cmd;
			int score[10000] = {0};
			int flag[10000] = {0};
			int group[10000] = {0};
			for(int j = 0; j < n; j++) {
				if (!flag[j]) {
					int count = 0;
					for(int k = j; k < n; k++) {
						if (lenth[k] == lenth[j]) {
							flag[k] = 1;
							group[count++] = k;
						}
					}
					if (count > 1)
						cal(group, count, cmd, 0, score);
				}
			}
			int max = -1;
			int ii = 0;
			for(int j = 0; j < n; j++) {
				if (max < score[j]) {
					max = score[j];
					ii = j;
				}
			}
			cout << " " << dic[ii];
		}
		cout << endl;
	}
	return 0;
}