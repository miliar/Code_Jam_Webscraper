#include<iostream>
#include <fstream>
#include<cmath>
using namespace std;

int main()
{
	int prepare[31]; 
	int i=0;
	for(i=1;i<=30;i++)
	{
		prepare[i]=int(pow(2.0,i));
	}

	int T;
	int N;
	int K;
	ifstream fin("A-large.in");
	if(! fin)
	{
		cout<<"文件打开失败\n";
		return 0;
	}

	ofstream fout("ans.txt");
	if(! fout)
	{
		cout<<"文件输出打开失败\n";
		return 0;
	}
	fin>>T;
	for(i=1;i<=T;i++)
	{
		fin>>N;
		fin>>K;
		fout<<"Case #"<<i<<": ";
		if((K+1)%prepare[N]==0)
			fout<<"ON\n";
		else 
			fout<<"OFF\n";
	}
	return 0;
}
