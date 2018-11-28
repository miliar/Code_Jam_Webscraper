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

#define RI( o ) for(typeof(o.begin()) i= (o).begin(); i!=o.end(); ++i)
#define RP3( x, y, z ) RP( x, i ) RP( y, j ) RP( z, k )
#define RP( x, i ) for(int i=0; i<(x); ++i)
#define R( x ) RP((x).size(), i)
#define pB push_back

int dist[110][1010];

int main()
{
	int N;
	cin >> N;
	for(int cn=1; cn<=N; ++cn)
	{
		int S, Q, c=0;
		string nm;
		map<string, int> m;
		char ip[1000];
		vi t;
		
		cin >> S;
		getline(cin, nm);
		RP(S,i)
		{
			getline(cin,nm);
			//nm=ip;
			m[nm]=c++;
		}
		
		//RI(m) cout << i->first << i->second << endl;
		
		cin >> Q;
		getline(cin,nm);
		RP(Q,i)
		{
			getline(cin,nm);
			t.pB(m[nm]);
		}
		
		memset(dist,0,sizeof(dist));
		
		for(int i=Q; i>0; --i) RP(S,j)
		{
			if(t[i-1]==j) dist[j][i-1]=0;
			else dist[j][i-1]=dist[j][i]+1;
		}
		
		int g=-1, cc=-1;
		for(int i=0; i<Q; )
		{
			int k=0;
			if(cc==-1 || cc==t[i])
			{
				for(int j=0; j<S; ++j) if(dist[j][i]>dist[k][i]) k=j;
			}
			cc=k; i+=dist[k][i]; ++g;
		}
		if(g==-1) g=0;
		cout << "Case #" << cn << ": " << g << endl;
	}
	return 0;
}
