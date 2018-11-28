// console.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <algorithm>
#include <conio.h>
#include <iostream>

using namespace std;


//	_getch();

	int _tmain(int argc, _TCHAR* argv[])
{
	//freopen("C:\\users\\lxy\\downloads\\practice.in","r",stdin);
	//freopen("C:\\users\\lxy\\downloads\\C-small-attempt0.in","r",stdin);
	freopen("C:\\users\\lxy\\downloads\\C-large.in","r",stdin);
	freopen("C:\\users\\lxy\\downloads\\out","w",stdout);

	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n;
		cin>>n;
		int xor,sum,min,tmp;
		cin>>sum;
		min=xor=sum;
		for(int j=1;j<n;j++)
		{
			cin>>tmp;
			xor^=tmp;
			sum+=tmp;
			min=tmp>min?min:tmp;
		}
		if(xor!=0)
			cout<<"Case #"<<i+1<<": "<<"NO"<<endl;
		else
			cout<<"Case #"<<i+1<<": "<<sum-min<<endl;
	}

}

