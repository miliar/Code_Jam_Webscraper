#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <cmath>
using namespace std;

#define forV(va,ve) for(int va=0;va < ve.size();++va)
#define V(t) vector< t >
#define Vall(t) t.begin(),t.end()
#define MP make_pair
vector<string> es;
vector<string> q;

int memo[1000][1000];

int dp(int at,int se)
{
	if(at == q.size()){return 0;}
	int &ret = memo[at][se];
	if(ret != -1){return ret;}
	if(q[at] == es[se]){return 100000;}
	ret = 1000000;
	for(int i=0;i<es.size();++i)
	{
		ret <?= dp(at+1,i) + ((i == se)?(0):(1));
	}
	return ret;
}

set<pair<pair<int,int>,int> > events;
vector<pair<pair<int,int>,int> > v;
pair<int,int> proc(string x,int inc=0)
{
	pair<int,int> p;
	sscanf(x.c_str(),"%d:%d",&p.first,&p.second);
	p.second += inc;
	while(p.second >= 60){p.second -= 60;++p.first;}
	return p;
}

double sq(double x)
{return x*x;}

int main(void)
{
	int N;
	cin >> N;
	const int TODO = 50000000;
	const double PI = acos(-1);
	for(int cn=1;cn <= N;++cn)
	{
		double f,R,t,r,g;
		cin >> f >> R >> t >> r >> g;
		if(2*f >= g)
		{
			cout << "Case #" << cn << ": 1.0" << endl;
			continue;
		}
		t += f;
		r += f;
		g -= 2*f;
		double holes = 0.0;
		const double iter = 2*r + g;
		//cerr << "iter: " << iter << endl;
		double x,y;
		const double sqRt = (R-t)*(R-t);
		for( x=r;x <= R-t;x+=iter)
		{
			for(y=r; sq(x+iter) + sq(y+iter) <= sq(R-t);y+=iter)
			{
				//complete square
			//	holes += g*g;
			}
			for(y=r;sq(x) + sq(y) <= sqRt;y+=iter)
			{
				//partially out, x completely in
				//integrate from cx = x to x+g
				//x2 + y2 = arr2
				//x = sqrt(arr2 - y2)
				//y = sqrt(arr2 - x2)
				double sum = 0.;
				const int INTERVAL = 10000;
				const double ma = min(x+g,R-t);
				for(int c=1;c<INTERVAL;c+=2)
				{
					const double ex = x + (ma-x)*c/(INTERVAL);
					const double sqex = ex*ex;
					sum += 4*max(0.,min(g,sqrt(max(0.,sqRt - sqex)) - y));
				}
				for(int c=2;c<INTERVAL;c+=2)
				{
					const double ex = x + (ma-x)*c/(INTERVAL);
					const double sqex = ex*ex;
					sum += 2*max(0.,min(g,sqrt(max(0.,sqRt - sqex)) - y));
				}
				sum += max(0.,min(g,sqrt(sqRt - x*x) - y));
				sum += max(0.,min(g,sqrt(max(0.,sqRt - (ma)*(ma))) - y));
				holes += sum*(ma-x)*1/(3*INTERVAL);

			}
		}
		//both (partially) out
	/*	x = r + iter*floor((R-t-r)/iter);
				double sum = 0.;
				const int INTERVAL = 10000;
				for(int c=1;c<INTERVAL;c+=2)
				{
					const double ex = x + (R-t-x)*c/(INTERVAL);
					const double sqex = ex*ex;
					sum += 4*max(0.,min(g - g*c/INTERVAL,sqrt(sqRt - sqex) - ex));
				}
				for(int c=2;c<INTERVAL;c+=2)
				{
					const double ex = x + (R-t-x)*c/(INTERVAL);
					const double sqex = ex*ex;
					sum += 2*max(0.,min(g - g*c/INTERVAL,sqrt(sqRt - sqex) - ex));
				}
				sum += max(0.,min(g,sqrt(sqRt - x*x) - x));
				sum += max(0.,min(0.,sqrt(sqRt - (R-t)*(R-t)) - R + t));
				holes += 2*sum*(R-t-x)*1/(3*INTERVAL);
			//	cerr << holes << endl;
		
*/

		double area = PI*R*R*0.25;
		double output = (area - holes)/area;
		printf("Case #%d: %.12lf\n",cn,output);
	}
	return 0;
}
