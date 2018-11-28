#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int input()
{
	int T = 0;
	int R = 0;
	int K = 0;
	int N = 0;
	vector<long> vl;

	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	
	if(fin==NULL || fout==NULL)
	{
		cout<<"Open file fails!"<<endl;
		exit(1);
	}
	int i = 0, j = 0;
	long tem = 0;
	long sum = 0;
	int count = 0;
	int add = 0;
	int num = 0;

	fin>>T;
	while(fin>>R)
	{
		i++;

		fin>>K>>N;
		vl.resize(N);
		
		for(j=0; j<N; j++)
		{
			fin>>vl[j];
		}

		sum = 0;
		tem = 0;
		count = 0;
		add = 0;
		num = 0;

		for(count=0; count<R; count++)
		{
			tem = 0;
			num = 0;
			while((tem+vl[add])<=K && num<N)
			{
				tem += vl[add];
				add = (add+1)%N;
				num++;
			}
			sum += tem;
		}

		cout<<"Case #"<<i<<": "<<sum<<endl;
		fout<<"Case #"<<i<<": "<<sum<<endl;	
	}

	return 0;
}

int main()
{
	input();
	return 0;
}