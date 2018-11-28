// B.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <iomanip>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");

	int T,C;
	long double L,P;
	int i,j,k;
	long double temp;
	int count;

	in>>T;
	for(k=1;k<=T;k++)
	{
		count=0;
		in>>L>>P>>C;
		temp=P/L;
		if(temp>C)
			count++;
		while(sqrt(temp)>C)
		{
			count++;
			temp=sqrt(temp);
		}
		out<<"Case #"<<k<<": "<<count<<endl;


	}


	in.close();
	out.close();
	return 0;
}