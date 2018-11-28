#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int caseCnt, caseNum;
	int Num;
	
	long sum ;
	long sum_xor ;
	long min ;
	long tmp;
		
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	fin>>caseCnt;
	for(int i=0; i<caseCnt; ++i)
	{
		sum = 0;
		sum_xor = 0;		
		
		fin>>Num;
		for(int j=0; j<Num; ++j)
		{
			fin>>tmp;
			if(j==0)
				min = tmp;
			else
				min = min>tmp?tmp:min;
			sum += tmp;
			sum_xor = sum_xor^tmp;		
		}	
		caseNum = i+1;
		
		if(sum_xor == 0)
			fout<<"Case #"<<caseNum<<": "<<(sum-min)<<endl;
		else
			fout<<"Case #"<<caseNum<<": "<<"NO"<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}