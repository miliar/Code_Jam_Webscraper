// d.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include <algorithm>

#include <iostream>
#include <math.h>
#include <string>
#include <set>
#include <float.h>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	freopen("A-large.in.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,N,n1,n2;
	set<pair<int,int>> A;
	set<pair<int,int>>::iterator it,it1;
	cin>>T;
	for (int i=0; i<T; i++)
	{
		cin>>N;
		A.clear();
		for (int j=0; j<N; j++)
		{
			cin>>n1>>n2;
			A.insert(make_pair(n1,n2));
		}
		int count1=0;
		for (it=A.begin(); it!=A.end(); it++)
		{
			it1=it;it1++;
			for (;it1!=A.end(); it1++)
			{
				if (it->second>it1->second)
				{
					count1++;
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<count1<<endl;

	}
	return 0;
}

