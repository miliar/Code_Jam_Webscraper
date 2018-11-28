#include <set>
#include <map>
#include <iomanip>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define rep(i, cnt)			for(int i=0;i<(cnt);++i)
#define repi(i, j, cnt)			for(int i=(j);i<(cnt);++i)
#define P(x)				cout<<#x<<" = { "<<x<<" }\n"

const int MAX = 600;

int match[MAX], back[MAX], queue[MAX], prev[MAX];
bool select[MAX][MAX];
	
int fastBipartite(int nright, int nleft)
{   //Build select during reading: select[i][j]=1 if possible else 0
        
	int i, j, x, qs, qe, /* Queue Start & End */ tot_matching=0;

	memset(match,  -1, sizeof(int ) * nright );
	memset(back ,  -1, sizeof(int ) * nleft  );

	rep(i, nright)
	{
		qs = qe = 0; 	rep(j, nleft) prev[j] = -2;
		rep(j, nleft)
			if( select[i][j] )	prev[j] = -1, queue[qe++] = j;

		while( qs < qe )
		{
			x = queue[qs]; 	if( back[x] == -1 )	break;	qs++;
			rep(j, nleft) if( prev[j] == -2 && select[ back[x] ][j] )
				prev[j] = x, queue[qe++] = j;
		}

		if( qs == qe )		continue;
		while( prev[x] > -1 ) {
			match[ back[ prev[x] ] ] = x, back[x] = back[prev[x]];
			x = prev[x];    }
		back[x] = i, match[i] = x, tot_matching++;
	}
	
	return tot_matching;	/* tot_matching <= nright */
}

pair<int, int> toMinutes(string str, int T)
{
	istringstream iss(str);
	int a, b, c, d;
	char ch;
	iss>>a>>ch>>b>>c>>ch>>d;
	
	return make_pair(  a*60+b, c*60+d+T  );
}

vector< pair<int, int> > va;
vector< pair<int, int> > vb;
	
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int cases, t, na, nb;
	string line;
	
	cin>>cases;
	
	for (int k = 1; k <= cases; ++k) {
		cin>>t>>na>>nb;
		va.clear();
		vb.clear();
		
		cin>>ws;
		rep(i, na) {
			getline(cin, line);
			va.push_back( toMinutes(line, t) );
		}
		
		rep(i, nb) {
			getline(cin, line);
			vb.push_back( toMinutes(line, t) );
		}
		
		int n = na+nb;
		clr(select, 0);
		
		rep(i, na)
			rep(j, nb)
			{
				if( va[i].second <= vb[j].first)
					select[i][ j+na ] = 1;
				
				if( vb[j].second <= va[i].first)
					select[ j+na ][i] = 1;
			}
		
		int tots = fastBipartite(n, n);
		
		int aCnt = 0, bCnt = 0;
		rep(i, na)		if( back[i] == -1)	aCnt++;
		repi(i, na, n)	if( back[i] == -1)	bCnt++;
		
		cout<<"Case #"<<k<<": "<<aCnt<<" "<<bCnt<<"\n";
	}
	
	return 0;
}
