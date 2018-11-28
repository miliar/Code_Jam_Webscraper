#include <stdio.h>
#include <string.h>

#include <queue>

using namespace std;

#define MAX 4000000

int s[MAX];

bool used[MAX];
queue<int> q;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int n;
		scanf("%d",&n);
		memset(s,0,sizeof(s));
		memset(used,0,sizeof(used));
		for(int i=0;i<n;++i) {
			int x,c;
			scanf("%d%d",&x,&c);
			s[x+2000000]=c;
			if(c>1)
				q.push(x+2000000);
		}
		int res=0;
    while(!q.empty()) {
      int x=q.front();
      q.pop();
      used[x]=false;
      res+=s[x]/2;
      s[x-1]+=s[x]/2;
      s[x+1]+=s[x]/2;
      s[x]&=1;
      if(s[x-1]>1 && !used[x-1]) {
        used[x-1]=true;
        q.push(x-1);
      }
      if(s[x+1]>1 && !used[x+1]) {
        used[x+1]=true;
        q.push(x+1);
      }
    }
    printf("Case #%d: %d\n",test,res);
	}
	return 0;
}
