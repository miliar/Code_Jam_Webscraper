#include<iostream>
using namespace std;
int main(void)
{
	int i,j,h;
	int sum;
	int r,k,t,n;
	int total;
	int *g;
	cin >> t;
	for(h = 0; h < t; h++)
	{
		total = 0;
		sum = 0;
		j = 0;
		cin >> r >> k >> n;
		g = new int[n];
		for(i = 0; i < n; i++) cin >> g[i];
		for(i = 0; i < n; i++) sum += g[i];
		if(sum <= k)
		{
			total = r * sum;
		}	
		else
		{
			for(i = 0; i < r; i++)
			{
				sum = 0;
				while(sum <= k) 
				{
					sum = sum + g[j];
					j = ((j + 1) % n);
				}
				if(j == 0){j = n - 1;}
				else j = j - 1;
				sum = sum - g[j];
				total = total + sum;
			}
		}
		cout << "Case #" << h+1 << ": " << total << endl;
		delete []g;
	}	
	return 0;
}