#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <algorithm>

using namespace std;
struct str
{
	int x,y;
};
str k[1002];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t,i,j,n;
	long long ans;
	cin >> t;
	for(int ti=1;ti<=t;ti++)
	{
		cin >> n;ans = 0;
		for(i=0;i<n;i++)
			cin >> k[i].x >> k[i].y;
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
			{
				if(k[j].x > k[i].x && k[j].y < k[i].y) ans++;
			}
		cout << "Case #" << ti << ": " << ans << endl;
	}
	return 0;
}
