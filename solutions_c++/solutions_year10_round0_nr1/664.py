// Snapper Chain(gcj2010).cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"

#include "stdio.h"
#include <fstream>
using namespace std;
int main()
{
	int ts,n,k,p;
	ifstream f("d:\\gcj\\A-small-attempt0.in");
	ofstream of("d:\\gcj\\A-small.out");
	if(f!=NULL)
	{
		f>>ts;
		for(int t=1;t<=ts;t++)
		{
			f>>n>>k;
			p=1;
			for(int i=0;i<n;i++)
				p=p<<1;
			p--;
			if((k&p)==p)
				of<<"Case #"<<t<<": "<<"ON "<<endl;
			else
				of<<"Case #"<<t<<": "<<"OFF "<<endl;
		}
	}
	return 0;
}

