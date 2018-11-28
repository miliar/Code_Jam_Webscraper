#include <iostream>
#include <cstring>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
using namespace std;

int Pair[2000][2];
int main(){
	ifstream in("A-large.in");
	ofstream out("out.txt");
	int cases;
	in >> cases;
	for(int c = 1; c <= cases; c++){
		int n, ans = 0;
		in >> n;
		for(int i = 0; i < n; i++){
			in >> Pair[i][0] >> Pair[i][1];
		}
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if(i == j) continue;
				if(Pair[i][0] < Pair[j][0] && Pair[i][1] > Pair[j][1])
					ans ++;
			}
		}
		out << "Case #" << c << ": " << ans << endl;
	}
	return 0;
}