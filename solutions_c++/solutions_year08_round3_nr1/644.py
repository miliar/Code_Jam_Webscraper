#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <conio.h>

using namespace std;

int main ()
{

	ifstream myfile;
	ofstream outfile;
	myfile.open("sample.txt");
	outfile.open("output.txt");

	int N,l;

	long i,j,k;

	long P,K,L,press[1000],tmp,S,x;


	myfile>>N;

	for(l=0;l<N;l++)
	{
		myfile>>P>>K>>L;

		for(i=0;i<L;i++)myfile>>press[i];

		for(j=0;j<L;j++)for(k=0;k<L-1;k++)if(press[k]<press[k+1])
		{

			tmp=press[k];
			press[k]=press[k+1];
			press[k+1]=tmp;
		}

		S=0; x=0;
		for(i=0;i<L;i++)
		{
			if(i%K==0)x++;


			S+=x*press[i];

		}









		outfile<<"Case #"<<l+1<<": "<<S<<endl;

  

	}



	//getch();




	myfile.close();
	outfile.close();
	
	return 0;

}
