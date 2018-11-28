#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <math.h>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
using namespace std;


typedef vector <int> vi;
typedef vector <string> vs;
typedef pair <int,int> pii;
typedef vector <double> vd;

int tc, ntc;
struct tt
{
	int a, b, c;
};
bool operator<(const tt& a, const tt& b)
{
	return a.a < b.a;
}

tt ar[5000];
int n;

pii xx[5000];
int nx;

int calc1(int sisa)
{
	int res = 0;
	int i;
	int cur = 0;
	int tmp;

	priority_queue <int> pq;
	for (i=0; i<nx; i++)
	{
		// take xx[i].first
		cur = xx[i].first;
		pq.push( xx[i].second );

		while (!pq.empty())
		{
			int a = pq.top();
			if (a <= sisa-cur) break;
			pq.pop();
		}

		tmp = pq.size();
		if (tmp > res) res = tmp;
	}

	return res;
}

int calc(int na)
{
	int i;
	nx = 0;
	for (i=0; i<n; i++) if (ar[i].a <= na)
		xx[nx++] = make_pair( ar[i].b, ar[i].c );

	sort(xx, xx+nx);
	int res = calc1( 10000 - na );
	return res;
}

int main()
{
	FILE* fi = fopen("A-large.in","r");
	FILE* fo = fopen("A-large.out","w");

	int i;
	int res, tmp;
	fscanf(fi,"%d",&ntc);
	for (tc=1; tc<=ntc; tc++)
	{
		fscanf(fi,"%d",&n);	
		for (i=0; i<n; i++) fscanf(fi,"%d %d %d",&ar[i].a, &ar[i].b, &ar[i].c);

		sort(ar, ar+n);
		res = 0;
		for (i=0; i<n; i++)
		{
			tmp = calc( ar[i].a );
			if (tmp > res) res = tmp;
		}

		printf("Case #%d: %d\n",tc,res);
		fprintf(fo,"Case #%d: %d\n",tc,res);
			
	}

	fclose(fi); fclose(fo);
	return 0;
}