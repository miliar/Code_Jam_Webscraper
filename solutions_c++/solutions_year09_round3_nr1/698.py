#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;


int main()
{
	FILE *in;
	in = fopen("input.txt","rt");
	freopen("output.txt", "w+", stdout);
	int T=0;
	int i,p,d;
	char ch;
	VI num(62);
	VI alpha(256, -1);
	for(ch=fgetc(in); ch!='\n'; T=T*10+ch-'0', ch=fgetc(in));
	REP (t, T)
	{
		cout << "Case #"<<(t+1)<< ": ";
		for(i=0, ch=fgetc(in); ch!='\n' && ch!=EOF; num[i]=ch, ch=fgetc(in), i++);
		REP(o, SZ(alpha))
			alpha[o]=-1;
		alpha[num[0]]=1;
		num[0]=1;
		for(p=1; p<SZ(num) && alpha[num[p]]==1; num[p]=1, p++);
		alpha[num[p]]=0;
		num[p]=0;
		int numeric=2;
		FOR(o,p+1,i)
		{
			if (alpha[num[o]]<0) 
			{
				alpha[num[o]]=numeric;
				numeric++;
			}
			num[o]=alpha[num[o]];
		}
		VI res(19,0);
		VI mnoj(19,0);
		VI mnojres(19,0);
		mnoj[18]=1;
		for(int o=i-1; o>=0; o--)
		{
			REP(l,19)
				mnojres[l]=0;
			d=0;
			for(int k=18; k>=0; k--)
			{
				mnojres[k]=(num[o]*mnoj[k]+d)%10;
				d=(num[o]*mnoj[k]+d)/10;
			}
			d=0;
			for(int k=18; k>=0; k--)
			{
				p=(res[k]+mnojres[k]+d)/10;
				res[k]=(res[k]+mnojres[k]+d)%10;
				d=p;
			}
			d=0;
			for(int k=18; k>=0; k--)
			{
				p=(numeric*mnoj[k]+d)/10;
				mnoj[k]=(numeric*mnoj[k]+d)%10;
				d=p;
			}
		}
		p=0;
		while(res[p]==0) p++;
		FOR(k,p,19) cout << res[k];
		cout << endl;
	}

	return 0;
}
