#include <algorithm>
#include <iostream>
#include <fstream>
#include <Windows.h>

using namespace std;

int d[1024][1024] = {999999999};
int cnt[1024][1024] = {0};

void prob1() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int T,t=0;

	int N,M;
	int i,j,k,tmp;
	int r;
	
	fin >> T;
	
	while(T--) {
		fin >> N;
		
		for(j=0;j<N;j++) {
			for(k=0;k<N;k++) {
				d[j][k]=999999999;
				cnt[j][k]=0;
			}
		}

		for(i=0;i<N;i++) {

			
			
			fin >> M;
			for(j=0;j<M;j++) {
				fin >> tmp;
				d[i][tmp-1] = 1;
				cnt[i][tmp-1]++;
			}
		}

		for(i=0;i<N;i++) {
			for(j=0;j<N;j++) {
				for(k=0;k<N;k++) {
					if(d[j][i] + d[i][k] < 999999999) {
						d[j][k] = d[j][i] + d[i][k];
						cnt[j][k]++;
					}
				}
			}
		}


		r=0;
		for(i=0;i<N;i++) {
			for(j=0;j<N;j++) {
				if(cnt[i][j]>1) r=1;
			}
		}
		cout << t << endl;
		fout << "Case #" << ++t << ": ";
		if(r) fout << "Yes" << endl;
		else fout << "No" << endl;
		
	}

	fin.close();
	fout.close();
}

int main() {
	prob1();
	system("pause");
}