#include <iostream>

// basic file operations
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>


using namespace std;

double UCLN(double a, double b);
void main()
{
	ifstream in ("inputL.in");
	ofstream out("outputL.out");
	//out.open("output.in");
	double T;
	double Case=0;
	
	in>>T;
	
	for(Case = 1;Case<=T;Case++)
	{
		double N, Pd, Pg;
		in>>N;
		in>>Pd;
		in>>Pg;
		
		double mD,mG;
		mD = UCLN(Pd,100);
		mG = UCLN(Pg,100);
		mD = 100/mD;
		mG = 100/mG;
		//out<<"pD:"<<Pd<<"mD:"<<mD<<endl;
		//out<<"pG:"<<Pg<<"mG:"<<mG<<endl;
		
		if (mD>N||(Pd<100&&Pg==100)||(Pg==0&&Pd>0))
			out<<"Case #"<<Case<<": "<<"Broken"<<endl;
		else
			out<<"Case #"<<Case<<": "<<"Possible"<<endl;
	}
	in.close();
	out.close();
}
double UCLN(double a, double b)
{
	double kq = 0; 
	if (a==0 ||b==0)
		return a+b;
	while (a !=b)
	{
		if(a>b)
			a=a-b;
		else
			b=b-a;
	}
	return a;
}