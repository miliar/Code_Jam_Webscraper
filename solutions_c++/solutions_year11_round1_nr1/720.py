// console.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <algorithm>
#include <conio.h>
#include <iostream>

using namespace std;


//	_getch();
//char ac[40*2];
//char at[40];
//char ad[40*2];
//char an[200];
//char ao[200];

int gcd(int a, int b)
{
    while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}

int _tmain(int argc, _TCHAR* argv[])
{
	//freopen("C:\\users\\lxy\\downloads\\practice.in","r",stdin);
	//freopen("C:\\users\\lxy\\downloads\\B-small-attempt2.in","r",stdin);
	freopen("C:\\users\\lxy\\downloads\\A-large (1).in","r",stdin);
	freopen("C:\\users\\lxy\\downloads\\out","w",stdout);

	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		long long n;
		int pd,pg;
		cin>>n>>pd>>pg;
		if(pg==100)
		{
			if(pd==100)
				cout<<"Case #"<<i+1<<": Possible"<<endl;
			else
				cout<<"Case #"<<i+1<<": Broken"<<endl;
		}
		else if(pg==0)
		{
			if(pd==0)
				cout<<"Case #"<<i+1<<": Possible"<<endl;
			else
				cout<<"Case #"<<i+1<<": Broken"<<endl;
		}
		else
		{
			int cc=gcd(pd,100);
			if(100/cc<=n)
				cout<<"Case #"<<i+1<<": Possible"<<endl;
			else
				cout<<"Case #"<<i+1<<": Broken"<<endl;

		}
	}

}

