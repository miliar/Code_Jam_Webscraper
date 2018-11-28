#include <iostream>
using namespace std;
int n;

int read_data()
{
	cin >> n;
	int i,res = 0,temp;
	for (i=1;i<=n;i++)
	{
		cin >> temp;
		if (temp != i) res++;
	}
	return res;
}
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int ans,t,i;
	cin >> t;
	for (i=1;i<=t;i++)
	{
		ans = read_data();
		printf("Case #%d: %d.000000\n",i,ans);
	}
}