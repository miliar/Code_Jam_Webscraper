
#include<iostream>
#include<stdio.h>

#include<string>
#include<vector>

using namespace std;

int compute(const vector<vector<int> >& occur, int i, int j);

int main(int argc, char** argv) {

	int N;
	cin >>	N;
	//cout << N << endl;
	
	char buf[1000];
	cin.getline(buf, 1000);	
	vector<string> lines;

	string word("welcome to code jam");

	for(int i = 0; i < N; i++) {
		cin.getline(buf, 1000);
		string s(buf);

//		cout << s << endl;
		
		vector<vector<int> > occur;
		occur.resize(word.size());
		for(int j = 0; j < occur.size(); j++)
			occur[j].resize(s.size());

		for(int j = 0; j < s.size(); j++){
			for(int k = 0; k < word.size(); k++)
				if(s[j] == word[k])
					occur[k][j] = 1;
				else
					occur[k][j] = 0;
		}

		int num = compute(occur, 0, 0);
		printf("Case #%d: %04d\n", (i+1), num);
	}



	
	return 0;
}

int compute(const vector<vector<int> >& occur, int i, int j){

	if(i == occur.size())
		return 1;
	int num = 0;
	for(int l = j; l < occur[i].size(); l++)
		if(occur[i][l] == 1)
			num += compute(occur, i + 1, l + 1)%10000;

	return num%10000;
}
