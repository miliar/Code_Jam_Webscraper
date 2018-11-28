#include<iostream>

#include<fstream>


using namespace std;

ifstream in("A.in");
ofstream out("A.out");
int main()
{
	int T;
	in>> T;
	int N,K;
	for(int i=0;i<T;i++)
	{
		in>>N>>K;
		int tmp = (1<<N)-1;
		if((tmp&K)==tmp)
			out<<"Case #"<<i+1<<": "<<"ON"<<endl;
		else
			out<<"Case #"<<i+1<<": "<<"OFF"<<endl;



	}
	return 0;
}