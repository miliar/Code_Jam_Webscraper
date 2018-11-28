#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

struct tpoint{double x,y,r;};

int test,n;
tpoint a[4];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	cin >> test;
	for (int tt=1; tt<=test; tt++) {
		printf("Case #%i: ", tt);
		cin >> n;
		for (int i=0; i<n; i++)
			cin >> a[i].x >> a[i].y >> a[i].r;

		if (n==1) {
			printf("%.5lf\n",a[0].r);
			continue;
		}
		if (n==2) {
			printf("%.5lf\n",max(a[0].r,a[1].r));
			continue;
		}

		double mx=1000000000;
		int l, r;
		for (int i=0; i<n; i++)
			for (int j=i+1; j<n; j++)
				if (sqrt( (double) ((a[i].x-a[j].x)*(a[i].x-a[j].x)+(a[i].y-a[j].y)*(a[i].y-a[j].y)))+a[i].r+a[j].r<mx) {
					mx=sqrt( (double) ((a[i].x-a[j].x)*(a[i].x-a[j].x)+(a[i].y-a[j].y)*(a[i].y-a[j].y)))+a[i].r+a[j].r;
					l=i;
					r=j;
				}
		mx/=2.0;
		int y=0;
		if (y==l || y==r) y++;
		if (y==l || y==r) y++;

		if (a[y].r>mx) mx=a[y].r;
		printf("%.5lf\n",mx);
	}

	return 0;
}
