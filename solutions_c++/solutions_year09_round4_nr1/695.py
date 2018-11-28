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

int main(int argc, char *argv[])
{
   
    ifstream in;
    ofstream out;
    in.open("A-large.in",ios::in);
    out.open("ap.out",ios::out);
    int T,t,N,i,j,s,m,q,k;
    string mat[50],st;
    int right[50];
    bool good;
    in >> T;
    for (t=1;t<=T;t++)
    {
		in>>N;
		for (i=0;i<N;i++) in>>mat[i];
		for (i=0;i<N;i++)
		{
			right[i]=0;
			for (j=N-1;j>=0;j--) if (mat[i][j]=='1')
			{
				right[i]=j;
				break;	
			};
		};
		good=false;
		m=0;
		while (!good)
		{
			good=true;
			for (i=0;i<N;i++)
			if (right[i]>i)
			{
				j=i+1;
				while (right[j]>=right[i]) j++;
				for (k=j-1;k>=i;k--)
				{
					q=right[k];
					right[k]=right[k+1];
					right[k+1]=q;
					m++;
				};
				good=false;
				cout<<"case "<<t<<":   "<<j<<","<<right[j]<<"<--->"<<j+1<<","<<right[j+1]<<"\n";
				break;				
			};
				
		};
		out<<"Case #"<<t<<": "<<m<<"\n";
    };
    
    in.close();
    out.close();
//    getch();
    return EXIT_SUCCESS;
   
}
