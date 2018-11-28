#include <iostream>
#define maxn 2001
using namespace std;
int t,n,k,r;
unsigned long long a[maxn],money[maxn],num[maxn];
int used[maxn];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C_large.out","w",stdout);
	int i,j;
	cin >> t;
	for (int tn=1;tn<=t;tn++)
	{
		cin >> r >> k >> n;
		for (i=0;i<n;i++)
			cin >> a[i];
		memset(num,0,sizeof num);
		memset(used,0,sizeof used);
		memset(money,0,sizeof money);
		int now=0,nownum=0;
		int aa;
		for (i=1;i<=n+1;i++)
		{
			int beg=now;
			while (nownum+a[now]<=k)
			{
				nownum+=a[now++];
				now%=n;
				if (now==beg) break;
			}
			num[i]=(now+n-1)%n;
			money[i]=money[i-1]+nownum;
			if (used[(now+n-1)%n])
			{
				aa=used[(now+n-1)%n];
				break;
			}
			used[(now+n-1)%n]=i;
			nownum=0;
		}
		long long ans=(r-aa)/(i-aa)*(money[i]-money[aa]);
		r=(r-aa)%(i-aa);
		ans+=money[aa+r];
		cout << "Case #" << tn << ": " << ans << endl;
	}
}