#include <stdio.h>
#include <algorithm>
using namespace std;
#define MAXN 1000
int n,d;
double arr[1000100];

bool apt(double t){
	double a = arr[0] - t;
	for (int i = 1;i < n;i++)
	{
		a += d;
		double b = arr[i] - t;
		if(a < b)
			a = b;
		if(a > arr[i] + t)
			return false;
	}
	return true;
}
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t,c;
	int p,v;
	double st,ed,mid;
	scanf("%d",&T);
	for (t = 1;t <= T;t++)
	{
		scanf("%d%d",&c,&d);
		n = 0;
		while (c--)
		{
			scanf("%d%d",&p,&v);
			while (v--)
				arr[n++] = p;
		}
		sort(arr,arr+n);
		st = 0;
		ed = 1e10;
		while (ed-st > 1e-8)
		{
			mid = (st + ed) /2;
			if (apt(mid))
				ed = mid;
			else
				st = mid;
		}
		printf("Case #%d: %.10f\n",t,ed);
	}
	return 0;
}