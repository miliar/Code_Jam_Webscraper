// google-C.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	long t,head,tail,c,money,count,r,k,n,i,room;
	long a[100];
	ifstream fin("C-small-attempt6.in",ios::binary|ios::in);
	ofstream fout("out.txt",ios::binary|ios::out);
	c=0;
	fin>>t;
	while (c<t)
	{
		fin>>r>>k>>n;
		for (i=0;i<n;i++)
		{
			fin>>a[i];
		}
		tail=0;
		count=0; money=0;
		while(count<r)
		{
			room=0; head=tail;
			while (room<k)
			{
				if (room+a[tail]<=k) 
				{
					room+=a[tail];
					tail++; 
					tail=tail%n;
					if (tail==head) break;
				}
				else break;
			}
			count++;
			money+=room;
		}
		fout<<"Case #"<<c+1<<": "<<money<<endl;
		c++;
	}
	return 0;
}

