#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<fstream>
#include<string>
#include<cstring>
#include<vector>
#include<list>
#include<map>
#define lli long long int
using namespace std;
int main() {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int t,a,b,fin_a,fin_b,dot,num;char A[4][4];
	fin>>num;
	for(int k=1;k<=num;k++) {
		for(int i=0;i<4;i++) {
			fin>>A[i];
			}
		fin_a=0;fin_b=0;dot=0;
		
		for(int i=0;i<4;i++) {
			a=0;b=0;
			for(int j=0;j<4;j++) {
				if(A[i][j]=='X')
					a++;
				else if(A[i][j]=='O')
					b++;
				else if(A[i][j]=='T') {
					a++;
					b++;
					}
				else
					dot++;
				}
			fin_a=max(fin_a,a);
			fin_b=max(fin_b,b);
			}

		for(int j=0;j<4;j++) {
			a=0;b=0;
			for(int i=0;i<4;i++) {
				if(A[i][j]=='X')
					a++;
				else if(A[i][j]=='O')
					b++;
				else if(A[i][j]=='T') {
					a++;
					b++;
					}
				else
					dot++;
				}
			fin_a=max(fin_a,a);
			fin_b=max(fin_b,b);
			}

		a=0;b=0;
		for(int i=0,j=0;j<4;i++,j++) {
			if(A[i][j]=='X')
				a++;
			else if(A[i][j]=='O')
				b++;
			else if(A[i][j]=='T') {
				a++;
				b++;
				}
			else
				dot++;
			}
		fin_a=max(fin_a,a);
		fin_b=max(fin_b,b);


		a=0;b=0;
		for(int i=0,j=3;i<4;i++,j--) {
			if(A[i][j]=='X')
				a++;
			else if(A[i][j]=='O')
				b++;
			else if(A[i][j]=='T') {
				a++;
				b++;
				}
			else
				dot++;
			}
		fin_a=max(fin_a,a);
		fin_b=max(fin_b,b);

		if(fin_a==4)
			fout<<"Case #"<<k<<": X won"<<endl;
		else if(fin_b==4)
			fout<<"Case #"<<k<<": O won"<<endl;
		else if(dot>0)
			fout<<"Case #"<<k<<": Game has not completed"<<endl;
		else
			fout<<"Case #"<<k<<": Draw"<<endl;
		}
	return 0;
	}
