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
ofstream fout("D-large.out");
ifstream fin("D-large.in");
int main(){
	int T;
	fin >> T;
	for(int s=0;s<T;s++){
		int N;
		fin >> N;
		int num = 0;
		for(int i=0;i<N;i++){
			int k;
			fin >> k;
			if(k != i + 1){
				num ++;
			}
		}
		fout << "Case #"<< s+1 << ": " << num << endl;
	}
}
