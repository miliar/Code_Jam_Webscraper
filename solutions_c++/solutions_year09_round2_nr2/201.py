#include <iostream>
#include <algorithm>
using namespace std;

int t,p,i,j,k,m,n;
string s;
int a[30];
int c[10];
bool ok;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin >> t;
	for (p=1; p<=t; p++)
	{
		cin >> s;
		cout << "Case #" << p << ": ";
		n=s.size();
		for (i=0; i<n; i++)
			a[i+1]=s[i]-48;
		
		
		ok=true;
		for (i=1; i<n; i++)
			if (a[i]<a[i+1]) ok=false;
		if (ok)
		{
			memset(c,0,sizeof(c));
			for (i=1; i<=n; i++)
				c[a[i]]++;
			c[0]++;
			for (i=1; i<=9; i++)
				if (c[i]) {c[i]--; cout << i; break;}
			for (i=0; i<=9; i++)
				for (j=1; j<=c[i]; j++)
					cout << i;
			cout << endl;
		}
		else
		{
			for (i=n; i>1; i--)
				if (a[i]>a[i-1])
				{
					k=10;
					memset(c,0,sizeof(c));
					for (j=i; j<=n; j++)
					{
						c[a[j]]++;
						if (a[j]>a[i-1]) k=min(k,a[j]);
					}
					c[a[i-1]]++;
					c[k]--;
					for (j=1; j<i-1; j++)
						cout << a[j];
					cout << k;
					for (j=0; j<=9; j++)
						for (k=1; k<=c[j]; k++)
							cout << j;
					cout << endl;
					break;
				}
		}
		
	}


//	system("pause");
	return 0;
}
