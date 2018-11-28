#include<stdio.h>
#include<map>
#include<string>
#include<memory.h>
using namespace std;

int query[1000], far[1000];
unsigned dist[100];
int main() {
	int N;
	scanf("%d", &N);
	for(int cas=1;cas<=N;cas++) {
		int S;
		char name[200];
		map<string, int> ns;

		scanf("%d", &S);
		gets(name);
		for(int i=0;i<S;i++) {
			gets(name);
			int t=ns.size();
			ns[name]=t;
		}

		int Q;
		scanf("%d", &Q);
		if(!Q) {
			printf("Case #%d: 0\n", cas);
			continue;
		}

		gets(name);
		for(int i=0;i<Q;i++) {
			gets(name);
			query[i]=ns[name];
		}
		
		memset(dist, -1, sizeof(dist));
		for(int i=Q-1;i>=0;i--) {
			dist[query[i]]=i;

			unsigned mx=0, mxid;
			for(int j=0;j<S;j++) {
				if(dist[j]>mx) mx=dist[j], mxid=j;
			}

			if(mx==-1) far[i]=-1;
			else far[i]=dist[mxid];
		}

		int cnt=0;
		for(int i=0;i!=-1;i=far[i]) cnt++;
		printf("Case #%d: %d\n", cas, cnt-1);
	}
	return 0;
}