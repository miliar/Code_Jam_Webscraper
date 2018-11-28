//Stephen Aultman

#include<math.h>
#include<iostream>
#include<fstream>

using namespace std;

long expansion(long n);

int main()
{
  
  //Read the input file
  ifstream file;
  file.open("A-small-attempt3.in",ifstream::in);
  //output file
  ofstream outfile;
  outfile.open("output.txt",ofstream::out);
  long numCases,i,N,K,K2,expanded;
 /* 
  cout<<"expansion of 1 2 3 4 5 are "<<
  expansion(1)<<" "<<
  expansion(2)<<" "<<
  expansion(3)<<" "<<
  expansion(4)<<" "<<
  expansion(5)<<" "<<endl;
  */
 if(file.good())
  {   
    file>>numCases;
    for(i=0;i<numCases;i++)
    {
	file>>N>>K;
	expanded=expansion(N);
	K2=K%(expanded+(long)1);
//	  cout<<N<<" "<<K<<" "<<expanded<<" "<<K2<<endl;
	if(K2==expanded)
	{
	  outfile<<"Case #"<<(i+1)<<": ON"<<endl;
	}
	else
	  outfile<<"Case #"<<(i+1)<<": OFF"<<endl;
    }
  }
	 
  file.close();
  return(0);
}

long expansion(long n)
{
 long i,place,result;
 
 place=1;result=0;
 
 for(i=0;i<n;i++)
 {
  result+=place;
  place*=2;   
 }
 
 return(result);
}