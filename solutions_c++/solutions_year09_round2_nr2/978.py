#include <iostream>
#include <fstream>
#include <stdlib.h>;
#include <math.h>
#include <string>
using namespace std;

int main()
{
	ifstream cin("b.in");
	ofstream cout("b.out");
    int t;
	cin>>t;
	int i;
	char a[100];
	int b[11];
	int j;
	int k;
	int max ;
	int q;
	bool p;
	for ( i = 0 ; i < t; i++)
	{
		cin>>a;
        for (j = 0; j < 11; j++)
        {
			b[j] = 0;
        }
		k = strlen(a);
		k--;
		max = a[k] - '0';
		b[a[k] - '0']++;
		if (k == 0) p = false;
		else p = true;
		while (k>0)
		{

			k--;
			b[a[k] - '0']++;
			if (a[k] - '0' >= max)
			{
				max = a[k] - '0';
			}
			else break;
			if (k == 0)
			{p = false;
			}
			
		}


		cout<<"Case #" << i+1 << ": ";


		if (p)
		{
			for (j = 0; j < k ; j++)
		{
			cout<<a[j];
		}
		b[a[k] - '0']--;
		for (j = a[k] - '0' + 1 ; j < 10; j++)
		{
			if (b[j] > 0)
			{
				cout<<j;
				b[j]--;
				break;
			}
		}
		b[a[k] - '0']++;
		for (j = 0; j< 10; j++)
		{
			for (q = 0; q < b[j]; q++)
			{
				cout<<j;
			}
		}
		}
		else
		{
			b[0]++;
			for (j = 1;j< 10;j++)
			{
				if (b[j] > 0)
				{
					cout<<j;
					b[j]--;
					break;
				}
			}
			for ( j = 0;j<10;j++)
			{
				for (q = 0; q < b[j];q++)
				{
					cout<<j;
				}
			}
		}
		

		
		
		cout<<endl;
	}

	
	return 0;
}