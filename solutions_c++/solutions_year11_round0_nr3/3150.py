#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector <int> c;
int main()
{
	int t;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int qw=1; qw<=t; qw++)
	{		
		printf("Case #%d: ",qw);
		c.clear();
		int n,k;
		int q;
		scanf("%d",&n);
		for (int i=0; i<n; i++)
		{scanf("%d",&k); c.push_back(k);}
		k=c[0]; 
		for (int i=1; i<n; i++) k^=c[i];
		if (k) { printf("NO\n"); continue;}
		k=c[0];
		for (int i=1; i<n; i++) k+=c[i];
		k-=*min_element(c.begin(),c.end());
		printf("%d\n", k);
	}
	return 0;
}