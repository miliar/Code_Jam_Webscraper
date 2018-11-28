// TextMessage.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"

#include "vector"
#include "string"
#include "iostream"
#include "sstream"
#include "stdio.h"
#include "math.h"
#include "algorithm"
#include "fstream"
using namespace std;

int main()
{
	int N;
	ifstream fin("c:\\A-large.in");
	ofstream fout("c:\\TextMessage.txt");
	fin>>N;
	for(int i=0;i<N;i++)
	{
		int P,K,L;
		fin>>P>>K>>L;
		vector<int> freq;
		for(int j=0;j<L;j++)
		{
			int t;
			fin>>t;
			freq.push_back(t);
		}
		sort(freq.rbegin(),freq.rend());
		int cur=1; int left=K;
		long long ans=0;
		for(int j=0;j<freq.size();j++)
		{
			ans+=(long long)cur*freq[j];
			left--;
			if(left==0) left=K,cur++;
		}
		fout<<"Case #"<<i+1<<": "<<ans<<endl;
	}

	return 0;
}

