#include <fstream>
#include <stdlib.h>
#include <iostream>
using namespace std;

int main(){
	ifstream fin("input.in");
	ofstream fout("output.txt");
	int t, n, s, p, border, count, cur;
	fin >> t;
	for(int i = 1;i<=t;i++){
		fin >> n >> s >> p;
		border = count = 0;
		for(int j = 1;j<=n;j++){
			fin >> cur;
			if(cur >= p*3-2)count++;
			else if(cur >= p*3-4 && cur>0)border++;
		}
		count += min(s, border);
		fout << "Case #" << i << ": " << count << '\n';
	}
	return 0;
}
