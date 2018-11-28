#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>

using namespace std;

int main ()
{

	ifstream myfile;
	ofstream outfile;
	myfile.open("sample.txt");
	outfile.open("output.txt");

	long i,j,l,t;

	long T,n,x[1000],y[1000],S;

	myfile>>T;

	for(l=0;l<T;l++)
	{
		myfile>>n;

		for(i=0;i<n;i++)myfile>>x[i];
		for(i=0;i<n;i++)myfile>>y[i];

		
		for(i=0;i<n;i++)
			for(j=0;j<n-1;j++)
				if(x[j]>x[j+1])
				{
					t=x[j]; x[j]=x[j+1]; x[j+1]=t;
				}


		for(i=0;i<n;i++)
			for(j=0;j<n-1;j++)
				if(y[j]<y[j+1])
				{
					t=y[j]; y[j]=y[j+1]; y[j+1]=t;
				}

		
		S=0;
		for(i=0;i<n;i++)S+=x[i]*y[i];

		
		outfile<<"Case #"<<l+1<<": "<<S<<endl;

  

	}



	//getch();




	myfile.close();
	outfile.close();
	
	return 0;

}
