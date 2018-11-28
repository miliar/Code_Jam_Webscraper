// problem2.cpp : Defines the entry point for the console application.
//


#include<fstream>
using namespace std;
int main()
{
	int T,N,S,p;
	int sur,result,temp;
	ifstream fin("B-large.in");
	ofstream fout("B-small-attempt.out");
	fin>>T;
	for(int i=0;i<T;i++)
	{
		result=0;
		sur=0;
		fin>>N>>S>>p;
		
		for(int j=0;j<N;j++)
		{
			fin>>temp;
			if(temp>3*p-3)result++;
			else if((temp>=p)&&(temp<=3*p-3)&&(temp>=3*p-4))sur++;
		}
		result+=sur<S?sur:S;
		fout<<"Case #"<<i+1<<": "<<result;
		if(i<T-1)fout<<endl;
	}
	return 0;
}


