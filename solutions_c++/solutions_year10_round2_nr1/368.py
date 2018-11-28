#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int getcount(string d,vector<string>& dir){
	if(d.length() <= 0) return 0;
	vector<string>::iterator it = find(dir.begin(),dir.end(),d);
	if(it != dir.end()) return 0;
	dir.push_back(d);
	int i;
	for(i = d.length() - 1; i >= 0; i--)
		if(d[i] == '/') break;
	return 1 + getcount(d.substr(0,i),dir);
}
int main(){
	ifstream in("input");
	ofstream out("output");
	int cases;
	in >> cases;
	int M,N;


	for(int casenum = 1; casenum <= cases; casenum++){
		out << "Case #" << casenum << ": ";
		cout << "Case " << casenum << endl;
		in >> N >> M;
		vector<string> dir;
		string temp;
		for(int i = 0; i < N; i++){
			in >> temp;
			dir.push_back(temp);
		}
		int cnt = 0;
		for(int i = 0; i < M; i++){
			in >> temp;
			cnt += getcount(temp,dir);
		}
		out << cnt << endl;


	}
	return 0;
}
