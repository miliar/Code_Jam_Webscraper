//#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

ifstream cin("B-large.in",ios::in);
ofstream cout("B-large.out",ios::out);

bool AB(int** A, char** B, int H, int W)
{
	bool done=1;
	for (int i=0; i<H; i++) {
		for (int j=0; j<W; j++) {
			if (B[i][j] < '5') {
				switch (B[i][j]) {
					case '0':
						if (B[i-1][j] > '5')
							B[i][j] = B[i-1][j];
						else done=0;
						break;
					case '1':
						if (B[i][j-1] > '5')
							B[i][j] = B[i][j-1];
						else done=0;
						break;
					case '2':
						if (B[i+1][j] > '5')
							B[i][j] = B[i+1][j];
						else done=0;
						break;
					case '3':
						if (B[i][j+1] > '5')
							B[i][j] = B[i][j+1];
						else done=0;
						break;
					default:
						break;
				}
			}
		}
	}
	return done;
}

void sheds()
{
	int** A;
	char** B;
	int H, W;
	cin>>H>>W;
	A = new int*[H];
	B = new char*[H];
	for (int i=0; i<H; i++) {
		A[i] = new int[W];
		B[i] = new char[W];
		for (int j=0; j<W; j++)
			cin>>A[i][j];
	}

	int min;
	char cur = 'A';
	for (int i=0; i<H; i++) {
		for (int j=0; j<W; j++) {
			min = A[i][j];
			if (i!=0 && A[i-1][j]<min) { B[i][j]='0'; min=A[i-1][j]; }
			if (j!=0 && A[i][j-1]<min) { B[i][j]='1'; min=A[i][j-1]; }
			if (j!=W-1 && A[i][j+1]<min) { B[i][j]='3'; min=A[i][j+1]; }
			if (i!=H-1 && A[i+1][j]<min) { B[i][j]='2'; min=A[i+1][j]; }
			if (min==A[i][j]) { B[i][j]=cur; cur++; }
		}
	}

	while (!AB(A,B,H,W)) {}

	cur = 'a';
	char ctc;
	for (int i=0; i<H; i++) {
		for (int j=0; j<W; j++) {
			if (B[i][j]<'a') {
				ctc = B[i][j];
				for (int k=0; k<H; k++) {
					for (int l=0; l<W; l++) {
						if (B[k][l]==ctc)
							B[k][l]=cur;
					}
				}
				cur++;
			}
		}
	}

	for (int i=0; i<H; i++) {
		for (int j=0; j<W; j++)
			cout<<B[i][j]<<" ";
		cout<<endl;
	}

	for (int i=0; i<H; i++) {
		delete [] A[i];
		delete [] B[i];
	}
	delete [] A;
	delete [] B;
}

void main()
{
	int T;
	cin>>T;
	for (int i=1; i<=T; i++) {
		cout<<"Case #"<<i<<":"<<endl;
		sheds();
	}
}