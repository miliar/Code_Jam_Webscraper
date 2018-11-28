/*
 * A.cpp
 *
 *  Created on: May 22, 2010
 *      Author: lsyl
 */
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <algorithm>
#include <string>
#include <cmath>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <cstring>


using namespace std;

#define REP(i, n) for((i)=0; (i)<(int)(n); (i)++)
#define REP2(i, n) for((i)=1; (i)<=(int)(n); (i)++)
#define REP3(i, n) for((i)=(int)(n)-1; (i)>=0; (i)--)

ifstream fin("A-large.in");
ofstream fout("A-large.out");



void Solve(int cn){
	set<string> exit;
	string given[100];
	int i,j;
	int N, M;
	int cnt=0;
	fin >> N >> M;
	string tmp;
	getline(fin, tmp);
	REP(i, N) {
		//string tmp; char ch;
		getline(fin, tmp);
		//cerr << tmp << endl;
		int s=1; string t;
		while(s<tmp.size()) {
			//string t;
			t+=tmp[s];
			if(tmp[s]=='/'||s==tmp.size()-1){
				if(s==tmp.size()-1) t+='/';
				exit.insert(t);
				//cerr << t << endl;
			}
			s++;
			//else {
				//exit.insert(tmp);
			//}
			//s++;
		//}

	}
	}
	//check
	//REP(i, N){

	//}
	//int cnt=0;
	REP(i, M) {
		//string tmp;
		getline(fin, tmp);
		//cerr << tmp << endl;
				int s=1; string t;
				while(s<tmp.size()) {
					//string t;
					t+=tmp[s];
					if(tmp[s]=='/'||s==tmp.size()-1) {
					//else {
						if(s==tmp.size()-1) t+='/';
						pair<set<string>::iterator, bool> pr;
						//cerr << t << endl;
						pr = exit.insert(t);
						if(pr.second) cnt++;
					}
					s++;
				}
	}

	//REP(i, M){

	//		pair<set<string>::iterator, bool> pr;
	//		pr = exit.insert(given[i]);

	//		if(pr.second){
	//		cnt++;

	//	}
	//}




	fout << "Case #" << cn << ": " << cnt <<endl;

}

int main() {
    //ifstream fin("A-small.in");
    //ofstream fout("A-small.out");

    int CASES, i;
    fin >> CASES;
    REP2(i, CASES) Solve(i);
    return 0;
}
