#include <iostream>
using namespace std;
#include <math.h>
#include <fstream>
void main()
{
	int T;
	ifstream infile;
	ofstream outfile;
	outfile.open("out.txt");
	infile.open("A-large.in");
    infile>>T;
    int *K=new int [T];
	int *N=new int [T];
	float *M=new float [T];
	int i;
	for(i=0;i<T;i++)
	{
		infile>>N[i];
		infile>>K[i];
	}
	for(i=0;i<T;i++)
	{
		M[i]=(K[i]+1)/pow(2,N[i]);
      	if(M[i]-int(M[i])<0.000000001)
		{
			outfile<<"Case #"<<i+1<<":"<<" "<<"ON\n";
		}
		else
			outfile<<"Case #"<<i+1<<":"<<" "<<"OFF\n";
	}
}