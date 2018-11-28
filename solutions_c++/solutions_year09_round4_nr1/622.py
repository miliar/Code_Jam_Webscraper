#include <iostream>
using namespace std;
#define tiao system("pause")

int n;
int t;
int a[111];
char s[111];

int main(void)
{
	int i,j,k,ci,cici,cicici;
	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	cin >> t;
	for (cicici=1; cicici<=t; cicici++)
	{
		cin >> n;
		char ch;
		
		memset(a,0,sizeof(a));
		for (i=1; i<=n; i++)
		{
			cin >> s;
			int cnt(0);
			for (j=n-1; j>=0; j--)
			{
				if (s[j] == '0') cnt++;
				else break;
			}
			a[i] = cnt;
		}
		
		int ans = 0;
		for (i=1; i<=n; i++)
		{
			for (j=i; j<=n; j++)
			{
				if (a[j] >= n-i)
				{
					for (k=j; k>i; k--)
					{
						swap(a[k], a[k-1]);
						ans++;
					}
					
					break;
				}
			}
		}
		
		cout << "Case #" << cicici << ": " << ans << endl;
	}
//	tiao;
	return 0;
}

