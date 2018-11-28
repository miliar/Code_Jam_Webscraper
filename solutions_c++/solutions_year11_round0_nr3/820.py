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
ofstream fout("C-large.out");
ifstream fin("C-large.in");
int main(){
	int T;
	fin >> T;
	for(int s=0;s<T;s++){
		int N;
		fin >> N;
		unsigned long long patricksum = 0;
		unsigned long long seansum = 0;
		unsigned long long seanmin = 100000000;
		for(int i=0;i<N;i++){
			unsigned long long k;
			fin >> k;
			patricksum = patricksum ^ k;
			seansum = seansum + k;
			seanmin = min(seanmin, k);
		}
		if(patricksum != 0){
			fout << "Case #"<< s+1 << ": NO" << endl;
		} else {
			fout << "Case #"<< s+1 << ": " << seansum - seanmin << endl;
		}
	}
}
