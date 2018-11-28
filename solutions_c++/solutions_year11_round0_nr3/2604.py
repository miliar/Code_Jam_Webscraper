// main.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("C-large.in.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	long int res,sum=0;
	int i,j;
	for(i=1;i<=t;i++)
	{
		res=0;
		sum=0;
		int num_chisla;
		long int chislo;
		long int min_chislo=2000000;

		cin>>num_chisla;
		for(int j=0;j < num_chisla; j++)
		{
			cin>>chislo;
			if(chislo<min_chislo)min_chislo=chislo;
			res=res^chislo;
			sum+=chislo;
		}
		if(res==0)cout<<"Case #"<<i<<": "<<sum-min_chislo<<endl;
		else cout<<"Case #"<<i<<": NO"<<endl;
	}
	//system("pause");
	return 0;
}

