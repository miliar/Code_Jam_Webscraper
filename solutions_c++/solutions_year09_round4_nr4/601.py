#include <iostream>
#include <sstream>
#include <fstream>
#include <conio.h>
#include <vector>
#include <math.h>
#include <iomanip>
//#include<>
using namespace std;

bool zero(double a)
{
  return ((a<0.00000001)&&(a>-0.00000001));    
};

double max(double a, double b)
{
	return a>b?a:b;	
};

double min(double a, double b)
{
	return a<b?a:b;	
};


int main(int argc, char *argv[])
{
   
    ifstream in;
    ofstream out;
    in.open("D-small-attempt0.in",ios::in);
    out.open("ap.out",ios::out);
    int C,c,N,i,j;
    in >> C;
    double X[50],Y[50],R[50],ans,dist;
    for (c=1;c<=C;c++)
    {
		in>>N;
		for (i=0;i<N;i++) in>>X[i]>>Y[i]>>R[i];
		if (N==1) 
		{
			out<<"Case #"<<c<<": "<<R[0]<<"\n";
			continue;
		};
		if (N==2)
		{
			out<<"Case #"<<c<<": "<<max(R[0],R[1])<<"\n";
			continue;
		};
		ans=100000;

		dist=sqrt((X[0]-X[1])*(X[0]-X[1])+(Y[0]-Y[1])*(Y[0]-Y[1]))+R[0]+R[1];
		ans=min(ans,max(dist,2*R[2]));

		dist=sqrt((X[1]-X[2])*(X[1]-X[2])+(Y[1]-Y[2])*(Y[1]-Y[2]))+R[1]+R[2];
		ans=min(ans,max(dist,2*R[0]));

		dist=sqrt((X[0]-X[2])*(X[0]-X[2])+(Y[0]-Y[2])*(Y[0]-Y[2]))+R[0]+R[2];
		ans=min(ans,max(dist,2*R[1]));
		out<<"Case #"<<c<<": "<<ans/2<<"\n";
    };
    
    in.close();
    out.close();
//    getch();
    return EXIT_SUCCESS;
   
}
