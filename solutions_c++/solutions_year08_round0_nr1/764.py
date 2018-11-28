#include <cstdio>
#include <iostream>
#include <string>
#include <map>

using namespace std;

int m,n;
map<string,int> my;
char val[128];

int main() {
	int nCase;
	freopen("1.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&nCase);
	for(int nc=1;nc<=nCase;nc++) {
		int i,j;
		char name[1000];
		scanf("%d",&n);
		getchar();
		for(i=0;i<n;i++) {
			gets(name);
			my[name]=i+1;
		}
		scanf("%d",&m);
		getchar();
		int ans=0;
		int num=0;
		memset(val,0,sizeof(val));
		for(i=0;i<m;i++) {
			gets(name);
			int id=my[name];
			if(val[id]==1) continue;
			else {
				num++;
				if(num==n) {
					memset(val,0,sizeof(val));
					num=1;
					ans++;
				}
				val[id]=1;
			}
		}
		printf("Case #%d: %d\n",nc,ans);
	}
	return 0;
}