#include<map>
#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{

	int i;
	map <int ,int >spl;
	map <int ,int >nonspl;

	spl[0] =0;
	nonspl[0] = 0;

	for(i=1;i<=30;i++)
	{
		if(i%3 == 1)
		{
			spl[i] = i/3+1;
			nonspl[i] = i/3+1;
		}
		else if(i%3 == 2)
		{
			spl[i] = i/3 + 2;
			nonspl[i] = i/3 + 1;
		}
		else
		{
			spl[i]  = i/3 + 1;
			nonspl[i] = i/3 ;
		}

	}

	int t,j;
	cin >> t;

	for(i=1;i<=t;i++)
	{
		int max = 0;
		int special = 0;
		int n,s,p;
		cin >> n;
		cin >>s;
		cin >> p;

		int a[n];

		for(j =0;j<n;j++)
			cin >> a[j];

		for(j =0;j< n;j++)
		{
			if(nonspl[a[j]] >= p) 
			{
				max ++;
			}
			else if (spl[a[j]] >=p && s!=0)
			{
				max++;
				s--;
			}
		}

		cout << "Case #"<<i <<": "<< max << endl;

	}
/*	for(i=0;i<=30;i++)
	{
		cout <<i<<"\t"<<nonspl[i]<<"\t"<<spl[i]<<endl;
	
	}
*/
	return 0;
}
