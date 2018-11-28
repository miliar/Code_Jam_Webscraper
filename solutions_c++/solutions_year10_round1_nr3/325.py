#include <iostream>
#include <fstream> 
#include <cstdlib> 
#include <cmath> 
#include <algorithm>
#include <vector> 
#include <string> 
#include <bitset> 
#include <set>
#include <sstream>
using namespace std; 
ifstream fin ("C-small.in");
ofstream fout ("output.out");
int main(){
	int T;
	fin >> T;
	for(int aa=0;aa<T;aa++){
		fout << "Case #" << (aa + 1) << ": ";
		int A1, A2, B1, B2;
		fin >> A1 >> A2 >> B1 >> B2;
		int count = 0;
		for(int i=A1;i<=A2;i++){
			for(int j=B1;j<=B2;j++){
				long long k = i, l = j;
				int stuff = 0;
				while(k*l > 0 && k/l+l/k < 2){
					int a = k;
					k%=l;
					l %= a;
					stuff++;
				}
				if((k == l) == (stuff%2)){
					count ++;
					cout << i << " " << j << endl;
				}
			}
		}
		fout << count << "\n";
	}
}
