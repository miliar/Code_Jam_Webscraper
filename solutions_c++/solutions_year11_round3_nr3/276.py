#include <iostream>
#include <string>

using namespace std;

int n,a[1000];
int l,w;

void doing()
{
	cin >> n >> l >> w;
	for (int i=0;i<n;i++) cin >> a[i];
	for (int i=l;i<=w;i++)
	{
		for (int j=0;j<=n;j++)
		{
			if (j==n)
			{
				cout << i << endl;
				return;
			}
			if (!((a[j]%i==0) || (i%a[j]==0))) break;
		}
	}
	cout << "NO" << endl;
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int casenum;
	scanf("%d\n",&casenum);
	for (int cc=1;cc<=casenum;cc++)
	{
		printf("Case #%d: ",cc);
		doing();
	}
}
