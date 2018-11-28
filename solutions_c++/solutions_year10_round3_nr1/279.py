// A.cpp : 定义控制台应用程序的入口点。
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
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	
	int T;
	int N;
	int Left[1001],Right[1001];
	int i,j,k;
	int count=0;
	
	in>>T;
	for(k=1;k<=T;k++)
	{
		in>>N;
		for(i=0;i<N;i++)
			in>>Left[i]>>Right[i];

		count=0;
		for(i=0;i<N-1;i++)
			for(j=i+1;j<N;j++)
				if((Left[i]-Left[j])*(Right[i]-Right[j])<0)
					count++;
		out<<"Case #"<<k<<": "<<count<<endl;

	}

	
	in.close();
	out.close();
	return 0;
}

