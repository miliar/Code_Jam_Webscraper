#include <iostream>
#include <vector>
using namespace std;

int n,t;
vector <int> a,b;

bool intresect(int x, int y)
{
	if ( (a[x]<a[y] && b[x]>b[y]) || (a[y]<a[x] && b[y]>b[x])) return true;
	else return false;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int q=1; q<=t; q++)
	{
		a.clear(); b.clear();
		int ans=0;
		scanf("%d", &n);
		a.resize(n); b.resize(n);
		for (int i=0; i<n; i++)
			scanf("%d %d",&a[i], &b[i]);
		for (int i=0; i<n; i++)
			for (int j=i+1; j<n; j++)
			if (intresect(i,j)) ans++;
		printf("Case #%d: %d\n",q,ans);
	}
}