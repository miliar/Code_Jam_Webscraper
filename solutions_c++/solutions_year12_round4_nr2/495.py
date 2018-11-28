#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <bitset>
#include <iomanip>
#include <utility>
#include <queue>
#include <map>
#include <set>
using namespace std;

const double EPS = 1e-10;
const double PI = acos(-1.0);

typedef long long LL;

typedef set<int>::iterator sii;

const int MAXN = 1000+10;

int n,W,L,r[MAXN];
int x[MAXN],y[MAXN];

struct node {
	int x,y;
};

node lis[MAXN];
int id[MAXN];

inline bool cmp(const node &p,const node &q) {
	return p.x<q.x || (p.x==q.x && p.y<q.y);
}

bool work(int i,int val) {
	if (val>W) return 0;
	x[i] = val;
	int cnt = 0;
	for (int k = 0; k<i; ++k)
		if (x[k]+r[k]<=x[i]-r[i] || x[k]-r[k]>=x[i]+r[i]);
		else {
			lis[cnt].x = y[k]-r[k]-r[i];
			lis[cnt].y = y[k]+r[k]+r[i];
			++cnt;
		}
	sort(lis,lis+cnt,cmp);
	int pre = 0;
	y[i] = -1;
	//cout<<"X = "<<x[i]<<endl;
	for (int k = 0; k<cnt; ++k) {
		//cout<<lis[k].x<<' '<<lis[k].y<<endl;
		if (lis[k].x>=pre) {
			y[i] = pre;
			break;
		}
		if (pre<lis[k].y) pre = lis[k].y;
	}
	if (L>=pre) y[i] = pre;
	if (0<=y[i] && y[i]<=L) return 1;
	return 0;
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int ntest;
	scanf("%d",&ntest);
	for (int loop = 1; loop<=ntest; ++loop) {
		printf("Case #%d:",loop);
		scanf("%d%d%d",&n,&W,&L);
		for (int i = 0; i<n; ++i) {
			scanf("%d",&r[i]);
			id[i] = i;
		}
		set<int> px;
		x[0] = y[0] = 0;
		if (x[0]+r[0]<=W) px.insert(x[0]+r[0]);
		for (int i = 1; i<n; ++i) {
			if (work(i,0));
			else {
				sii j;
				for (j = px.begin(); j!=px.end(); ++j)
					if (work(i,*j+r[i])) break;
			}
			if (x[i]+r[i]<=W) px.insert(x[i]+r[i]);
		}
		for (int i = 0; i<n; ++i) {
			if (0<=x[i] && x[i]<=W) {
				if (0<=y[i] && y[i]<=L);
				else printf("%d\n",i);
			}
			else printf("%d\n",i);
			for (int j = i+1; j<n; ++j) {
				double dis = sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]));
				//if (dis<r[i]+r[j]) printf("%d %d\n",i,j);
			}
		}
		for (int i = 0; i<n; ++i)
			printf(" %d %d",x[i],y[i]);
		printf("\n");
	}
	return 0;
}
