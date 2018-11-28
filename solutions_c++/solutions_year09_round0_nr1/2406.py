#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int C = 0;
int L = 0;
int D = 0;
char words[5000][15];
bool Q[15][26];

void fillQ()
{
	string word;
	bool in = false;

	memset(Q, false, sizeof(Q));
	cin >> word;

	int lth = 0;
	for(int i = 0; i < word.length(); i++)
	{
		char ch = word.at(i);
		int index = ch - 'a';
		if(ch == '(')
			in = true;
		else if(ch == ')') {
			in = false;
			++lth;
			}
		else if(in)
			Q[lth][index] = true;
		else {
			Q[lth][index] = true;
			++lth;
		}
	}
}

int play()
{
	fillQ();

	int matchNum = 0;
	int index = 0;
	bool matchFlag;
	for(int i = 0; i < D; ++i) {
		matchFlag = true;
		for(int j = 0; j < L; ++j) {
			char ch = words[i][j];
			index = ch - 'a';
			if(!Q[j][index]){
				matchFlag = false;
				break;
			}
		}
		if(matchFlag)
			++matchNum;
	}
	return matchNum;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	cin >> L; cin >> D; cin >> C;

	for(int i = 0; i < D; ++i)
		for(int j = 0; j < L; ++j)
			cin >> words[i][j];

	for(int i = 1; i <= C; i++)
		cout << "Case #" << i << ": " << play() << endl;

	return 0;
}

