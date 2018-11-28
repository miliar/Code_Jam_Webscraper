#include <iostream>

using namespace std;
int t , n , k , i , j;
int a[40] , p[40];
int main()
{
	freopen("d:/input.txt" , "r" , stdin);
	freopen("d:/output.txt" , "w" , stdout);
	cin>>t;
	for (int tt = 1; tt <= t; tt++)
	{
		cin>>n>>k;
		/*
		for (i = 0; i < n; i++)
		{
			a[i] = 0;
			p[i] = 0;
		}

		p[0] = 1;

		for (i = 0; i < k; i++)
		{
			for (j = 0; j < n; j++)
			if (p[j])
				a[j] = 1 - a[j];

			for (j = 0; j < n; j++)
				p[j] = 0;

			p[0] = 1;
			if (a[0])
			{
				for (j = 1; j < n && a[j] == 1; j++)
					p[j] = 1;
				p[j] = 1;
			}

			
		}
		*/

		cout<<"Case #"<<tt<<": ";
		if ((k + 1) % (1<<n) == 0)
			cout<<"ON"<<endl; else
			cout<<"OFF"<<endl;

		

	}

	

	return 0;
}