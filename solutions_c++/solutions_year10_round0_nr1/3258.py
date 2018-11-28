#include<iostream>
#include<stdlib.h>
#include<fstream>
#include<string>
#include<map>
#include<algorithm>
#include<list>
#include<math.h>
#include<vector>
#include <stdint.h>

using namespace std;

int main()
{
	ifstream infile("A-large.in");
	ofstream outfile("A-large-output.txt");
	
	if(!infile)
	{
		cout<<"Error opening inout file";
		return 1;
	}
	if(!outfile)
	{
		cout<<"Error opening output file";
		return 1;
	}
	int numTestCases;
	int num, k;
	infile >> numTestCases;
	for(int i = 1; i<= numTestCases; i++)
	{
		//Input testcase
		infile >> num;
		infile >> k;
		cout << "num is "<<num<<endl;
		cout << "k is "<<k<<endl;

		//Process
		int cyc_len = pow(2,num);
		bool flag = ((k%cyc_len) == (cyc_len - 1));
		
		//Output result
		if(flag)
			outfile << "Case #"<< i <<": ON" << "\n";
		else
			outfile << "Case #"<< i <<": OFF"<< "\n";
	}

}
