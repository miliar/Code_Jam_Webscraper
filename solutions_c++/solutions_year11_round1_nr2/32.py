#include <bitset>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <utility>
#include <deque>
#include <vector>
#include <list>
#include <queue>
#include <string>
using namespace std;
ofstream fout("B-large.out");
ifstream fin("B-large.in");
bool l(vector<int> a, vector<int> b){
	return lexicographical_compare(a.begin(), a.end(), b.begin(), b.end());
}
int main(){
	int T;
	fin >> T;
	for(int s=0;s<T;s++){
		int N, M;
		fin >> N >> M;
		string D[N];
		for(int i=0;i<N;i++){
			fin >> D[i];
		}
		fout << "Case #"<< s+1 << ":";
		for(int i=0;i<M;i++){
			int order[26];
			for(int j=0;j<26;j++){
				char c;
				fin >> c;
				order[c - 'a'] = j;
			}
			vector<int> id[N];
			
			for(int j=0;j<N;j++){
				id[j] = vector<int>(28, 0);
				id[j][0] = D[j].length();
				
				for(int k=0;k<id[j][0];k++){
					char x = D[j][k];
					id[j][order[x - 'a'] + 1] += (1 << k);
				}
				id[j][27] = j;
			}
			sort(id, id+N, l);
			
			bool split[N];
			int score[N];
			for(int j=0;j<N;j++){
				split[j] = false;
				score[j] = 0;
			}
			split[N-1] = true;
			for(int j=0;j<27;j++){
				for(int k=0;k<N-1;k++){
					if(!split[k] && id[k][j] != id[k+1][j]){
						if(id[k][j] == 0){
							int l = k;
							while(!split[l]){
								score[l] ++;
								l--;
							}
						}
						split[k] = true;
					}
				}
			}
			int mscore = 0;
			int mindex = 0;
			for(int j=0;j<N;j++){
				if(score[j] > mscore || score[j] == mscore && id[j][27] < mindex){
					mindex = id[j][27];
					mscore = score[j];
				}
			}
			fout << " " << D[mindex];
		}
		fout << endl;
	}
}
