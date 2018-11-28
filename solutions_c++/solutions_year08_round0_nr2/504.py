#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

vector<pair<int,int> > da(0),db(0);

int main() {
	freopen("B-small.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;++i) {
		da.clear();
		db.clear();
		vector<int> tm_a(1700,0);
		vector<int> tm_b(1700,0);
		int na,nb,t;
		scanf("%d%d%d",&t,&na,&nb);
		for(int j=0;j<na;++j) {
			int h,m;
			scanf("%d:%d",&h,&m);
			int n1=h*60+m;
			scanf("%d:%d",&h,&m);
			da.push_back(make_pair(n1,h*60+m));
		}
		
		for(int j=0;j<nb;++j) {
			int h,m;
			scanf("%d:%d",&h,&m);
			int n1=h*60+m;
			scanf("%d:%d",&h,&m);
			db.push_back(make_pair(n1,h*60+m));
			//printf("%d %d %d %d$\n",n1,h,m,h*60+m);
		}
		
		sort(da.begin(),da.end());
		sort(db.begin(),db.end());
		int ta=0,tb=0;
		int cnt_a=0,cnt_b=0;
		for(int j=0;j<=1440;++j) {
			//if (i==0)
			//printf("%d %d %d\n",j,tm_a[j],tm_b[j]);
			if (ta<da.size()) {
				while (da[ta].first==j) {
					if (tm_a[j]>0) {
						tm_a[j]--;
						tm_b[da[ta].second+t]++;
					} else {
						cnt_a++;
						tm_b[da[ta].second+t]++;
					}
					ta++;
					if (ta>=da.size()) break;
				}
			}
			
			if (tb<db.size()) {
				while (db[tb].first==j) {
					if (tm_b[j]>0) {
						tm_b[j]--;
						tm_a[db[tb].second+t]++;
					} else {
						cnt_b++;
						tm_a[db[tb].second+t]++;
					}
					//printf("!%d %d %d %d!",tb,db[tb].second+t,db[tb].second,t);
					tb++;
					if (tb>=db.size()) break;
				}
			}
			
			tm_a[j+1]+=tm_a[j];
			tm_b[j+1]+=tm_b[j];
		}
		printf("Case #%d: %d %d\n",(i+1),cnt_a,cnt_b);
	}
	return 0;
}
