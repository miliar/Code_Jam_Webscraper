// tic.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>

using namespace std;
int main()
{
	int ans;
	int t;
	int tic[4][4];
	ifstream fp;
	ofstream fout;
	fp.open("input.txt",ios::beg);
	fout.open("output.txt",ios::beg);
	fp >> t;
	
	
	

	for(int test =0;test<t;++test){
		for(int j=0;j<4;++j){
			for(int k=0;k<4;++k){
				fp>>tic[j][k];
			}
		}
		ans=0;
		for(int i=0;i<4;++i){

			if((tic[i][0]==0||tic[i][0]==1) && (tic[i][1]==0||tic[i][1]==1) && (tic[i][2]==0||tic[i][2]==1) && (tic[i][3]==0||tic[i][3]==1))
				ans=1;
			else if((tic[i][0]==0||tic[i][0]==2) && (tic[i][1]==0||tic[i][1]==2) && (tic[i][2]==0||tic[i][2]==2) && (tic[i][3]==0||tic[i][3]==2))
				ans=2;
			else if((tic[0][i]==0||tic[0][i]==1) && (tic[1][i]==0||tic[1][i]==1) && (tic[2][i]==0||tic[2][i]==1) && (tic[3][i]==0||tic[3][i]==1))
				ans=1;
			else if((tic[0][i]==0||tic[0][i]==2) && (tic[1][i]==0||tic[1][i]==2) && (tic[2][i]==0||tic[2][i]==2) && (tic[3][i]==0||tic[3][i]==2))
				ans=2;
		}
			if((tic[0][0]==0||tic[0][0]==1) && (tic[1][1]==0||tic[1][1]==1) && (tic[2][2]==0||tic[2][2]==1) && (tic[3][3]==0||tic[3][3]==1))
				ans=1;
			else if((tic[0][3]==0||tic[0][3]==1) && (tic[1][2]==0||tic[1][2]==1) && (tic[2][1]==0||tic[2][1]==1) && (tic[3][0]==0||tic[3][0]==1))
				ans=1;
			else if((tic[0][3]==0||tic[0][3]==2) && (tic[1][2]==0||tic[1][2]==2) && (tic[2][1]==0||tic[2][1]==2) && (tic[3][0]==0||tic[3][0]==2))
				ans=2;
			else if((tic[0][0]==0||tic[0][0]==2) && (tic[1][1]==0||tic[1][1]==2) && (tic[2][2]==0||tic[2][2]==2) && (tic[3][3]==0||tic[3][3]==2))
				ans=2;
		
		if (ans==0){
			for(int m=0;m<4;++m){
				for(int n=0;n<4;++n){
					if(tic[m][n]==3){
						ans=3;
						
					}
				}
			}
		}
		if (ans==0)
			fout<<"Case #"<<test+1<<": Draw"<<endl;
		if (ans==1)
			fout<<"Case #"<<test+1<<": X won"<<endl;
		if (ans==2)
			fout<<"Case #"<<test+1<<": O won"<<endl;
		if (ans==3)
			fout<<"Case #"<<test+1<<": Game has not completed"<<endl;
	}
	fp.close();
	fout.close();
		
	return 0;
}

