#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <ios>
#include <numeric>
#include <stack>

using namespace std;
ifstream fin;
ofstream fout;
int casenum;
int caseid;

void show(int x){cout << x << " ";}

string task(int casenum){
	// Input part
	int N;
	//cout << "read N:";
	fin >> N;

	vector<vector<int> > M(N+1);
	for (int V = 1; V <= N; ++V) {
		int n;
		//cout << "read n:";
		fin >> n;
		M[V].resize(n);
		for(int j = 0; j < n; ++j){
			//cout << "read Mi's";
			fin >> M[V][j];
		}
	}

	// Business logic
//	vector<int> mark(N+1,0);
//	stack<int> stk;
//	for (int V = 1; V <= N; ++V){
//		//stk = stack<int>();
//		mark = vector<int>(N+1,0);
//		mark[V]=1;
//		stk.push(V);
//		while(!stk.empty()){
//			int v = stk.top(); stk.pop();
//			for(unsigned int j = 0; j < M[v].size();++j){
//				if(mark[M[v][j]]){
//					return " Yes";
//				}else{
//					mark[M[v][j]] = 1;
//					stk.push(M[v][j]);
//				}
//			}
//		}
//	}

	vector<int> mark(N+1,0);
	stack<int> stk;
	int cnt = 0;
	for (int V = 1; V <= N; ++V){
		//stk = stack<int>();
		//mark = vector<int>(N+1,0);
		if(mark[V]) continue;
		mark[V]=++cnt;
		stk.push(V);
		while(!stk.empty()){
			int v = stk.top(); stk.pop();
			for(unsigned int j = 0; j < M[v].size();++j){
				if(mark[M[v][j]]==cnt){
					return " Yes";
				}else{
					mark[M[v][j]] = cnt;
					stk.push(M[v][j]);
				}
			}
		}
	}
	// Output part
	return " No";
}

int main(){

	fin.open("inout/A-large.in");
	fout.open("inout/A-large.out");
	fout.precision(8);

	fin >> casenum;

	for(int caseid=1;caseid <= casenum ;++caseid)
	{
		fout << "Case #" << caseid << ":" << task(caseid) << endl;;

	}

	fout.close();
	fin.close();
	return 0;
}
