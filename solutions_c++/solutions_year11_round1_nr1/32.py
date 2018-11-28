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
ofstream fout("A-small.out");
ifstream fin("A-small.in");
int gcd(int a, int b){
	if(a == 0 || b == 0){
		return a + b;
	}
	return gcd(b,a%b);
}
int main(){
	int T;
	fin >> T;
	for(int s=0;s<T;s++){
		int N, PD, PG;
		fin >> N >> PD >> PG;
		if(PG == 100 && PD != 100 || PG == 0 && PD != 0){
			fout << "Case #"<< s+1 << ": Broken" << endl;
			continue;
		}
		if(100/gcd(100, PD) > N){
			fout << "Case #"<< s+1 << ": Broken" << endl;
			continue;
		}
		fout << "Case #"<< s+1 << ": Possible" << endl;
	}
}
