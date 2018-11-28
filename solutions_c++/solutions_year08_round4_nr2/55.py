#include<stdio.h>
#include<ext/hash_map>
#include<algorithm>
using namespace std;
using namespace __gnu_cxx;

hash_map<int,pair<int,int> > mm;
int n,m,a;

void run(int T) {
	bool flag=false;
	mm.clear();
	scanf("%d %d %d",&n,&m,&a);
	for(int i=n;!flag && i>=0;i--)
		for(int j=m;!flag && j>=0;j--) {
			int s=i*j;
			hash_map<int,pair<int,int> >::iterator it=mm.find(s+a);
			if (it!=mm.end()) {
				printf("Case #%d: 0 0 %d %d %d %d\n",T,i,it->second.second,it->second.first,j);
				flag=true;
			}
			if (s>=a && mm.find(s)==mm.end()) mm.insert(make_pair(s,make_pair(i,j)));
		}
	if (!flag) printf("Case #%d: IMPOSSIBLE\n",T);
}

int main() {
	int N,cs=0;
	for(scanf("%d",&N);N--;)
		run(++cs);
	return 0;
}
