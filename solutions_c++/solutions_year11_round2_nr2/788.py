#include <fstream>
using namespace std;

ifstream input("input.txt");
ofstream output("output.txt");

typedef __int64 i64;
int c, d;
int p[200], v[200];

double min(double a, double b) { return (a<b)?a:b; }
double max(double a, double b) { return (a>b)?a:b; }

bool can(int i, double t, bool left)
{
	i64 li = ((i64)d)*(v[i]-1);
	if (0.5 * li > t) return false;
	double pl, pr;
	if (left) { pl = p[i]-t; pr=p[i]-t+li; }
	else { pr = p[i] + t; pl = p[i] + t - li; }
	double ml = pl - d, mr = pr + d;
	for (int j = i-1; j>=0; --j)
	{
		i64 ll = ((i64)d)*(v[j]-1);
		double l, r;
		r = min(p[j] + t, ml);
		l = r - ll;
		if (t < fabs(p[j]-l)) return false;
		ml = l - d;
	}
	for (int j = i+1; j<c; ++j)
	{
		i64 ll = ((i64)d)*(v[j] - 1);
		double l, r;
		l = max(p[j]-t, mr);
		r = l + ll;
		if (t < fabs(r-p[j])) return false;
		mr = r + d;
	}
	return true;
}

double run(double t1, double t2)
{
	double m = 0.5*(t1+t2);
	if (fabs(t1-t2)<1e-6) return m;
	bool ok = false;
	for (int i=0;i<c;++i)
		if (can(i,m,true) || can(i,m,false))
		{
			ok = true;
			break;
		}
		else if (can(i,t1,true) || can(i,t1,false)) return t1;
	if (ok) return run(t1, m);
	return run(m, t2);
}

int main()
{
	int t;
	input >> t;
	output.precision(6);
	for (int i=0;i<t;++i)
	{
		input >> c >> d;
		for (int j=0;j<c;++j)
			input >> p[j] >> v[j];
		double ans = run(0, d*1e7);
		if (ans<1e-6) ans = 0;
		output << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}