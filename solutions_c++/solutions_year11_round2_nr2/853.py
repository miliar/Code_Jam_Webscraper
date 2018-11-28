#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#define Max 1000005
#define EPS 1e-9

using namespace std;

int m;
int arr[Max], an;
double tarr[Max];
double ans;

double fabs(double t)
{
	if( t>0)
		return t;
	else
		return -t;
}

bool check(double t)
{
	int i;

	tarr[0] = arr[0] - t;

	for(i=1;i<an;i++)
	{
		tarr[i] = max(1.0*tarr[i-1] + m, arr[i]-t);

//		cout<<tarr[i]<<" "<<arr[i]<<"\n";

		if(fabs(tarr[i] - arr[i]) > t)
			return 0;
	}
	return 1;
}

int main()
{
	int z, zi, n, i, t, v;
	double l, r, mid;

	scanf("%d", &z);

	for(zi=1;zi<=z;zi++)
	{
		scanf("%d %d", &n, &m);

		an = 0;
		for(i=0;i<n;i++)
		{
			scanf("%d %d", &t, &v);

			while(v--)
				arr[an++] = t;
		}

		ans = -1;
		l = 0.0; r = 1e12;
		while(fabs(r - l) > EPS)
		{
			mid = (l+r)/2;


//			cout<<mid<<"\n";
			if(check(mid))
				ans = mid, r = mid;
			else
				l = mid;
		}


		printf("Case #%d: %.6lf\n", zi, ans);

	}
}
