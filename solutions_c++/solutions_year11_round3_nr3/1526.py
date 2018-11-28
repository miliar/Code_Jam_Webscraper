#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("out.txt");
typedef unsigned long int uli;
vector<uli>harmony;

int main () {
	int T,N,L,H,Case = 0,i,j;
	fin >> T;
	while(T) {
		--T;
		++Case;
		fin >> N >> L >> H;
		harmony.clear();
		for(i = 0;i < N;++i) {
			fin >> j;
			harmony.push_back(j);
		}
		bool all = false;
		for(i = L;i <= H;++i) {
			bool flag = true;
			for(j = 0;j < N;++j) {
				if( (harmony[j] % i != 0) && (i % harmony[j] != 0) ) {
					flag = false;
					break;
				}
			}
			if(flag) {
				all = true;
				break;
			}
		}
		if(all) {
			fout<<"Case #" <<Case << ": " << i <<endl;
		}
		else {
			fout<<"Case #" <<Case << ": NO" <<endl;
		}
	}
    return 0;
}