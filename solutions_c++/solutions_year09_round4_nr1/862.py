#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

ifstream fin("infile.in");
ofstream fout("outfile.out");

const int SIZE = 100;

int main()
{
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		int N; fin>>N;
		int leastRow[SIZE];
		for(int i=0; i<N; i++) {
			int row=0;
			for(int j=0; j<N; j++) {
				char ch; fin>>ch;
				if(ch=='1') row=j;
			}
			leastRow[i]=row;
		}

		int swapCount=0;
		for(int row=0; row<N; row++) {
			int index=-1;
			for(int i=row; i<N; i++) {
				if(leastRow[i]<=row) {
					index=i;
					break;
				}
			}
			int temp=leastRow[index];
			for(int i=index; i>row; i--)
				leastRow[i] = leastRow[i-1];
			leastRow[row] = temp;
			swapCount += index-row;
		}

		fout<<"Case #"<<t<<": "<<swapCount<<endl;
	}

	return 0;
}