#include <fstream>
#include <iostream>

using namespace std;

void main()
{
	ifstream fin("A-large.in");
	ofstream fout("output1.txt");

	int T,N;

	fin >> T;

	for(int i=0; i<T; i++){
		int a[1000], b[1000], cnt=0;

		fin >> N;
		for(int j=0; j<N; j++){
			fin >> a[j] >> b[j];
		}

		if(N >= 2){
			for(int k=0; k<N; k++){
				for(int z=0; z<N; z++){
					if(a[k] > a[z] && b[k] < b[z])
						cnt++;
			}}
		}
		fout << "Case #" << i+1 << ": " << cnt << endl;
	
	}
}