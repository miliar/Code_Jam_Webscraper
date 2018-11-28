#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define forn(X,Y) for (int X = 0;X < Y;X++)
#define debug(x) cout << '>' << #x << ':' << x << '\n';

#define rep(X,Y,Z) for (int X = Y;X < Z;X++)
#define reset(Z,Y) memset(Z,Y,sizeof(Z))

#define sz(Z) ((int)Z.size())
#define all(W) W.begin(), W.end()
#define pb push_back

#define mp make_pair
#define A first
#define B second

#define inf 1023123123
#define eps 1e-11

#define MX(Z,Y) Z = max((Z),(Y))
#define MN(X,Y) X = min((X),(Y))

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vint;

int diamond[757][757];


int main() {
	
	
	
	int nc;
	scanf("%d",&nc);
	forn(z,nc) {
		printf("Case #%d: ",z+1);
		reset(diamond,-1);
		int best = inf;
		int n;
		cin >> n;
		int midx = 375;
		int inity = 250;
		vint x,y,color;
		
		forn(i,n) {
			int leftpos = midx-i;
			forn(j,i+1) {
				int b;
				cin >> b;
				int dy = i+inity;
				int dx = leftpos + 2*j;
				x.pb(dx);
				y.pb(dy);
			//	debug(dx);
			//	debug(dy);
				diamond[dx][dy] = b;
				color.pb(b);
				}
			}
		inity += n;
		for (int i = n-2;i >= 0;i--) {
			int leftpos = midx-i;
			forn(j,i+1) {
				int b;
				cin >> b;
				int dy = (n-2-i)+inity;
				int dx = leftpos + 2*j;
				x.pb(dx);
				y.pb(dy);
			//	debug(dx);
			//	debug(dy);
			//	debug(leftpos);
			//	debug(inity);
				diamond[dx][dy] = b;
				color.pb(b);
				}
			}
		int minx = *min_element(all(x));
		int maxx = *max_element(all(x));
		int miny = *min_element(all(y));
		int maxy = *max_element(all(y));
		//debug(maxy);
		int count = sz(x);
		int jarak = maxx - 375;
	//	debug(jarak);
		//debug(minx);debug(maxx);debug(miny);debug(maxy);
		rep(ox,175,375+175) rep(oy,175,375+175) {
			//coba jadiin di tengah
			
			//debug((maxy-miny)/2);
			//if (abs(ox-375) + abs(oy - (miny+(maxy-miny)/2)) > jarak) continue;
			//debug(ox);
//(oy);
			int bisa = 1;
			vint mx,my;
			forn(j,count){
				int nx = x[j],ny = y[j];
				int cx,cy;
				int dia = diamond[nx][ny];
				//debug(dia);
				if (nx < ox) {
					cx=(ox + (ox-nx));
					}
				if (nx >= ox) {
					cx=(ox - (nx-ox));
					}
				if (ny < oy) {
					cy=(oy + (oy-ny));
					}
				if (ny >= oy) {
					cy=(oy - (ny-oy));
					}
				//if (oy == 252) {debug(ny);
				//debug(cy);}
				if (diamond[cx][ny] == -1) {
					//baru++;
					mx.pb(cx);
					my.pb(ny);
					diamond[cx][ny] = dia;
					}
				if (diamond[nx][cy] == -1) {
					//baru++;
					mx.pb(nx);
					my.pb(cy);
					diamond[nx][cy] = dia;
					}
				if (diamond[cx][ny] != dia) {
					bisa = 0;
					break;
					}
				if (diamond[nx][cy] != dia) {
					bisa = 0;
					break;
					}
				}
			//dibalikin
			forn(i,sz(mx)) diamond[mx[i]][my[i]] = -1;
			//if (bisa) MN(best,baru);
			/*if (bisa) {
				debug(ox);
				debug(oy);
				}*/
			
			if (bisa) {
			//	..debug(ox);
				//debug(oy);
				//debug("irvan\n");
				//coba cek sizenya
				int jarakmax = 0;
				forn(i,count) {
					//debug(x[i]);
					//debug(y[i]);
					MX(jarakmax,abs(x[i]-ox) + abs (y[i]-oy));
					}
				
				int tes = x[0]+y[0];
				int cur = ox+oy;
				/*debug(tes);
				debug(jarakmax);
				debug(ox);
				debug(oy);
				debug(miny);
				debug(maxy);*/
				if (tes%2 == cur%2) {
					//senasib
					jarakmax++;
					MN(best,jarakmax*jarakmax-sz(x));
					}
				else {
					jarakmax++;
					MN(best,jarakmax*jarakmax-sz(x));
					}
				}
				
				
			}
		printf("%d\n",best);
		}

		
	
	return 0;
	}


//Powered by [KawigiEdit] 2.0!









