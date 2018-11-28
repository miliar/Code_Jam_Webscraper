#include <iostream>

using namespace std;
long long ans;
long r,K,n,i,j,l;
long g[1005],s[1005],next[1005];

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T;
	cin >> T;
	for(l=0;l<T;l++)
	{
		cin >> r >> K >> n;
		ans = 0;
		for(i=0;i<n;i++)
		{
			cin >> g[i];
			g[i+n] = g[i];
		}
		for(i=0;i<n;i++)
		{
				s[i] = 0;j=0;
				while(j < n && s[i] <= K)
				{
					s[i] += g[i+j];
					j++;
				}
				j--;
				if(s[i] > K)
					s[i] -= g[i+j];
				next[i] = (i+j)%n;
		}
		j = 0;
		for(i=0;i<r;i++)
		{
			ans += s[j];
			j = next[j];
		}
		cout << "Case #" << l+1 << ": " << ans << endl;
	}
	return 0;
}
