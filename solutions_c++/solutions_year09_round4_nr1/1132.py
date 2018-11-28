#include <iostream>
#include <algorithm>

using namespace std;

int x[100][100];
int row[100];

int main ()
{
	freopen("input.txt","r", stdin);
	freopen("output.txt","w", stdout);

	int t;
	cin >> t;
	for (int T = 1; T<=t; T++)
	{
		int n;
		cin >> n;
		for (int i=0; i<n; i++)
		{
			row[i]=0;
			for (int j=0; j<n; j++)
			{
				char c;
				
				do
				{
					cin >> c;
				}
				while (c!='0' && c!='1');
				
				x[i][j] = (c=='1');
				if (x[i][j] == 1)
					row[i] = j;
			}
		}
		
		
		int ans=0;
		
		for (int i=0; i<n; i++)
		{
			int j = i;
			while (row[j]>i) j++;
			
			for (int k=j; k>i; k--)
			{
				swap(row[k], row[k-1]);
				ans++;
			}
		}
		
		cout << "Case #" << T << ": " << ans << endl;
	}

	
    return 0;
}
