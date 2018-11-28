/*This is a C++ file*/

#include<iostream>
#include <algorithm>
#include <vector>
#include<fstream>
#include<string>
using namespace std;

#define FILE_IN "A-small-attempt3.in"
const char *FILENAME = "output.txt";



main()
{
 int T, N, i, j, k, clr, intersec=0;
 int w1[3],w2[3];
 
 ifstream input;
 ofstream fout(FILENAME);
 input.open(FILE_IN);


 if(!input)
	{
		cout<<endl<<"The file couldn't be found";
		exit(1);
	}

 input>>T;
 
 for(i=0;i<T;i++)
 {    input>>N;
	  for(clr=0;clr<3;clr++)
	  {
		  w1[clr]=0;
		  w2[clr]=0;
	  }
	  intersec=0;
	  
	  input>>w1[0]>>w2[0];
	  for(j=1;j<N;j++)
	  {
		  input>>w1[j]>>w2[j];
		  
		  for(k=0;k<j;k++)
		  {
			  if(((w1[j]-w1[k])>0 && (w2[j]-w2[k])<0) || ((w1[j]-w1[k])<0 && (w2[j]-w2[k])>0))
			  {
				  intersec++;
			  }
		  }
		  
	  }
	  fout<<"Case #"<<i+1<<": "<<intersec<<"\n";
 }
 input.close();
 fout.close();
 return 0;
}  

















 

 
