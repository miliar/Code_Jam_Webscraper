#include <iostream>
#include <string>
          
using namespace std;

int l,d,n,i,j,k,x,ans;
string s[5001];
string c;
bool a[20][500];

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	cin >> l >> d >> n;
	for (i = 1;i<=d;i++)
		cin >> s[i];
	for (i = 1;i<=n;i++)
	{
		ans = 0;
		memset(a,0,sizeof(a));
		cin >> c;
		x = 0;
		j = 0;
		while (x<c.length())
		{
			if (c[x] != '(')
			{
				a[j][c[x]-'0'] = 1;		
			}
			else
			{
				x++;
				while (c[x] != ')')
				{
					a[j][c[x]-'0'] = 1;
					x++;
				}	
			}
			j++;
			x++;
		}
		for (j = 1;j<=d;j++)
		{
			bool r = false;
			for (k = 0;k<l;k++)
				if (a[k][s[j][k]-'0'] == 0)
				{
					r = true;
					break;
				}
			if (r == false) ans++;
		}	
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}                              