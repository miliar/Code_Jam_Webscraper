#include<vector>
#include<cstdio>
using namespace std;
int tc,n,l,h,temp;

int main(){
	scanf("%d",&tc);
	for (int ti = 1; ti <= tc; ti++) {
		scanf("%d %d %d\n",&n, &l, &h);
		vector<int> v;		
		for (int i = 1; i <= n; i++) {
			scanf("%d",&temp);
			v.push_back(temp);
		}
		int ans = -1;
		for (int i = l; i <= h; i++) {
			bool tr = true;
			for (int j = 0; j < v.size(); j++) {
				if (((i%v[j]) != 0) && ((v[j]%i) != 0)) tr = false;
			}
			if (tr) {ans = i; break;}
		}
		printf("Case #%d:",ti);
		if (ans!=-1) printf(" %d\n",ans);
		else printf(" NO\n");
	}
}