#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

int v,i,j,t,p,q,k,x,y,ans;
int a[101],b[101];

int main()
{
	freopen("c.in","rt",stdin);
	freopen("c.out","wt",stdout);
	cin >> t;
	for (v = 1;v<=t;v++)
	{
		cin >> p >> q;
		for (i = 1;i<=q;i++)
			cin >> b[i];
		sort(b+1,b+q+1);
		ans = 10000000;
		do
		{
			memset(a,0,sizeof(a));
			k = 0;
			for (i = 1;i<=q;i++)
			{
				a[b[i]] = 1;
				x = b[i]-1;
				while ((x>=1)&&(a[x] == 0))
				{
					k++;
					x--;
				}
				x = b[i]+1;
				while ((x<=p)&&(a[x] == 0))
				{
					k++;
					x++;
				}			
			}
			ans = min(ans,k);	
		}while (next_permutation(b+1,b+q+1));          		
		cout << "Case #" << v << ": " << ans << endl;
	}
	return 0;
}



