#include <cstdio>
#include <algorithm>

using namespace std;

struct In{
	int time;
	int flag;
	bool operator < (const In t) {
		if(time!=t.time) return time<t.time;
		return flag<t.flag;
	}
};
In p1[1000];
In p2[1000];

int main(){
	int nCase;
	freopen("1.in","r",stdin);
	freopen("B-lar.out","w",stdout);
	scanf("%d",&nCase);
	int t;
	int i,j;
	for(int nc=1;nc<=nCase;nc++) {
		int m,n;
		scanf("%d",&t);
		scanf("%d %d",&m,&n);
		int h1,m1,h2,m2;
		int n1,n2;
		n1=0;
		n2=0;
		for(i=0;i<m;i++) {
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			p1[n1].flag=1;
			p1[n1++].time=h1*60+m1;
			p2[n2].flag=0;
			p2[n2++].time=h2*60+m2+t;
		}
		for(i=0;i<n;i++) {
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			p1[n1].flag=0;
			p1[n1++].time=h2*60+m2+t;
			p2[n2].flag=1;
			p2[n2++].time=h1*60+m1;
		}
		sort(p1,p1+n1);
		sort(p2,p2+n2);
		int ans1=m;
		int ans2=n;
		for(i=n1-1;i>=0;i--) {
			if(p1[i].flag!=1) continue;
			for(j=i-1;j>=0;j--) {
				if(p1[j].flag==0) {
					p1[j].flag=-11;
					ans1--;
					break;
				}
			}
		}
		for(i=n2-1;i>=0;i--) {
			if(p2[i].flag!=1) continue;
			for(j=i-1;j>=0;j--) {
				if(p2[j].flag==0) {
					p2[j].flag=-11;
					ans2--;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n",nc,ans1,ans2);
	}
	return 0;
}