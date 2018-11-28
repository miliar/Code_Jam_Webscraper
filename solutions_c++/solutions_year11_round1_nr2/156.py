/*
ID: Plagapong
LANG: C++
TASK: B
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#define INF 999999999

using namespace std;
ifstream fin;
ofstream fout;

int n, m;
string word[11][10005];
int ord[11][10005];
int wtop[11];
int cnt[11][10005][26];
int ok[2][10005], otop[2];

void clearVars() {
  // Clear variables
  fill(wtop, wtop + 11, 0);
  for (int i = 1; i <= 10; i++) {
	for (int j = 0; j < 10005; j++) {
	  for (int k = 0; k < 26; k++) {
		cnt[i][j][k] = 0;
	  }
	}
  }
}

void process() {
  // Code here!
  fin >> n >> m;
  string temp;
  for (int i = 0; i < n; i++) {
	fin >> temp;
	int l = temp.length();
	word[l][wtop[l]] = temp;
	ord[l][wtop[l]] = i;
	wtop[l]++;
  }
  // Count!
  for (int l = 1; l <= 10; l++) {
	for (int i = 0; i < wtop[l]; i++) {
	  for (int j = 0; j < l; j++) {
		cnt[l][i][word[l][i][j] - 'a'] += (1 << j);
	  }
	}
  }
  // Action!
  for (int i = 0; i < m; i++) {
	string liz;
	fin >> liz;
	int maxLose = -1, maxOrder = INF;
	string maxWord;
	for (int l = 1; l <= 10; l++) {
	  for (int i = 0; i < wtop[l]; i++) {
		int lose = 0;
		otop[0] = otop[1] = 0;
		for (int j = 0; j < wtop[l]; j++) {
		  ok[1][otop[1]++] = j;
		}
		for (int j = 0; j < 26; j++) {
		  int alpha = liz[j] - 'a';
		  int thisSignature = cnt[l][i][alpha];
		  otop[j&1] = 0;
		  bool choose = false;
		  for (int k = 0; k < otop[1-(j&1)]; k++) {
			// only the ones with same signature should come out
			if (cnt[l][ok[1-(j&1)][k]][alpha])
			  choose = true;
			if (cnt[l][ok[1-(j&1)][k]][alpha] == thisSignature) {
			  ok[j&1][otop[j&1]++] = ok[1-(j&1)][k];
			}
		  }
		  // cout << otop[j&1] << " : " <<  otop[1-(j&1)] << endl;
		  // If same set, do nothing
		  if (choose) {
			//cout << liz[j] << " " << otop[j&1] << " " << thisSignature << endl;
			if (thisSignature == 0) lose++;
		  }
		}
		//cout << word[l][i] << " -- " << lose << endl;
		if (lose > maxLose || (lose == maxLose && ord[l][i] < maxOrder)) {
		  maxLose = lose;
		  maxWord = word[l][i];
		  maxOrder = ord[l][i];
		}
	  }
	}
	fout << " " << maxWord;
	// cout << maxWord << " " << maxLose << endl;
  }
}

int main(int argc, const char* argv[]) {
  if (argc != 3) {
	cout << "Please indicate input and output" << endl;
	exit(0);
  }
  fin.open(argv[1]);
  fout.open(argv[2]);
  int times;
  fin >> times;
  for (int i = 1; i <= times; i++) {
	fout << "Case #" << i << ":";
	clearVars();
	process();
	fout << endl;
  }
  fin.close();
  fout.close();
  return 0;
}
