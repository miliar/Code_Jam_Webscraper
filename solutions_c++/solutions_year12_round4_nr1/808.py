#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
using namespace std;
const int MAXN=10000;
struct Node {
	int d,l,t;
} a[MAXN+10];
int n,d;
void ReadIn()
{
	scanf("%d",&n);
	for (int i=1;i<=n;i++) {
		scanf("%d%d",&a[i].d,&a[i].l);
		a[i].t=0;
	}
	scanf("%d",&d);
}
bool YES()
{
	a[1].t=a[1].d;
	for (int i=1;i<=n;i++) {
		if (a[i].d+a[i].t>=d) return true;
		for (int j=i+1;j<=n && (a[j].d-a[i].d)<=a[i].t;j++)
			a[j].t=max(a[j].t,
						min(a[j].d-a[i].d,a[j].l));
	}
	return false;
}
int main()
{
	int cases;
	scanf("%d",&cases);
	for (int c=1;c<=cases;c++) {
		ReadIn();
		if (YES()) printf("Case #%d: YES\n",c);
		else printf("Case #%d: NO\n",c);
	}
	return 0;
}
