#include <map>
#include <queue>
#include <cstdio>
#include <algorithm>
using namespace std;

int up(int b){
	int ret=1;
	while (ret<=b) ret*=10;
	return ret;
}

int B[100000000];
int main(){
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	
	int a, b, v[60], cnt, ans;
	map<pair<int, int>, int> mp;
	int T, u, z, s;
	scanf("%d", &T);
	for (int t=1; t<=T; t++){
		scanf("%d%d", &a, &b);
		u=up(b); z=10, ans=0;
		for (int i=10; i<=u; i++){
			if (B[i]==t) continue;
			cnt=1; v[0]=s=i;
			if (z*10<=i) z=z*10;
			for (s=(s-(s/z)*z)*10+s/z; s!=v[0];){
				B[s]=t; v[cnt++]=s;
				s=(s-(s/z)*z)*10+s/z;
			} sort(v, v+cnt);
			for (int j=0; j<cnt; j++)
			  for (int l=j+1; l<cnt; l++)
			    if (a<=v[l] && v[l]<=b && a<=v[j] && v[j]<=b && mp[make_pair(v[j], v[l])]!=t)
						{ mp[make_pair(v[j], v[l])]=t; ans++;}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
