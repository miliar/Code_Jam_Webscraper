// SavingTheUniverse.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//
#include <stdio.h>
#include <vector>
#include <string>
#include <set>
#include <iostream>
#include <sstream>
#include <algorithm>

using namespace std;
int main(int argc, char* argv[])
{
	string s;

	int N;
	getline(cin, s);
	istringstream ss(s);
	ss >> N;

	for(int c = 0; c < N; c++) {
		int count = 0;
		int S;
		getline(cin, s);
		ss.clear();
		ss.str(s);
		ss >> S;

		vector<string> engines;
		for(int i=0; i<S;i++){
			getline(cin, s);
			engines.push_back(s);
		}

		int Q;
		getline(cin, s);
		ss.clear();
		ss.str(s);
		ss >> Q;
		set<int> flags;
		for(int k=0;k<Q;k++){
			getline(cin, s);
			vector<string>::iterator i = find(engines.begin(), engines.end(), s);
			int v = i-engines.begin();
			set<int>::iterator j = flags.find(v);
			if(j==flags.end()){
				flags.insert(v);
				if(flags.size()==S){
					count++;
					flags.clear();
					flags.insert(v);
				}
			}

		}
		printf("Case #%d: %d\n",c+1,count);
	}

	return 0;
}

