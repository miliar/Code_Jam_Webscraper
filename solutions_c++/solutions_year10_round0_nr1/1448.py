// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <set>
#include <vector>
#include <bitset>
#include <list>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	fstream in("A-large.in",ios::in);
	fstream out("A-large.out",ios::out);

	int T;
	unsigned long N,K;
	int i,j;
	in>>T;
	
	bitset<32> bs;
	for(i=0;i<T;i++)
	{
		in>>N>>K;
		bitset<32> bs(K);
		
		for(j=0;j<N;j++)
		{
			if(bs.test(j)==0)
				break;
		}

		if(j==N)
			out<<"Case #"<<i+1<<": "<<"ON"<<endl;
		else
			out<<"Case #"<<i+1<<": "<<"OFF"<<endl;
	}


	in.close();
	out.close();
	return 0;
}

