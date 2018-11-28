#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
	double testcases=0,snapp=0,num ;

    ofstream fout ("A-large.out");
    ifstream fin ("A-large.in");

	fin>>testcases;

	for(int i=0;i<testcases;i++)
	{
		fin>>num>>snapp;

		num=pow(2.0,num);

		if((int)snapp%(int)num==num-1)
			fout<<"Case #"<<i+1<<": ON"<<endl;    
        else
            fout<<"Case #"<<i+1<<": OFF"<<endl;
	}


	return 0;
}

/*

 

*/