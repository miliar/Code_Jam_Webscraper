#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream fin("A-small-attempt1.in");
	ofstream fout("A-small-attempt1.out");
	int cant_cases;
	fin>>cant_cases;
	int trees[100000][2];
	for (int case_number=0;case_number<cant_cases;case_number++) {
		
		long long n, A, B, C, D, x0, y0,M;
		fin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		
		long long X = x0, Y = y0;
		trees[0][0]=X; trees[0][1]=Y;
		for (int i = 1;i<n;i++) {
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			trees[i][0]=X; trees[i][1]=Y;
		}
		
		//		for (int i=0;i<n;i++) {
		//			cout<<trees[i][0]<<" "<<trees[i][1]<<endl;
		//		}
		
		long long num=0, cx,cy;
		for (int i=0;i<n-2;i++) {
			for (int j=i+1;j<n-1;j++) {
				for (int k=j+1;k<n;k++) {
					cx = trees[i][0]+trees[j][0]+trees[k][0];
					cy = trees[i][1]+trees[j][1]+trees[k][1];
					if ( ( cx%3==0 ) && ( cy%3==0 ) ) {
						//						cx/=3; cy/=3;
						//						for (int o=0;o<n;o++) {
						//							if (trees[o][0]==cx && trees[o][1]==cy) {
						num++;
						//								break;
						//							}
						//						}
					}
				}
			}
		}
		
		cout<<"Case #"<<case_number+1<<": "<<num<<endl;
		fout<<"Case #"<<case_number+1<<": "<<num<<endl;
	}
	fout.close();
	fin.close();
	return 0;
}

