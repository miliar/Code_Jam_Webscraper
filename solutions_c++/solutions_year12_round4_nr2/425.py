#include <cstdio>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <iostream>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <bitset>
#include <algorithm>
#include <sstream>
using namespace std;

const double pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679;
const int mod = 1000000007;
const int maxn = 1010;

int T;
int n;
double w, l;
double r[maxn];
double x[maxn], y[maxn];

void init()
{
	memset(r, 0, sizeof(r));
	memset(x, 0, sizeof(x));
	memset(y, 0, sizeof(y));
	scanf("%d%lf%lf", &n, &w, &l);
	for (int i=0; i<n; i++) scanf("%lf", &r[i]);
	sort(r, r+n);
	for (int i=0; i<n/2; i++)
	{
		double t = r[i];
		r[i] = r[n-i-1];
		r[n-i-1] = t;
	}
}

double al[maxn+maxn];
double ar[maxn+maxn];
double ah[maxn+maxn];
int size;
void insert(int l, int r, int h)
{
	if (size==0)
	{
		al[0] = l;
		ar[0] = r;
		ah[0] = h;
		size++;
	}
	else
	{
		al[size] = l;
		ar[size] = r;
		ah[size] = h;
		size++;
		int cur = size - 1;
		while (cur>0 && al[cur] <=al[cur-1])
		{
			double t = al[cur]; al[cur] = al[cur-1]; al[cur-1] = t;
			t = ar[cur]; ar[cur] = ar[cur-1]; ar[cur-1] = t;
			t = ah[cur]; ah[cur] = ah[cur-1]; ah[cur-1] = t;
			cur--;
		}
		for (int i=0; i<size; i++)
			if (al[i]>=l && ar[i] <=r)
			{
				al[i] = l;
				ar[i] = l;
				ah[i] = h;
			}
			else if (al[i]>=l && al[i]<r && ar[i]>r) al[i] = r;
		for (int i=0; i<size; i++)
			if (al[i]<l && ar[i]<=r && ar[i]>=l) ar[i] = l;
		int index = -1;
		for (int i=0; i<size; i++)
			if (al[i]<l && ar[i]>r) index = i;
		if (index != -1)
		{
			double t = ar[index];
			ar[index] = l;
			insert(r, t, ah[index]);
		}
	}
}

void work()
{
	size = 0;
	memset(al, 0, sizeof(al));
	memset(ar, 0, sizeof(ar));
	memset(ah, 0, sizeof(ah));
	insert(0-2*r[0], w+2*r[0], -2*r[0]);

	for (int i=0; i<n; i++)
	{
		for (int j=0; j<size; j++)
			if (ah[j]+r[i]<=l && ar[j]-al[j]>=2*r[i] && ar[j]>=0 && al[j]<=w)
			{
				x[i] = max(0.0, al[j]+r[i]);
				y[i] = max(0.0, ah[j]+r[i]);
				insert(x[i]-r[i],x[i]+r[i], y[i]+r[i]);
				break;
			}
	}
}

void check()
{
	for (int i=0; i<n; i++)
	{
		for (int j=i+1; j<n; j++)
			if ((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])<(r[i]+r[j])*(r[i]+r[j]))
				cout << "ERROR" << endl;
		if (x[i]<0 || x[i]>w || y[i]<0 || y[i]>l)
			cout << "ERROR" << endl;
	}
}

int main(){
	freopen("C:/Users/yaoyao/Downloads/B-small-attempt0.in", "r", stdin);
	freopen("D:/workspace/Topcoder/Algorithm/Algorithm/out.txt", "w", stdout);
	scanf("%d", &T);
	for (int i=1; i<=T; i++)
	{
		init();
		work();
		check();
		printf("Case #%d:",i);
		for (int i=0; i<n; i++)
			printf(" %0.0lf %0.0lf", x[i], y[i]);
		printf("\n");
	}
	return 0;
}

