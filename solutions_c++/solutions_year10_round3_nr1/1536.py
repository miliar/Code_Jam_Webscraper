#include <iostream>
#include <fstream>
#include <stdlib.h>;
#include <math.h>
using namespace std;
int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	
	
		
	int a[2000][2];
	int t;
	cin>>t;
	int i;
	int n;
	int j;
	int k;
	int b[2000];
	for (i = 0 ; i < t; i++)
	{
		cin>>n;
		for (j = 0; j < n ; j++)
		{
			cin>>a[j][0]>>a[j][1];

		}
		
		for (j = 0 ; j< n; j++)
		{
			b[j] = j;
		}
		for (j = 0 ; j < n-1; j++)
		{
			for (k = j+1; k < n; k++)
			{
				if (a[j][0] > a[k][0])
				{
					int k1,k2;
					k1 = a[j][0];
					k2 = a[j][1];
					a[j][0] = a[k][0];
					a[j][1] = a[k][1];
					a[k][0] = k1;
					a[k][1] = k2;

				}
			}
		}

		for (j = 0 ; j < n-1; j++)
		{
			for (k = j+1; k < n; k++)
			{
				if (a[j][1] > a[k][1])
				{
				int k1,k2;
				
				k2 = a[j][1];
				
				a[j][1] = a[k][1];
				
				a[k][1] = k2;
				int r;
				r = b[j];
				b[j] = b[k];
				b[k] = r;
				}
			}
		}
		int num;
		num = 0;
		for (j = 0 ; j < n; j++)
		{
			if (j < b[j])
			{
				num+=b[j] - j;
			}
		}
		cout<<"Case #"<<i+1<<": "<<num<<endl;

	}


	
	return 0;
}