#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
#define M 110
int n,K,B,T;
int data[M],v[M];

void read_data()
{
	cin >> n >> K >> B >> T;
	int i;
	for (i=1;i<=n;i++) cin >> data[i];
	for (i=1;i<=n;i++) cin >> v[i];
}

int work_ans()
{
	int i,cnt = 0,ans = 0,obt = 0;
	for (i=n;i>=1;i--)
	{
		if (data[i] + v[i] * T >= B)
		{
			ans += obt;
			cnt++;
		}
		else obt++;
		if (cnt == K) return ans;
	}
	return -1;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int ans,t,i;
	cin >> t;
	for (i=1;i<=t;i++)
	{
		read_data();
		ans = work_ans();
		cout << "Case #" << i << ": ";
		if (ans == -1) cout << "IMPOSSIBLE" << endl; else cout << ans << endl;
	}
	return 0;
}
