#include<cstdio>
#include<utility>
#include<algorithm>
using namespace std;


double tleft;

double walk(double dist, double ws, double rs)
{
	if (tleft <= 0.0)
		return dist/ws;

	double run = dist/rs;
	if (run <= tleft)
	{
		tleft -= run;
		return run;
	}

	double wr = tleft;
	dist -= tleft*rs;
	tleft = 0.0;
	return dist/ws + wr;
}

pair<int,int> input[1001];

int main()
{
	int tests;
	double wynik;
	int x,s,r,t,n,b,e,w;
	double as;
	scanf("%d",&tests);
	for (int tt=1; tt<=tests; tt++)
	{
		scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
		tleft = double(t);
		wynik = 0.0;
		for (int i=0; i<n; i++)
		{
			scanf("%d %d %d",&b,&e,&w);
			int dist = e-b;
			input[i] = make_pair(w,dist);
			x -= dist;
		}
		wynik += walk(x,s,r);
		sort(input,input+n);
		for (int i=0; i<n; i++)
			wynik += walk(input[i].second,input[i].first+s,input[i].first+r);
		printf("Case #%d: %.9lf\n",tt,wynik);
	}

}
