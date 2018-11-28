#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <set>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_n=(b);i<=_n;i++)
#define _m(a,b) memset(a,b,sizeof(a))

vector<string> split( const string& s, const string& delim =" " ) {
    vector<string> res;
    string t;
    for ( int i = 0 ; i != s.size() ; i++ ) {
        if ( delim.find( s[i] ) != string::npos ) {
            if ( !t.empty() ) {
                res.push_back( t );
                t = "";
            }
        } else {
            t += s[i];
        }
    }
    if ( !t.empty() ) {
        res.push_back(t);
    }
    return res;
}

vector<int> splitInt( const string& s, const string& delim =" " ) {
    vector<string> tok = split( s, delim );
    vector<int> res;
    for ( int i = 0 ; i != tok.size(); i++ )
        res.push_back( atoi( tok[i].c_str() ) );
    return res;
}

double sqr(double x)
{
	return x*x;
}

int main()
{
	int t,n;
	int x[500],y[500],z[500],vx[500],vy[500],vz[500];
	scanf("%d",&t);
	REP(__,t)
	{
		scanf("%d",&n);
		REP(i,n) scanf("%d %d %d %d %d %d",x+i,y+i,z+i,vx+i,vy+i,vz+i);
		long long sx,sy,sz,svx,svy,svz;
		sx = sy = sz = svx = svy = svz = 0LL;
		REP(i,n)
		{
			sx += x[i],sy+=y[i],sz+=z[i];
			svx += vx[i] , svy += vy[i], svz += vz[i];
		}
		long long A,B;
		A = sx * svx + sy * svy + sz * svz;
		B = svx*svx + svy * svy + svz * svz;
		//printf("%I64d %I64d %I64d %I64d %I64d %I64d\n",sx,sy,sz,svx,svy,svz);
		//printf("%I64d %I64d\n",A,B);
		double T;
		if (B>0LL) T= -(double) A / B;
		else T = 0;
		if (A > 0) T = 0;
		double dx = sqr((sx + T * svx) / n);
		double dy = sqr((sy + T * svy) / n);
		double dz = sqr((sz + T * svz) / n);
	//	fprintf(stderr,"Case #%d: %d\n",__+1,2);
		printf("Case #%d: %.8lf %.8lf\n",__+1,sqrt(dx+dy+dz),T);
		//fprintf(stderr,"Case #%d: %.8lf %.8lf\n",__+1,sqrt(dx+dy+dz),T);
	}
	return 0;	
}
