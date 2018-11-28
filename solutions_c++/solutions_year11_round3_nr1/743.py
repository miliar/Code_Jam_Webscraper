#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
using namespace std;

int main(){
	ifstream input;
	input.open("prueba.dat");
	ofstream output;
	output.open("output.dat");

	int t,r,c;
	int mat[60][60];
	char temp[60];
	input>>t;
	bool posible;

	for (int s=1; s<=t;s++)
	{
		input>>r>>c;
		for (int i=0; i<r;i++)
		{
			input>>temp;
			for (int j=0; j<c; j++)
			{ if (temp[j]=='#') mat[i][j]=1;
			else mat[i][j]=0;}
		}
		
		for (int i=0; i<r;i++)
		{
			for (int j=0; j<c; j++)
			{ 
				if (mat[i][j]==1 and mat[i+1][j]==1 and mat[i][j+1]==1 and mat[i+1][j+1]==1) 
				{ mat[i][j]=2; mat[i+1][j]=3; mat[i][j+1]=4; mat[i+1][j+1]=5; j++;}
			}
		}
		
		posible=true;
		for (int i=0; i<r;i++)
		{
			for (int j=0; j<c; j++)
			{ 
				if (mat[i][j]==1) 
				{ posible = false; j=c; i=r;}
			}
		}
		
		output<<"Case #"<<s<<": "<<"\n";
		if (posible)
		{for (int i=0; i<r;i++)
		{
			for (int j=0; j<c; j++)
			{ 
				if (mat[i][j]==0) output<<".";
				if (mat[i][j]==2) output<<"/";
				if (mat[i][j]==3) output<<"\\";
				if (mat[i][j]==4) output<<"\\";
				if (mat[i][j]==5) output<<"/";
			}
			output<<"\n";
		}}
		else
		output<<"Impossible\n";
		
	}
	
	output.close();
	input.close();
	
	return 0;
					

}
