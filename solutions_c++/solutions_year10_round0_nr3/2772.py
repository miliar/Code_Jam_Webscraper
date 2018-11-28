// park.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <sstream>
using namespace std;
using std::endl;

int _tmain(int argc, _TCHAR* argv[])
{
	int lines,N;
    long int R,k;

	ifstream input("C-small-attempt0.in",ios::in);
	ofstream output("C-small-attempt0.out",ios::out);
    input>>lines;
    for(int l=0;l<lines;l++)
	{
	 long int Money=0;
     input>>R;
	 input>>k;
	 input>>N;
	 long int *Gr= new long int[N];
     stringstream stream;
	 for(int g=0;g<N;g++)
	 {
		 input>>Gr[g];
	 }
	 for(long int r=0;r<R;r++)
	 {
		 int i=0;
		 long int p=0;
         for(;i<N;i++)
		 {
			 p=p+Gr[i];
			 if(p>k)
			 {
                 p=p-Gr[i];			
				 break;
			 }
			 else
				{
              stream<<Gr[i]<<endl;
			  
			    }
		 }
		 int m=0;
		 for(;m<N-i;m++)
		 {
			 Gr[m]=Gr[m+i];
		 }
		 for(;m<N;m++)
		 {
			 stream>>Gr[m];
		 }
		 stream.clear();
		 
		 Money=Money+p;
	 }
		  output << "Case #" << l+1 << ": "<<Money<<'\n';
		  delete[] Gr;
		  Gr=NULL;
	}
	input.close();
	output.close();
	return 0;
}

