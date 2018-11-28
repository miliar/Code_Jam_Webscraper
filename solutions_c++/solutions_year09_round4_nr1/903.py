#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;
#define rep(i,n) for (int i=0;i<n;i++)

typedef vector<int> vi;

int main()
{
	freopen("sm.in", "r", stdin);
	freopen("sm.txt", "w", stdout);
	int tno;
	scanf("%d",&tno);
	for (int tc=1;tc<=tno;tc++) {
		int n; char s[1024];
		scanf("%d", &n);
		vi t(n);

		rep(i,n) {
			scanf("%s", s);
			t[i]=0;
			rep(j,n)
				if (s[j]=='1') t[i]=j;
		}

		map<vi,int> mm;
		queue<vi> st;
		st.push(t);
		mm[t]=1;
		int sol=-1;
		
		while(!st.empty())
		{
			vi& top = st.front();
			int cnt = mm[top];
			bool fnd=true;
			rep(i,n) {
				if ( top[i]>i ) { fnd=false; break; }
			}
			if (fnd) { sol=cnt; break; }
			int ncnt = cnt+1;
			rep(i,n-1) {
				vi targ = top;
				swap( targ[i], targ[i+1] );
				int& v = mm[targ];
				if (v==0) {
					v=ncnt;
					st.push(targ);
				}
			}
			st.pop();
		}

		printf("Case #%d: %d\n", tc, sol-1);
		fflush(stdout);
	}
	return 0;
}