// google-C.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
using namespace std;

struct round
{
	long r;
	long long money;
};

int _tmain(int argc, _TCHAR* argv[])
{
	long t,head,tail,c,count,r,k,n,i,room,cycle;
	long a[1000];
	long long money,cm;
	round bl[1000];
	ifstream fin("C-large.in",ios::binary|ios::in);
	ofstream fout("out.txt",ios::binary|ios::out);
	c=0;
	fin>>t;
	while (c<t)
	{
		fin>>r>>k>>n;
		for (i=0;i<n;i++) bl[i].r =0;
		for (i=0;i<n;i++)
		{
			fin>>a[i];
		}
		tail=0;
		count=0; money=0;
		while(count<r)
		{
			room=0; head=tail;
			if (bl[head].r>0) 
			{
				cycle=count+1-bl[head].r;
				cm=money-bl[head].money;
				money+=((r-count-1)/cycle)*cm;
				count+=((r-count-1)/cycle)*cycle;
			}
			else 
			{
				bl[head].r=count+1;
				bl[head].money=money;
			}
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

