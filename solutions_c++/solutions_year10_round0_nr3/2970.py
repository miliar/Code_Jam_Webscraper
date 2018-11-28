#include <iostream>

using namespace std;

int main()
{
	int t,r,k,n,i,j;
	int q[1000], c[1000],e[1000];
	int earn;
	cin >> t;
	
	for (i = 1; i <= t; i++)
	{
		

		cin >> r >> k >> n;
		for (j=0; j<n;j++) 
		{
			cin >> q[j];
		}
		int sum=0;
		int di=0;
		int jj;
		j=0;
		for (j = 0; j<n;j++)
		{
			sum=q[j];
			for (jj = j+1; jj<n+n;jj++)
			{
				if (sum + q[jj%n] > k || (jj%n)==j)
				{
					c[j]=jj-j;
					e[j]=sum;
					break;
				}
				sum+=q[jj%n];
			}
		}
		earn = 0;
		di=0;
		for (j=0; j<r;j++)
		{
			earn+=e[di];
			di+=c[di];
			di=di%n;
		}
		cout << "Case #" << i << ": " << earn <<endl;
	}
	return 0;
}