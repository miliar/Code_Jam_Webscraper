#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
using namespace std;

int a[1024][2];
int r[1024];
int b[2];
int n,m;
int mxw,mnw,mxm,mnm;
int mndw,mxdw,mndm,mxdm;
vector<pair<int,int> > lu,ru,lb,rb;

int main() {
	int N,cs=0;
	char tmp[23];
	for(scanf("%d",&N);N--;) {
		scanf("%d",&n);
		mnw=mnm=10000000,mxw=mxm=0;
		for(int i=0;i<n;i++) {
			scanf("%d %d",&a[i][0],&a[i][1]);
			gets(tmp);
			if (tmp[1]=='B') {
				r[i]=1;
				mnw=min(mnw,a[i][0]);
				mxw=max(mxw,a[i][0]);
				mnm=min(a[i][1],mnm);
				mxm=max(a[i][1],mxm);
			}
			else r[i]=0;
		}
		mndw=mndm=1000000000,mxdw=mxdm=0;
		lu.clear(),ru.clear(),lb.clear(),rb.clear();
		if (mnw<=mxw);
		for(int i=0;i<n;i++) {
			if (!r[i]) {
				if (a[i][1]>=mnm && a[i][1]<=mxm) {
					if (a[i][0]<mnw) mxdw=max(mxdw,a[i][0]);
					if (a[i][0]>mxw) mndw=min(mndw,a[i][0]);
				}
				if (a[i][0]>=mnw && a[i][0]<=mxw) {
					if (a[i][1]<mnm) mxdm=max(mxdm,a[i][1]);
					if (a[i][1]>mxm) mndm=min(mndm,a[i][1]);
				}
				if (a[i][0]<mnw && a[i][1]<mnm) 
					lu.push_back(make_pair(a[i][0],a[i][1]));
				if (a[i][0]>mxw && a[i][1]<mnm)
					ru.push_back(make_pair(a[i][0],a[i][1]));
				if (a[i][0]<mnw && a[i][1]>mxm)
					lb.push_back(make_pair(a[i][0],a[i][1]));
				if (a[i][0]>mxw && a[i][1]>mxm)
					rb.push_back(make_pair(a[i][0],a[i][1]));
			}
		}
		scanf("%d",&m);
		printf("Case #%d:\n",++cs);
		for(;m--;) {
			scanf("%d %d",&b[0],&b[1]);
			if (mxw<mnw) {
				bool flag=false;
				for(int i=0;i<n;i++)
					if (a[i][0]==b[0] && a[i][1]==b[1]) printf("%d\n",i),flag=true;
				if (flag) puts("NOT BIRD"); else puts("UNKNOWN");
				continue;
			}
			if (b[0]>=mnw && b[0]<=mxw && b[1]>=mnm && b[1]<=mxm) {
				puts("BIRD");
				continue;
			}
			if (b[0]<=mxdw || b[0]>=mndw || b[1]<=mxdm || b[1]>=mndm) {
				puts("NOT BIRD");
				continue;
			}
			bool flag=false;
			for(int i=0;i<lu.size();i++)
				if (lu[i].first>=b[0] && lu[i].second>=b[1]) {
					flag=true;
					puts("NOT BIRD");
					break;
				}
			if (flag) continue;
			for(int i=0;i<ru.size();i++)
				if (ru[i].first<=b[0] && ru[i].second>=b[1]) {
					flag=true;
					puts("NOT BIRD");
					break;
				}
			if (flag) continue;
			for(int i=0;i<lb.size();i++)
				if (lb[i].first>=b[0] && lb[i].second<=b[1]) {
					flag=true;
					puts("NOT BIRD");
					break;
				}
			if (flag) continue;
			for(int i=0;i<rb.size();i++)
				if (rb[i].first<=b[0] && rb[i].second<=b[1]) {
					flag=true;
					puts("NOT BIRD");
					break;
				}
			if (flag) continue;
			puts("UNKNOWN");
		}
	}
	return 0;
}
