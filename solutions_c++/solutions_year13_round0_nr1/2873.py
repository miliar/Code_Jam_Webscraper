#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

int n, t, a, b;
#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)

int main() {
	ifstream myfile;
	myfile.open("input.txt");
	ofstream myfile2;
	myfile2.open("output.txt");
	
	myfile >> n;

	for (int u = 0; u < n; u++) {
		int** ary = new int*[4];
		for(int i = 0; i < 4; ++i)
			ary[i] = new int[4];

		For(i,0,3)
		{
		 string temp;

		 myfile>>temp;
		 For(j,0,3)
		 {
			 if(temp[j]=='X')
			 ary[i][j]=2;
			 else if(temp[j]=='O')
			 ary[i][j]=-2;
			 else if(temp[j]=='T')
				 ary[i][j]=1;
			 else
				 ary[i][j]=0;
		 }
		}
		 bool mark=false;
		For(i,0,3)
		{

			if((ary[i][1]+ary[i][0]+ary[i][2]+ary[i][3])==8 || (ary[i][1]+ary[i][0]+ary[i][2]+ary[i][3])==7)
			{
				mark=true;
				myfile2<<"Case #"<<u+1<<": "<< "X won"<<endl;
				break;
			}
			if((ary[i][1]+ary[i][0]+ary[i][2]+ary[i][3])==-8 || (ary[i][1]+ary[i][0]+ary[i][2]+ary[i][3])==-5)
			{
				mark=true;
				myfile2<<"Case #"<<u+1<<": "<< "O won"<<endl;
				break;
			}

		}
		if(!mark)
		{
			
		
		For(i,0,3)
		{
			if((ary[0][i]+ary[1][i]+ary[2][i]+ary[3][i])==8 || (ary[0][i]+ary[1][i]+ary[2][i]+ary[3][i])==7)
			{
				mark=true;
				myfile2<<"Case #"<<u+1<<": "<< "X won"<<endl;
				break;
			}
			if((ary[0][i]+ary[1][i]+ary[2][i]+ary[3][i])==-8 || (ary[0][i]+ary[1][i]+ary[2][i]+ary[3][i])==-5)
			{
				mark=true;
				myfile2<<"Case #"<<u+1<<": "<< "O won"<<endl;
				break;
			}

		}
		}
			if(!mark)
		{
			
		
			if((ary[1][1]+ary[0][0]+ary[2][2]+ary[3][3])==8 || (ary[1][1]+ary[0][0]+ary[2][2]+ary[3][3])==7)
			{
				mark=true;
				myfile2<<"Case #"<<u+1<<": "<< "X won"<<endl;

			}
			else if((ary[1][1]+ary[0][0]+ary[2][2]+ary[3][3])==-8 || (ary[1][1]+ary[0][0]+ary[2][2]+ary[3][3])==-5)
			{
				mark=true;
				myfile2<<"Case #"<<u+1<<": "<< "O won"<<endl;
			

		}
			if((ary[0][3]+ary[1][2]+ary[2][1]+ary[3][0])==8 || (ary[0][3]+ary[1][2]+ary[2][1]+ary[3][0])==7)
			{
				mark=true;
				myfile2<<"Case #"<<u+1<<": "<< "X won"<<endl;

			}
			else if((ary[0][3]+ary[1][2]+ary[2][1]+ary[3][0])==-8 || (ary[0][3]+ary[1][2]+ary[2][1]+ary[3][0])==-5)
			{
				mark=true;
				myfile2<<"Case #"<<u+1<<": "<< "O won"<<endl;
			

		}
			}
			if(!mark)
		{
		
		For(i,0,3)
		{
						if(!mark)
		{
			For(j,0,3)
			{
				if(ary[i][j]==0)
				{
					mark=true;
						myfile2<<"Case #"<<u+1<<": "<< "Game has not completed"<<endl;
						break;
			
				}
			}
						}
		}
			}
			if(!mark)
		{
			
		For(i,0,3)
		{
			if((ary[i][1]+ary[i][0]+ary[i][2]+ary[i][3])<7 && (ary[i][1]+ary[i][0]+ary[i][2]+ary[i][3])>-5)
			{
				mark=true;
				myfile2<<"Case #"<<u+1<<": "<< "Draw"<<endl;
				break;
			}

		}
			}
			if(!mark)
		{
			
		myfile2<<"Case #"<<u+1<<": "<< "ON"<<endl;
			}
	}
	system("pause");
}