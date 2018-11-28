// temp.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "stdafx.h"
#include <string.h>
#include <assert.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
using namespace std;


struct point
{
	long long x;
	long long y;
};

bool isRight(const point &a,const point &b,const point &c)
{
/*	if((a.y-b.y)*(a.x-c.x)==(a.y-c.y)*(a.x-b.x))
		return false;*/
	if((a.x+b.x+c.x)%3!=0)
		return false;
	if((a.y+b.y+c.y)%3!=0)
		return false;
	return true;
}

void test_i(const int tm,//第i个用例
			long &n,
			const long long &A, 
			const long long &B, 
			const long long &C, 
			const long long &D, 
			const long long &x0, 
			const long long &y0, 
			const long long &M
			)
{
	cout<<"Case #"<<tm<<": ";
	//{BEGIN
	long num=0;
	vector<point> v;
	
	long long x=x0,y=y0;
	point pt;
	pt.x=x;
	pt.y=y;
	v.push_back(pt);
	for(long i=0;i<n-1;i++)
	{
		 x =(A * x + B)%M;
		 y =(C * y + D)%M;
		pt.x=x;
		pt.y=y;
		v.push_back(pt);
	}
	while(n>=3)
	{
		int i,j;
		for(i=1;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(isRight(v[0],v[i],v[j]))
					num++;
			}
		}
		v.erase(v.begin());
		n--;
	}
	//{END
	cout<<num<<endl;
}


int _tmain(long argc, _TCHAR* argv[])
{
	locale loc = locale::global(locale(""));
	ifstream inFile("C:\\Documents and Settings\\Administrator\\桌面\\GOOGLE_JAM\\a.in");
	if(!inFile)
	{
		cerr<<"ifstream error!"<<endl;
		return 1;
	}
	locale::global(loc);

	int N;inFile>>N;
	int i;
	long n;
	long long  A, B, C, D, x0, y0, M;
	for(i=1;i<=N;i++)
	{	
		inFile>>n>>A>>B>>C>>D>>x0>>y0>>M;
		::test_i(i,n,A, B, C, D, x0, y0, M);
	}	
	return 0;
}

/*		sort(array1.begin(), array1.end());
		sort(array2.begin(), array2.end(), greater<long long>());
*/
