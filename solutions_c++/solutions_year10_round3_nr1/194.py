#include <cstdio>
#include <vector>
using namespace std;
int ccw(int x1, int y1, int x2, int y2, int x3, int y3){
	int temp = x1*y2+x2*y3+x3*y1;
	temp = temp - y1*x2-y2*x3-y3*x1;
	if(temp>0)
		return 1;
	else if(temp==0)
		return 0;
	else
		return -1;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int tc=1; tc<=t; tc++){
		int ans = 0;
		int n;
		scanf("%d",&n);
		vector<pair<int, int> > a(n);
		for(int i=0; i<n; i++)
			scanf("%d %d",&a[i].first,&a[i].second);
		for(int i=1; i<n; i++){
			for(int j=0; j<i; j++){
				int t1,t2,t3,t4;
				t1 = ccw(1,a[i].first,2,a[i].second,1,a[j].first);
				t2 = ccw(1,a[i].first,2,a[i].second,2,a[j].second);
				t3 = ccw(1,a[j].first,2,a[j].second,1,a[i].first);
				t4 = ccw(1,a[j].first,2,a[j].second,2,a[i].second);
				int t5 = t1*t2;
				int t6 = t3*t4;
				if(t5==-1 && t6==-1)
					ans++;
			}
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}