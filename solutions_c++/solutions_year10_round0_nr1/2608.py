#include<iostream>
#include<fstream>
using namespace std;
ifstream fin("A-small-attempt1.in");
ofstream fout("A-small-attempt1.out");
int ncase,N,K;
//***********************************
inline void oper(int &op)
{
	int i=0;
	int t=op;
	while(t&1)
	{
		op^=1<<i;
		++i;
		t>>=1;	
	}
	if(i<N)
	   op^=1<<i;
}
int main()
{
	fin>>ncase;
	int count=0;
	while(ncase--)
	{
		fin>>N>>K;
		//cin>>N>>K;
		int res=0;
		for(int i=0;i<K;++i)
			oper(res);
		int j=0;
		while(res&1)
		{
			++j;
			res>>=1;
		//	if(j>N+1)
		//		cout<<"eror"<<endl;
		}
		if(j>=N)
		   fout<<"Case #"<<++count<<": "<<"ON"<<endl;
		else fout<<"Case #"<<++count<<": "<<"OFF"<<endl;
	}
	return 0;
}