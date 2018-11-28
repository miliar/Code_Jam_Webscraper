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

	int t,n;
	input>>t;
	char temp[100];
	int mat[100][100];
	int res[100][2];
	double wp[100];
	double owp[100];
	double oowp[100];
	int k;
	
	for (int s=1; s<=t;s++)
	{
		input>>n;
		for (int i=0; i<n; i++)
				{
					res[i][0]=0;
					res[i][1]=0;
					wp[i]=0.;
					owp[i]=0.;
					oowp[i]=0.;
				}

		for (int i=0;i<n;i++)
		{
			input>>temp;
			for (int j=0; j<n; j++)
			{
				if (temp[j] =='1') {mat[i][j]=2; res[i][0]++; res[i][1]++;} 
				if (temp[j] =='0') {mat[i][j]=1; res[i][0]++;} 
				if (temp[j]=='.') mat[i][j]=0;
				
			}
			if (res[i][0]!=0) {wp[i]=1.0*res[i][1]/res[i][0]; }
		}
		
		for (int i=0; i<n;i++)
		{
			k=0;
			for (int j=0; j<n; j++)
				{
				if (mat[i][j]!=0) {owp[i]+=(1.0*res[j][1]-(mat[j][i]-1.0))/(res[j][0]-1.0);}
				}
			owp[i]=1.0*owp[i]/res[i][0];
		}
		
		for (int i=0; i<n;i++)
		{
			k=0;
			for (int j=0; j<n; j++)
				{
				if (mat[j][i]!=0) {oowp[i]+=owp[j];	k++;}
				}
			oowp[i]=oowp[i]/res[i][0];
		}
		
		
		output<<"Case #"<<s<<": "<<"\n";
		for (int i=0; i<n;i++)
		{
		output<<(0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i])<<"\n";
		}
	}
	
	output.close();
	input.close();
	
	return 0;
					

}
