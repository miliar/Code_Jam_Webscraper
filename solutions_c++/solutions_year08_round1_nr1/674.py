#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<vector>
#include<cmath>
#include<iomanip>
#include<algorithm>
using namespace std;
int x[3],y[3];
int a[3];
int main(){
	//string filein("test.txt");
	//string filein("A-small(2).in");
	string filein;
	//filein="A-small.in";
	//filein="A-large.in";
	filein="test.txt";
	filein="A-small-attempt0.in";
	string fileout;
	//fileout="Anslarge.txt";
	fileout="Anstest.txt";
	fileout="Anssmall.txt";
	ifstream fin;
	fin.open(filein.c_str());
	ofstream fout;
	fout.open(fileout.c_str());
	string word;
	int Case;
	fin>>Case;
	for(int i=1;i<=Case;i++)
	{
		fout<<"Case #"<<i<<": ";
		int n;
		fin>>n;
		vector<int>A;
		vector<int>B;
		int tmp;
		for(int j=0;j<n;j++)
		{
			fin>>tmp;
			A.push_back(tmp);
		}
		for(int j=0;j<n;j++)
		{
			fin>>tmp;
			B.push_back(tmp);
		}
		sort(A.begin(),A.end());
		sort(B.begin(),B.end());
		int Ans=0;
		for(int j=0;j<n;j++)
		{
			Ans+=A[j]*B[n-1-j];
		}
		fout<<Ans<<endl;
	}
	return 0;
}