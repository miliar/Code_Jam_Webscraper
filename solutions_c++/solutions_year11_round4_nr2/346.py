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
#include <complex>
using namespace std;
ofstream fout("B-large.out");
ifstream fin("B-large.in");
char yes[500][500];
long long p[500][500];
long long partial1[501][501];
pair<long long, long long> aaa[500][500];
pair<long long, long long> partial[501][501];
pair<long long, long long> times(long long a, pair<long long, long long> b){
	return pair<long long, long long>(a * b.first, a * b.second);
}
pair<long long, long long> add(pair<long long, long long> a, pair<long long, long long> b){
	return pair<long long, long long>(a.first + b.first, a.second + b.second);
}
int main(){
	int T;
	fin >> T;
	for(int s=0;s<T;s++){
		fout << "Case #"<< s+1 << ": ";
		int R, C, D;
		fin >> R >> C >> D;
		
		//pair<int, int> correct[R+1][C+1];
		for(int i=0;i<=R;i++){
			partial[i][0] = pair<long long, long long>(0, 0);
			partial1[i][0] = 0;
		}
		for(int i=0;i<=C;i++){
			partial[0][i] = pair<long long, long long>(0, 0);
			partial1[0][i] = 0;
		}
		for(int i=1;i<=R;i++){
			for(int j=1;j<=C;j++){
				fin >> yes[i-1][j-1];
				p[i-1][j-1] = yes[i-1][j-1] - '0';
				partial1[i][j] = p[i-1][j-1] + partial1[i-1][j] + partial1[i][j-1] - partial1[i-1][j-1];
				//cout << partial1[i][j] << endl;
				aaa[i-1][j-1] = times(yes[i-1][j-1] - '0', pair<long long, long long>(i-1, j-1));
				partial[i][j] =  add(add(aaa[i-1][j-1], partial[i-1][j]), add(partial[i][j-1], times(-1, partial[i-1][j-1])));
				//cout << i << " " << j << " " << partial[i][j].first << " " << partial[i][j].second << endl;
			}
			
		}
		bool found3 = false;
		for(int k=min(R, C);k>=3;k--){
			bool found2 = false;
			for(int i = 0;i<R-k+1;i++){
				bool found = false;
				for(int j=0;j<C-k+1;j++){
					pair<long long, long long> one = partial[i][j];
					pair<long long, long long> two = partial[i+k][j+k];
					pair<long long, long long> three = partial[i+k][j];
					pair<long long, long long> four = partial[i][j+k];
					pair<long long, long long> a1 = add(add(one, two), times(-1, add(three,four)));
					pair<long long, long long> a2 = add(a1, times(-1, add(add(aaa[i][j],aaa[i][j+k-1]), add(aaa[i+k-1][j],aaa[i+k-1][j+k-1]))));
					//cout << k << " " << i << " " << j << " " << a2.first << " " << a2.second << " " << partial1[i][j] + partial1[i+k][j+k] - partial1[i+k][j] - partial1[i][j+k] - p[i][j] - p[i][j+k-1] - p[i+k-1][j] - p[i+k-1][j+k-1] << endl;
					if(times(partial1[i][j] + partial1[i+k][j+k] - partial1[i+k][j] - partial1[i][j+k] - p[i][j] - p[i][j+k-1] - p[i+k-1][j] - p[i+k-1][j+k-1],pair<int, int>(2*i + (k-1), 2*j + (k-1))) == times(2,a2) ){
						fout << k;
						found = true;
						break;
					}
				}
				if(found){
					found2 = true;
					break;
				}
			}
			if(found2){
				found3 = true;
				break;
			}
		}
		if(!found3){
			fout << "IMPOSSIBLE";
		}
		fout << endl;
	}
}
