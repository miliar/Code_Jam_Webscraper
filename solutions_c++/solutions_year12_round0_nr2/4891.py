//
#include <iostream>
#include <string>
#include <fstream>

using namespace std;


int numcal(int N,int S,int p,int* t )
{
	int num,ns_num=0,s_num=0;
	if (p==0)
		return N;
	else 
		{
			
	    int ns_value=3*p-2;
	    int s_value=3*p-4;
		for(int n=0;n<N;n++)
	{
		if (t[n]>=ns_value)
			ns_num++;
		else if (t[n]>=s_value)
			s_num++;
	}
		if (p==1)
		s_num=0;
	
	if (s_num<=S)
		num=ns_num+s_num;
	else
		num=ns_num+S;
	return num;
	}
}
int main()
{   
	//ifstream fin("A-small-practice.in");
	ifstream fin("B-large.in");
	int T;
	fin>>T;
	cout<<T;
	//ofstream fout("A-small-practice.out");
	ofstream fout("B-large.out");	
	
	int N,S,p;
	






	for (int n=1;!fin.eof();n++)
	{
		fin>>N>>S>>p;
			int* t=new int[N];
			for (int t1=0;t1<N;t1++)
		       { fin>>t[t1];
			cout<<t[t1];
			}
		int num=numcal(N,S,p,t);
			
		fout<<"Case #"<<n<<": "<<num<<endl;
		delete []t;
	}
	
	
	
	return 0;
}