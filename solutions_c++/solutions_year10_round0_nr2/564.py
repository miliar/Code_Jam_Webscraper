// c.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include <iostream>
#include "hlp.h"
#include <set>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int C,N;
hp y,T,n,a,b;
set<hp> t;
set<hp> detat;
set<hp>::iterator it;

hp get_T(hp a, hp b)
{
	if (a<b)
	{
		swap(a,b);
	}
	if (iszero(b))
	{
		return a;
	}
	return get_T(a%b,b);
}

//hp get_T_other(hp a, hp b)
//{
//	if (a<b)
//	{
//		swap(a,b);
//	}
//	if (0==b)
//		return a;
//	if ((a%2==0)&&(b%2==0))
//	{
//		return 2*get_T_other(a/2,b/2);
//	}
//	if (a%2==0)
//	{
//		return get_T_other(a/2,b);
//	}
//	if (b%2==0)
//	{
//		return get_T_other(a,b/2);
//	}
//	return get_T_other((a+b)/2,(a-b)/2);
//}


int main()
{
	freopen("B-large.in.txt","r",stdin);
	freopen("output1.txt","w",stdout);
	cin>>C;
	string s;
	//cin>>s;
	//input(C,s);
	for (int i=0; i<C; i++)
	{
		if (i==8)
		{
			i=i;
		}
		cin>>N;
		//cin>>s;
		//input(N,s);
		t.clear();
		detat.clear();
		for (int j=0; j<N; j++)
		{
			//cin>>n;
			cin>>s;
			input(n,s);
			t.insert(n);
		}
		it=t.begin();
		N=t.size();
		for (int j=0; j<N-1; j++)
		{			
			b=(*it);
			it++;
			a=(*it);
			detat.insert(a-b);
		}
		it=detat.begin();
		T=(*it);
		for (int j=1; j<detat.size(); j++)
		{
 			it++;
			T=get_T(T,(*it));
		}
		detat.clear();
		it=t.begin();
		for (int j=0; j<N; j++)
		{
			detat.insert((T-(*it)%T)%T);
			it++;
		}
		if (detat.size()==1)
		{
			cout<<"Case #"<<i+1<<": ";
			print(*detat.begin());
		}
		else
		{
			cout<<"Case #"<<i+1<<": "<<0<<endl;	
		}
	}
	return 0;
}

