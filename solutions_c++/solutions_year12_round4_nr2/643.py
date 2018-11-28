#include<cstdio>
#include<vector>
#include<algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

typedef long long ll;

struct circle{
	int x,y,r,id;
};

bool intersect(const circle &C1,const circle &C2){
	return (ll)(C1.x-C2.x)*(C1.x-C2.x)+(ll)(C1.y-C2.y)*(C1.y-C2.y)<(ll)(C1.r+C2.r)*(C1.r+C2.r);
}

void solve(){
	srand(77);

	int n,W,H; scanf("%d%d%d",&n,&W,&H);
	pair<int,int> r[10];
	rep(i,n) scanf("%d",&r[i].first), r[i].second=i;
	sort(r,r+n);

	vector<circle> ans;
	if(n>0) ans.push_back((circle){0,0,r[n-1].first,r[n-1].second}), n--;
	if(n>0) ans.push_back((circle){W,H,r[n-1].first,r[n-1].second}), n--;
	if(n>0){
		while(1){
			circle C[8];
			rep(i,n){
				C[i].x=rand()%W+1;
				C[i].y=rand()%H+1;
				C[i].r=r[i].first;
				C[i].id=r[i].second;
			}

			rep(j,n) rep(i,j) if(intersect(C[i],C[j])) goto BAD;
			rep(i,n) rep(j,2) if(intersect(C[i],ans[j])) goto BAD;

			rep(i,n) ans.push_back(C[i]);
			break;

			BAD:;
		}
	}

	int x_ans[10],y_ans[10];
	rep(i,ans.size()){
		x_ans[ans[i].id]=ans[i].x;
		y_ans[ans[i].id]=ans[i].y;
	}
	rep(i,ans.size()) printf("%d %d%c",x_ans[i],y_ans[i],i<(int)ans.size()-1?' ':'\n');
}

int main(){
	int T; scanf("%d",&T);
	for(int t=1;t<=T;t++) printf("Case #%d: ",t), solve();
	return 0;
}
