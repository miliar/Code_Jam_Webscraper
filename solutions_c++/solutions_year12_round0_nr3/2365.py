#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for (int ctr = 0; ctr < t; ctr++)
	{
		long long sum=0;
		long long i;
		long long l=1111, u=2222;
		cin>>l>>u;
		
		int n_digits=0;
		long long temp = l;
		while(temp!=0)
		{
			n_digits++;
			temp/=10;
		}
		for (i = l; i < u; i++)
		{
			long long save = i;
			long long temp = save;
			for (long long j = 0; j < n_digits-1; j++)
			{
				long long x = temp%10;
				temp = temp/10;
				while (x == 0 && temp > 0 && j<n_digits-1)
				{
					x = temp%10;
					temp = temp/10;
					j++;
				}
				if(j == n_digits-1)
					break;
				long long nt;
				nt = x*pow(10, n_digits-1) + temp;
				
				if(nt >= l && nt <= u && nt > save)
				{
					//fmap[i]++;
					sum++;
					temp = nt;
					//cout<<save<<" "<<nt<<endl;
				}
				else if(nt == save)
				{
					break;
				}
				else
				{
					temp = nt;
				}
			}
		}
		cout<<"Case #"<<ctr+1<<": "<<sum<<endl;
	}
}
