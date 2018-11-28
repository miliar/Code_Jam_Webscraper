#include<iostream>
#include<algorithm>
#include<cmath>
#include<fstream>
using namespace std;
int main(){
	int t;
	ifstream fin("A-large.in");
	ofstream fout("out.out");
	fin >> t;
	for(int i = 0; i < t; i++){
		int n, a, t1 = 0, p1 = 1, t2 = 0, p2 = 1;
		char c;
		fin >> n;
		for(int i = 0; i < n; i++){
			fin >> c >> a;
			if(c == 'O'){
				t1 = max(abs(a - p1) + t1, t2) + 1;
				p1 = a;
			}
			else{
				t2 = max(t1, abs(a - p2) + t2) + 1;
				p2 = a;
			}
		}
		fout << "Case #" << i + 1 << ": " << max(t1, t2) << endl;
	}
	return 0;
}