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

//vector<vector<bool> > mud, mew;
bool sq[6010][6010];
bool mud[6010][6010];
bool mew[6010][6010];
int SF=3005;

int main()
{
	int N;
	cin >> N;
	for(int cn=1; cn<=N; ++cn)
	{
		int T, L, ss;
		string s;
		
		int x=0, y=0, t;
		int dx=0, dy=1;
		memset(sq,0,sizeof(sq));
		memset(mud,0,sizeof(mud));
		memset(mew,0,sizeof(mew));
		cin >> L;
		
		RP(i,0,L)
		{
			cin >> s >> T;
			ss=s.size();
			
			RP(j,0,T)
			{
				
				for(int k=0; k<ss; ++k)
				{
					//cout << x << " " << y << endl;
					if(s[k]=='F')
					{
						if(dy==1)
							mew[SF+y][SF+x]=1;
						else
						if(dy==-1)
							mew[SF+y-1][SF+x]=1;
						else
						if(dx==1)
							mud[SF+x][SF+y]=1;
						else
						if(dx==-1)
							mud[SF+x-1][SF+y]=1;
						
						x=x+dx; y=y+dy;
					}
					
					if(s[k]=='R')
					{
						t=dx; dx=dy; dy=-t;
					}
					if(s[k]=='L')
					{
						t=dx; dx=-dy; dy=t;
					}
				}
			}
			
		}
		
		int ct, cc;
		ll ans=0;
		RP(i,0,6010)
		{
			ct=0; cc=0;
			RP(j,0,6010) if(mud[i][j]) ++cc;
			
			RP(j,0,6010)
			{
				if(mud[i][j]) {++ct; }
				if(ct>0 && ct%2==0 && ct<cc) sq[i][j]=1;
				
			}
		}
		
		RP(i,0,6010)
		{
			ct=0; cc=0;
			RP(j,0,6010) if(mew[i][j]) ++cc;
			
			RP(j,0,6010)
			{
				if(mew[i][j]){ ++ct; /*cout << (j-3005) << endl;*/}
				if(ct>0 && ct%2==0 && ct<cc) {sq[j][i]=1; }
				
			}
		}
		
		RP(i,0,6010)
		RP(j,0,6010)
		if(sq[i][j]) ++ans;
		
		cout << "Case #" << cn << ": " << ans << endl;
	}
	
	return 0;
}