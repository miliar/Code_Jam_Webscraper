#include<fstream>
#include<iostream>
using namespace std;

int main(){
	ofstream fout("split.out");
	ifstream fin ("split.in");
	int test;
	int num;
	int candy[1001];
	fin >> test;
	int max;
	for(int i=1;i<=test;i++) {
		fin >> num;
		max = -1;
		for (int j =0;j<num;j++) {
			fin >> candy[j];
		}
		int t = 0;
		for(int j =0;j<num;j++) {
			t = t ^ candy[j];
		}
		if (t!=0) {
			fout << "Case #" << i << ": NO\n";
			continue;
		}
		for (int j =0;j<num;j++) {
			int c = candy[j];
			int xor = 0;
			int sum = 0;
			for (int z=0;z<num;z++) {
				if(z!=j) {
					xor = xor ^ candy[z];
					sum = sum + candy[z];
				}
			}
			if(c == xor && max < sum) {
				max = sum;
			}				
		}
		fout << "Case #" << i << ": " << max << "\n";
	}
}