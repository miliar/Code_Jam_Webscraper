#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
	ifstream infile("C:\\Users\\qingpingw\\Desktop\\A-small-attempt0.in");
	ofstream outfile("C:\\Users\\qingpingw\\Desktop\\A-small.txt");
	int test;
	int N,K;
	int i;
	infile>>test;
	i=1;
	while(i<=test)
	{
		infile>>N>>K;
		N=1<<N;
		if((K+1)%N)
		{
			printf("Case #%d: OFF\n",i);
			outfile<<"Case #"<<i<<": OFF"<<endl;
		}
		else
		{
			printf("Case #%d: ON\n",i);
			outfile<<"Case #"<<i<<": ON"<<endl;
		}
		i++;
	}
	system("pause");
	return 0;
}
			

