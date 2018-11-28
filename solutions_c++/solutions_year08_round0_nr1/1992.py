#include <map>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
int N, S, Q;
int memo[1001][101];
int switches(const vector<int> &queries, int pos, int current_engine) {
	//fout<<"Pos: "<<pos<<" engine: "<<current_engine<<endl;
	if(memo[pos][current_engine]!=-1) return memo[pos][current_engine];
	
	if(pos>=queries.size()) memo[pos][current_engine] = 0;
	else if(queries[pos]!=current_engine) 
		memo[pos][current_engine] = switches(queries, pos+1, current_engine);
	else {
		int answer=99999999;
		for(int i=0;i<S;i++) {
			if(i!=current_engine)
				answer=min(answer, 1+switches(queries, pos+1, i));
		}
		memo[pos][current_engine] = answer;
	}
	return memo[pos][current_engine];
}

int main() {
	ifstream fin( "A-large.in" );
    ofstream fout( "universe_output.txt", ios::trunc );
	map<string, int> names;
	string line;
	char buffer[1000];
	fin>>N;
	
	
	for(int test=0;test<N;test++) {
		fin>>S;
		fin.getline(buffer,1000);
		for(int i=0;i<S;i++) {
			fin.getline(buffer, 1000);
			names[line.assign(buffer)]=i;
		}
	
		fin>>Q;
		fin.getline(buffer, 1000);
		vector<int> queries;
		for(int i=0;i<Q;i++) {
			fin.getline(buffer, 1000);
			queries.push_back(names[line.assign(buffer)]);
		}
		int answer=99999999;
		memset(memo, -1, sizeof memo);
		for(int i=0;i<S;i++) {
			answer=min(answer, switches(queries, 0, i));
		}
		fout<<"Case #"<<test+1<<": "<<answer<<endl;
	//	for(int i=0;i<S;i++) {
	//		for(int j=0;j<Q;j++) fout<<memo[j][i];
	//		fout<<endl;
	//	}
	}
	
}
