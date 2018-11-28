#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
#define fi first
#define se second
#define mp make_pair
pair<pair<int,int>,int> b[5000];
pair<int,pair<int,int> > a[5000];
FILE *in,*out;
int main()
{
	int X,i,n,nr,lastpoz,taux,T,t2,s,r;
	double timp,t,dist,timp_necesar;
	in=fopen("a.in","r");
	out=fopen("a.out","w");
	fscanf(in,"%d",&T);
	for(t2=1;t2<=T;t2++)
	{
		fscanf(in,"%d%d%d%d%d",&X,&s,&r,&taux,&n);
		t=taux;
		r-=s;
		for (i=1;i<=n;i++)
		{
		//	fscanf(in,"%d%d%d",&a[i].se.fi,&a[i].se.se,&a[i].fi);
			fscanf(in,"%d%d%d",&b[i].fi.fi,&b[i].fi.se,&b[i].se);
			b[i].se += s;
			a[i].fi=b[i].se;
			a[i].se=b[i].fi;
		//	a[i].se += s;

		}
		sort(b+1,b+n+1);
		nr = n;
		lastpoz = 0;
		timp = 0;
		for (i=1;i<=n;i++)
		{
			if (b[i].fi.fi == lastpoz) 
			{
				lastpoz  = b[i].fi.se;
				continue;
			}
			nr++;
			a[nr].fi = s;
			a[nr].se = mp(lastpoz, b[i].fi.fi);
			lastpoz = b[i].fi.se;
		}

		if (X!=lastpoz)
		{
			nr++;
			a[nr].fi = s;
			a[nr].se = mp(lastpoz, X);
		}
		sort(a+1,a+nr+1);
		timp = 0; 
		for (i=1;i<=nr;i++)
		{
			timp_necesar = ((double) (a[i].se.se-a[i].se.fi)) / (a[i].fi + r);
			if (timp_necesar <= t)
			{
				t-=timp_necesar;
				timp += timp_necesar;
				continue;
			}
			dist = (a[i].se.se-a[i].se.fi);
			
			timp += t;
			
			dist -= t* (a[i].fi + r);
			t = 0;
			timp += dist/ (a[i].fi);
			
		}
		fprintf(out,"Case #%d: %.8lf\n",t2,timp);

	}
	fclose(in);
	fclose(out);
	return 0;
}
