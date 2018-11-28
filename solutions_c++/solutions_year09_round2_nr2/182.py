#define DBG
// Grzegorz Guspiel
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#ifdef DBG
#define R(x) cout<<x<<endl
#else
#define R(x)
#endif
#define REP(i,n) for(int (i)=0; (i)<(n); (i)++)
#define FOR(i,b,e) for(int (i)=(b); (i)<=(e); (i)++)

const int maxn=30;
char buf[30];
vector<int> v;

void get_data() {
	v.clear();
	scanf("%s\n", buf);
	int i=0;
	while(buf[i]) {
		v.push_back(buf[i]-'0');
		i++;
	}
}

void prres() {
	REP(i,v.size()) printf("%c", '0'+v[i]);
	printf("\n");
}

int main() {
	int z; scanf("%d\n", &z);
	REP(zz,z) {
		get_data();
		printf("Case #%d: ", zz+1);
		int inv=-1;
		FOR(i,1,v.size()-1) if(v[i]>v[i-1]) inv=i-1;
		if(inv==-1) {
			v.push_back(0);
			int best=10;
			int besti;
			REP(i,v.size()) if(v[i]>0&&v[i]<best) {
				best=min(best,v[i]);
				besti=i;
			}
			swap(v[0],v[besti]);
			sort(v.begin()+1,v.end());
			prres();
			continue;	
			
		}
		int best=10;
		int besti;
		FOR(i,inv+1,v.size()-1) if(v[i]>v[inv]&&v[i]<best){
			best=v[i];
			besti=i;
		}
		swap(v[inv],v[besti]);
		sort(v.begin()+inv+1,v.end());
		prres();
	}
}
