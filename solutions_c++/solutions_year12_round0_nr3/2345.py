#include <fstream>
#include <stdlib.h>
#include <cmath>
#include <iostream>
#include <set>
using namespace std;
int main(){
	ifstream fin("input.in");
	ofstream fout("output.txt");
	int t, a, b, cnt, rotations, currot;
	fin >> t;
	for(int i = 1;i<=t;i++){
		fin >> a >> b;
		cnt = 0;
		for(int n = a;n<=b;n++){
			rotations = log10(n);
			currot = n;
			set<int> workedrotations;
			for(int m = 0;m<rotations;m++){
				currot = ((currot%10)*pow(10, rotations+1)+currot)/10;
				if(currot>n&&currot<=b&&workedrotations.count(currot)==0){
					workedrotations.insert(currot);
					cnt++;
				}
			}
		}
		fout << "Case #" << i << ": " << cnt << '\n';
	}
	return 0;
}
