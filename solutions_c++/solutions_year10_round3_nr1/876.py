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

int main(int argc, char *argv[])
{
	if(argc != 3)
	{
		cout << "incorrect args\n";
		return -1;
	}
//	ifstream infile("B-small.txt");
//	ofstream outfile("B-small.out");
//	ifstream infile("B-small-attempt2.in");
//	ofstream outfile("B-small-attempt2.out");
//	ifstream infile("B-large-practice.in");
//	ofstream outfile("B-large-practice.out");
	
	string in(argv[1]);
	string out(argv[2]);
	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);
	
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
	infile >> numTestCases;
	for(int i = 1; i<= numTestCases; i++)
	{
		 int n;
		int A[1000],B[1000], can[50];
		int timeR[50];
		std::map<int, int> win;
		//Input testcase
		infile >> n;
		cout << "num is "<<n<<endl;
		int sum = 0;
		for(int j=0;j<n;j++)
		{
			infile >> A[j];
			infile >> B[j];
		//	win[A[j]]=B[j];
		}
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<n;k++)
			{
				if(k==j)
					continue;
		
				if((A[j]<A[k]) && (B[j]>B[k]))
					sum++;
			}

		}
		
		//Process

		//Output result
			outfile << "Case #"<< i <<": " << sum<<"\n";

	}

}
