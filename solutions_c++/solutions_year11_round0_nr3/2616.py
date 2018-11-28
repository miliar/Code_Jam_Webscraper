#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <iostream>
#include <fstream>


using namespace std;

int main() {

	int T, N;

// 	ifstream fin("in.txt");	
	ifstream fin("C-large.in");	
	fin>>T;
	
	ofstream fout("out.txt");
	
	int bisum;
	int sum;
	int min;
	int x, i;
	
	for (int Ti=0; Ti<T; Ti++) {
		fin>>N;
		bisum = 0;
		sum = 0;
		min = 0;
		for (i=0; i<N; i++) {
			fin>>x;
			if (x<min||min==0) min=x;
			sum += x;
			if (bisum==0) bisum = x;
			else bisum ^= x;
// 		cout<<bisum<<endl;
		}
		if (bisum!=0) fout<<"Case #"<<Ti+1<<": NO"<<endl;
		else fout<<"Case #"<<Ti+1<<": "<<sum-min<<endl;
// 		cout<<endl<<endl;
	}
	
	fout.close();
	
	return 0;
}
