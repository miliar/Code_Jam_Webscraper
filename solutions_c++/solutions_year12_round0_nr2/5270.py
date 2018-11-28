#include <iostream>

using namespace std;

int t,n[100],s[100],p[100][100],a[100],ans[100];

int main()
{
	cin>>t;
	for (int f1 = 0; f1 < t; f1++)
	{
		cin>>n[f1]>>s[f1]>>a[f1];
		for (int f2 = 0; f2 < n[f1]; f2++)
		{
			cin>>p[f1][f2];
		}
	}
	for (int f1 = 0; f1 < t; f1++)
	{
		for (int f2 = 0; f2 < n[f1]; f2++)
		{
			if (p[f1][f2] > (a[f1]*3)-3)
			{
				ans[f1]++;	
			}
			else if (p[f1][f2] < 1)
			{
				
			}
			else if (p[f1][f2] > (a[f1]*3)-5)
			{
				if (s[f1] > 0)
				{
					ans[f1]++;
					s[f1]--;
				}
			}
		}
	}
	for (int f1 = 0; f1 < t; f1++)
	{
		cout<<"Case #"<<f1+1<<": "<<ans[f1]<<endl;
	}
}