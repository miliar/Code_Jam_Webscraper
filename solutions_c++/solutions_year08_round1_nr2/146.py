#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <complex>
#include <valarray>
#include <deque>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

#define RI( i, o ) for(typeof(o.begin()) i= (o).begin(); i!=(o).end(); ++i)
#define RP3( x, y, z ) RP( i, 0, x ) RP( j, 0, y ) RP( k, 0, z )
#define RP( i, s, e ) for(typeof(s) i=(s); i<(e); ++i)
#define R( i, x ) RP(i,0,(x).size())
#define pB push_back


int l[2010][2010];
int xu[2010]; int yu[2010];
int nu[2010]; int mu[2010];int mc[2010];

int main()
{
	int N;
	cin >> N;
	for(int cn=1; cn<=N; ++cn)
	{
		ll n,m,t,c, g, h;
		
		cin >> n >> m;
		
		RP(i,0,2010) xu[i]=yu[i]=nu[i]=mu[i]=mc[i]=0;
		
		memset(l,-1,sizeof(l));
		
		RP(i,0,m)
		{
			cin >> t;
			RP(j,0,t)
			{
				cin >> g >> h;
				--g;
				l[i][g]=h;
				if(h==0) nu[i]++; else {mu[i]++;mc[i]=g;}
			}
		}
		
		
		
		int ct=0, fl=0, s, cl=0;
		for(ct=0; ct<=n+1; ++ct)
		{
			RP(i,0,m)
			{
				if(xu[i]==0 && nu[i]==0 && mu[i]==1)
				{
					s=mc[i];
					yu[s]=1;
					RP(j,0,m)
					if(xu[j]==0)
					{
						if(l[j][s]==1)
						{
							xu[j]=1;
							mu[j]--;
							++cl;
						}
						else
						if(l[j][s]==0)
						{
							nu[j]--;
							
							if(nu[j]==0 && mu[j]==0) {fl=1; break;}
							//cout << j << " " << nu[j] << " " << mu[j] << endl;
						}
					}
				}
			}
			if(fl==1) break;
		}
		if(fl==1)
		cout << "Case #" << cn << ": " << "IMPOSSIBLE" << endl;
		else{
			cout << "Case #" << cn << ":";
			RP(i,0,n) cout << " " << yu[i];
			cout << endl;}
	}
	return 0;
}
