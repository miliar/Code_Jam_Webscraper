// snapper.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
using namespace std;
#include <math.h>



int _tmain(int argc, _TCHAR* argv[])
{
	bool ResultOutput(int N,long int K);
	int N,lines;
	long int K;
	ifstream input("A-large.in",ios::in);
	ofstream output("A-large.out",ios::out);
    input>>lines;
	for(int i=0;i<lines;i++)
	{
	  input>>N;
	  input>>K;
      if(ResultOutput(N,K))
		  output << "Case #" << i+1 << ": ON"<<'\n';
	  else
		  output << "Case #" << i+1 << ": OFF"<<'\n';

	}
	input.close();
	output.close();
	return 0;
}
bool ResultOutput(int N,long int K)
	{
       long int q=1;
       for(int i=0;i<N;i++)
       {
          q=q*2;
       }
		if((K+1)%q==0)
		{
			return true;
		}
		else
		{
			return false;

		}

	}

