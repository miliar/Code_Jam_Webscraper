/*
Nguyen Tran Nam Khanh
microsoft
*/
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cmath>
#include <cstdio>

using namespace std;

#define Clear(t) memset((t),0,sizeof(t))
#define For(i,a,b) for (int i=(int)(a),_t = (int)(b);i<=_t;i++)
#define Ford(i,a,b) for (int i=(int)(a), _t = (int)(b);i>=_t;i--)
#define Rep(i,n) for (int i=0, _t = (int)(n);i<_t;i++)
#define tr(it, c) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define SZ(t) ((int)((t).size()))
#define All(v) (v).begin(),(v).end()
#define Sort(v) sort(All(v))
#define pb push_back

typedef vector<int> VI;
typedef long long ll;
typedef vector<ll> VL;
typedef vector<string> VS;

string i2s(int x) { ostringstream o; o<<x; return o.str(); }
int s2i(string s) { int x; istringstream i(s); i>>x; return x; }

int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};

int sl[7000], vt[7000][7000], minx[7000], miny[7000], maxx[7000], maxy[7000];
int n;
bool ok[7000];
string a;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int st;
	cin>>st;
	For(ts,1,st) {
		cin>>n;
		a = "";
		while (n--) {
			string tmp;
			int sl;
			cin>>tmp;
			cin>>sl;
			while (sl--) a+=tmp;
		}
		n = SZ(a);
		For(i,0,6600) {
			maxx[i]=maxy[i]=-10000;
			minx[i]=miny[i]=10000;
		}
		int ix = 10000, ax = -10000, iy = 10000, ay = -10000;
		int h = 3;
		int x = 0;
		int y = 0;
		memset(sl,0,sizeof(sl));
		//memset(vs,0,sizeof(vt));
		Rep(i,n) if (a[i]=='F') {
			int xx = x+dx[h];
			int yy = y+dy[h];
			ix = min(ix,xx);
			ax = max(ax,xx);
			iy = min(iy,yy);
			ay = max(ay,yy);
			if (h==0) {
				vt[xx+3300][sl[xx+3300]++]=yy;
				maxy[xx+3300]=max(maxy[xx+3300], yy);
				miny[xx+3300]=min(miny[xx+3300], yy);
			} else if (h==1) {
				minx[yy+3300]=min(minx[yy+3300], xx);
				maxx[yy+3300]=max(maxx[yy+3300], xx);
			} else if (h==2) {
                vt[x+3300][sl[x+3300]++]=yy;
				maxy[x+3300]=max(maxy[x+3300], yy);
				miny[x+3300]=min(miny[x+3300], yy);
			} else if (h==3) {
				minx[y+3300]=min(minx[y+3300], xx);
				maxx[y+3300]=max(maxx[y+3300], xx);
			}
			x = xx;
			y = yy;
		} else if (a[i]=='L') {
			h = (h+1)%4;
		} else {
			h = (h+3)%4;
		}
		int dt = 0;
		For(i,ix+3300,ax+3300) {
			For(j,miny[i]+3300,maxy[i]+3300) ok[j]=false;
			Rep(j,sl[i]) ok[vt[i][j]+3300]=true;
			bool cong = false;
			int save = 0;
			For(j,miny[i]+3300,maxy[i]+3300) if (ok[j]) {
				if (cong) {
					dt+=j-save;
					cong = false;
				} else {
					cong = true;
					save = j;
				}
			}
		}
		int res = 0;
		//For(i,ix+3300,ax+3300) cout<<miny[i]<<' '<<maxy[i]<<endl;
		For(i,ix+3300,ax+3300) For(j,iy+3300,ay+3300) {
			if ((miny[i]<=j-3300 && maxy[i]>j-3300) || (minx[j]<=i-3300 && maxx[j]>i-3300)) {
				res++;
				//cout<<i-3300<<' '<<j-3300<<endl;
			}
		}
		res-=dt;
		cout<<"Case #"<<ts<<": "<<res<<endl;
	}

	return 0;
}
