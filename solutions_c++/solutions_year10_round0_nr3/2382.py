#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
using namespace std;
#define FOR(i,a,b) for(int i=a; i<b; i++)

map<pair<int,int>, int> repetidos;

int main(){
	ifstream in("A-large-practice.in");
	ofstream out("A-large-practice.out");
	int R,k,N,T;
	in >> T;
	for(int t = 0; t<T; t++){
		repetidos.clear();
		in >> R >> k >> N;
		vector<int> g(N);
		for(int i = 0; i<N; i++)
			in >> g[i];

		int indexGroup = 0;
		int usedK;
		int start,finish,win;
		long long tot = 0;
		bool vale = true;
		
		while(R){
			start = indexGroup;
			win = 0; usedK = k;
			vector<bool> recentUsed(N,false);
			while(indexGroup < N && usedK >= g[indexGroup] && !recentUsed[indexGroup]){
				recentUsed[indexGroup] = true;
				usedK -= g[indexGroup];
				win += g[indexGroup];
				indexGroup = (indexGroup + 1)%N;
			}
			finish = indexGroup;
			/*if(repetidos.find(make_pair(start,finish)) != repetidos.end() && vale){
				vale = false;
				int tempR = R;
				long long tempTot = tot;
				if(R>=repetidos.size()){
					int vecesQueEntra = R/repetidos.size();
					tot += tempTot*vecesQueEntra;
					R -= (R/repetidos.size())*(repetidos.size());
					R++;
				}
				else break;
			}
			else*/
				tot += win;
			repetidos[make_pair(start,finish)] = win;
			R--; 
		}
		out << "Case #" << t+1 << ": " << tot << endl;
	}
	
}