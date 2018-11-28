#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	ifstream fin("input.in");
	ofstream fout("output.out");
	int t;
	fin >> t;
	for(int i = 1; i <= t; i++){
		int n; fin >> n;
		vector<pair<char, int>> v(n);
		for(int j = 0; j < n; j++){
			char c; int p;
			fin >> c >> p;
			v[j] = make_pair(c,p);

		}
		int opos = 1, bpos = 1, time = 0, done = 0;
		int nexto = -1, nextb = -1;
		while (done < v.size()){
			if(nexto < done)
				do{
					nexto++;
				} while(nexto < v.size() && v[nexto].first != 'O' || nexto < done);
			if(nextb < done)
				do{
					nextb++;
				} while(nextb < v.size() && v[nextb].first != 'B' || nextb < done);
			if(v[done].first == 'O'){
				if(v[done].second == opos){
					done++;
				} else if(v[done].second > opos){
					opos++;
				} else if(v[done].second < opos){
					opos--;
				}
				if(nextb != v.size() && bpos < v[nextb].second) bpos++;
				if(nextb != v.size() && bpos > v[nextb].second) bpos--;
			} else if(v[done].first == 'B'){
				if(v[done].second == bpos){
					done++;
				} else if(v[done].second > bpos){
					bpos++;
				} else if(v[done].second < bpos){
					bpos--;
				}
				if(nexto != v.size() && opos < v[nexto].second) opos++;
				if(nexto != v.size() && opos > v[nexto].second) opos--;
			}
			time++;
		}
		fout << "Case #" << i << ": " << time << endl; 
	}
}