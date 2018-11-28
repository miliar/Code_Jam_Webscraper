#include <iostream>
using namespace std;

int t,n,i,j;
int a[1000],b[1000];

int process()
{
	int k,l;
	int ret = 0;
	for (k = 0; k < n; k++)
	{
		for (l = 0; l < n; l++)
		{
			if (l == k) 
				continue;
			
			if ( (a[k] > a[l] && b[k] < b[l]) || (a[k] < a[l] && b[k] > b[l]) )
				ret++;
			
		}
	}
	return ret/2;
}
int main()
{
	cin >> t;

	for (i = 0; i < t; i++)
	{
		cin >> n;
		for (j = 0; j < n; j++)
		{
			cin >> a[j] >> b[j];
		}
		cout << "Case #" << (i+1) << ": " << process() << endl;
	}
	return 0;
}