#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int arr[100000], r, i, T, n, p, e, s , j;
int masiv[10000];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>T;
	for (i=0; i<T; i++)
	{
		cin>>n>>s>>p;
		for (j=0; j<n; j++)
		{
			cin>>masiv[j];
		} 
		sort(masiv, masiv+n);
		for (j=n-1; j>=0; j--)
		{
			e=masiv[j]/3;
			if (e>=p)
			{
				r++;
			}
			else 
			{
			if (((masiv[j] % 3)>0) && (e+1>=p))
			{
				r++;
			}
			else 
			{
				if (s>0)
				{
					s--;
					if ((e+2>=p) && (masiv[j]>1) && (masiv[j] % 3==2))
						r++;
					if ((e+1>=p) && (masiv[j]>1))
						r++;
				}
			}
			}
		
		}
		cout<<"Case #"<<i+1<<": "<<r<<endl;
		r=0;
	}

}