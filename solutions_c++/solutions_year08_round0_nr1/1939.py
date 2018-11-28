// codejam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <map>
#include <iostream>
#include <string>
#include <bitset>
using namespace std;

map<string,int> sm;
int _tmain(int argc, _TCHAR* argv[])
{
	bitset<200> bs;

	int N;
	cin >>  N;
	for(int n=0;n<N;n++)
	{
		bs.reset();
		sm.clear();
		int K;
		cin >>  K;
		string s;
		getline(cin,s);
		for(int k=0;k<K;k++)
		{
			std::getline(cin,s);
//			cout << s <<endl;
			sm[s]=k;
		}
		int T=0;
		int M;
		cin >>  M;
		getline(cin,s);
		for(int m=0;m<M;m++)
		{
			std::getline(cin,s);
			bs.set(sm[s]);
			if(bs.count()==K)
			{
				T++;
//				cout << bs << endl;
				bs.reset();
				bs.set(sm[s]);
			}
		}
		cout << "Case #" << n+1 <<": " << T <<endl;
	}

	return 0;
}

