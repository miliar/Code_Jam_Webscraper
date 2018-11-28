#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <stdlib.h>
using namespace std;




long main(long argc, char * argv[])
{  
	char* InFileName = "A-large.in";
	char* OutFileName = "A-large.out";
	ifstream fileIn;
	ofstream fileOut; 

	fileIn.open(InFileName);
	fileOut.open(OutFileName);
	if(!fileIn)
		cout<<"Input file Open ERROR"<<endl;
	if(!fileOut)
		cout<<"Output file Open ERROR"<<endl;

	long totalCaseNum;
	fileIn>>totalCaseNum;
	cout<<"CaseNum: "<<totalCaseNum<<endl;

	for(long i = 0; i < totalCaseNum; i++)
	{
		long long vec_n;

		list<long  long>vec_A;
		list<long  long>vec_B;

		fileIn>>vec_n;
		long  long A_num,B_num;
		for (long j=0;j<vec_n;j++)
		{
			fileIn>>A_num;
			vec_A.push_back(A_num);
		}
		for (long j=0;j<vec_n;j++)
		{
			fileIn>>B_num;
			vec_B.push_back(B_num);
		}

		vec_A.sort();
		vec_B.sort();
		vec_B.reverse();
		  long  long  sum = 0;

		list<long  long >::iterator itA,itB;
		itA = vec_A.begin();
		itB = vec_B.begin();
		for ( long j=0;j<vec_n;j++)
		{
			sum+=(*itA)*(*itB);
			itA ++;
			itB++;			
		}
		fileOut<<"Case #"<<i+1<<": "<<sum<<endl;



	}//end testcase
	fileIn.close();
	fileOut.close();

	cout<<"FINISH";
	while(1);
		
}//end main