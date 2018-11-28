#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
using namespace std;

void getData(ifstream & infile,int & S,int & Q,vector<string> & engines,vector<string> & queries){
	string temp;
	infile>>S;
	getline(infile,temp);
	for (int i=1;i<=S;i++){
		getline(infile,temp);
		engines.push_back(temp);
	}
	infile>>Q;
	getline(infile,temp);
	for (int i=1;i<=Q;i++){
		getline(infile,temp);
		queries.push_back(temp);
	}
}

int calc(int S,int Q,vector<string> & engines,vector<string> & queries){
	set<string> temp;
	int t=0;
	if (queries.empty()) t++;
	while (!queries.empty()){
		temp.clear();
		while (!queries.empty()&&temp.size()<S){
			temp.insert(queries.front());
			if (temp.size()<S) queries.erase(queries.begin());
		}
		t++;
	}
	return t-1;
}

int main(){
	int N;
	int S;
	int Q;
	vector<string> engines;
	vector<string> queries;
	ifstream infile("A-small.in");
	ofstream outfile("A-small.out");

	infile>>N;
	for (int i=1;i<=N;i++){
		engines.clear();
		queries.clear();
		getData(infile,S,Q,engines,queries);
		outfile<<"Case #"<<i<<": "<<calc(S,Q,engines,queries)<<endl;
	}
	return 0;
}