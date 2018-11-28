#include<iostream>
#include<fstream>
#include<cstring>
#include<cmath>
#include<map>
#include<vector>
#include<algorithm>
#include<iterator>
#include<sstream>
#include<set>
using namespace std;

typedef unsigned long long uint64;
typedef long long int64;
bool binarysum(unsigned int *A, int N)//is zero?
{
	unsigned int sum=A[0];
	for(int i=1;i<N;i++)
	{
//		cout<<A[i]<<' '<<sum<<endl;
		unsigned re=0;
		for(int j=0;j<32;j++)
		{
			unsigned int mask=1;
			mask<<=j;
//			cout<<mask<<' '<<sum<<' '<<A[i]<<' '<<(mask&sum)<<':'<<(mask&(A[i]))<<endl;
			if(((mask&sum)^(mask&A[i]))!=0)re+=mask;
//			cout<<re<<endl;
		}
		sum=re;
	}
//	cout<<sum<<endl;
	if(sum==0)return true;
	else return false;
}

int main(int argc, char *argv[])
{
//readin file
	string file;
	if(argc!=2){cerr<<"0,1 or 2!"<<endl;exit(1);}
	switch(atoi(argv[1]))
	{
		case 0: file="test"; break;
		case 1: file="C-small"; break;
		case 2: file="C-large"; break;
		default: cerr<<"choose the correct file, 0(test),1(small),2(large)"<<endl;exit(1); break;
	}
	string ifilename=file+".in"; string ofilename=file+".out";
	ifstream input(ifilename.c_str());ofstream output(ofilename.c_str());

//read in number of events
	int T;
	input>>T;
	int N;

//main loop start
	for(int t=0;t<T;t++)
	{
		input>>N;
		unsigned A[N];
		for(int i=0;i<N;i++)input>>A[i];
		if(binarysum(A,N))
		{
			int x=*min_element(A,A+N);
			uint64 sum=0;
			for(int i=0;i<N;i++)
				sum+=A[i];
			sum-=x;
			output<<"Case #"<<t+1<<": "<<sum<<endl;
		}
		else
		{
			output<<"Case #"<<t+1<<": NO"<<endl;
		}

		cout<<"case : "<<t+1<<endl;
	}

	input.close();
	output.close();
	return 0;
}
