#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;


int main()
{
	ifstream ifile("A-large.in");
	ofstream ofile("A-large-out.txt");

	long f[40];
	long k;
	int i,t,n;
	ifile>>t;
		
	//≥ı ºªØf[40]
	for (i=0;i<31;i++)
	{
		if (i==0) f[i]=1;
		else f[i]=f[i-1]*2;
		
	}

	for (i=0;i<t;i++)
	{
		//n devices,and k knock times 
		ifile>>n>>k;
		ofile<<"Case #" <<i+1<<":"; 
		if ((k+1)%f[n]==0)
		{
			ofile<<" ON"<<endl;
		}
		else
		{
			ofile<<" OFF"<<endl;
		}
	
	}
	return 0;

}


