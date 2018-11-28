#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <ctime>
#include <memory.h>

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,Be,En) for(int (i)=(Be);(i)<=(En);++(i))
#define DFOR(i,Be,En) for(int (i)=(Be);(i)>=(En);--(i))
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a,0,sizeof(a))

#define LL  long long
#define VI  vector<int>
#define PAR pair<int ,int> 

using namespace std;
void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}


int T;
int n, k, r;
PAR next[1024];
LL m[1024];
bool flag[1024];
int p[1024];
LL s[1024];
void init()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
}
LL sol2(int v, int r, int len){
	//WR("v=%d r=%d len=%d\n",v,r,len);
	ass(len<=r);
	s[0] = 0;
	int cur = v;
	FOR(i,1,len){
		s[i] = s[i-1] + next[cur].SE;
		cur = next[cur].FI;
	}
	ass(v==cur);
	return s[len]*(r/len) + s[r%len];
}
void sol(){	
	cin >> T;
	int h;
	FOR(t,1,T){
		cin >> r >> k >> n;
		LL sum = 0;
		FOR(i,0,n-1) {
			cin >> m[i];
			sum+=m[i];
		}
		if (sum<k) {
			WR("Case #%d: %I64d\n",t,sum*r);
			cerr << "1";
		} else {
			r++;
			CLR(next);
			FOR(i,0,n-1) {
				int ne = i;
				int su = 0;
				while (su+m[ne]<=k) {
					su+=m[ne];
					ne = (ne+1)%n;
				}
				next[i] = make_pair(ne,su);
				//WR("%d->%d %d\n",i,next[i].FI,next[i].SE);
			}
			CLR(flag);
			int cur = 0;
			LL ans = -666;
			s[0] = s[1] = 0;
			FOR(it,1,r-1){
				flag[cur] = true;
				p[cur] = it;
				int temp = next[cur].FI;
				if (!flag[temp]) {
					s[it+1] = s[it] + next[cur].SE;
					cur = temp;
				} else {
					/*int cl = it - p[temp] + 1;
					LL cc = s[it] - s[p[temp]] + next[cur].SE;
					int co = (r - p[temp] + 1)/cl;
					int re = (r - p[temp] + 1)%cl;
					ans = cc*co + s[p[temp]-1+re];*/
					ans = s[p[temp]];
					ans+=sol2(temp, r - p[temp], it - p[temp] + 1);
					break;
				}
			}
			if (ans==-666) {
				ans = s[r];
				cerr << "2";
			}
			WR("Case #%d: %I64d\n",t,ans);
		}
	}
}
int main()
{
	init();
	sol();
	return 0;
}