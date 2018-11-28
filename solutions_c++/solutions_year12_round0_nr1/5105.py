#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<cmath>

using namespace std;

int main(){

	string keys = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvyeqz";
	string vals = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupaozq";
	map<char,char> dict;
	for (int i = 0; i < keys.length(); i++){
		dict[keys[i]] = vals[i];
		dict[' '] = ' ';
	}
	
	string line;
	getline(cin, line);
	stringstream ss(line);
	int N = atoi(line.c_str());
	for (int i = 0; i < N; i++){
		getline(cin, line);
		for (int j = 0; j < line.length(); j++){
			line[j] = dict[line[j]];
		}
		cout << "Case #" << i+1 << ": ";
		cout << line << endl;
	}
	return 0;
}