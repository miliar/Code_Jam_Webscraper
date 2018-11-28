#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
#include<queue>
using namespace std;

int tc;
int n,m;
int a[6000],b[6000];
vector<int> edg[2005];
int p[2005][2005],ret[2005],v[2005][2005];
int used[2005];
queue<pair<int,int> > q;

int main() {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&tc);
    for (int T=1; T<=tc; T++) {
		scanf("%d%d",&n,&m);
		for (int i=1; i<=n; i++) edg[i].clear();
		for (int i=0; i<m; i++)
			scanf("%d",&a[i]);
		for (int i=0; i<m; i++)
			scanf("%d",&b[i]);
		for (int i=1; i<=n; i++) {
			a[m]=i; b[m]=i%n+1; m++;
		}
		for (int i=0; i<m; i++) {
			edg[a[i]].push_back(b[i]);
			edg[b[i]].push_back(a[i]);
		}
		for (int i=1; i<=n; i++) {
			sort(edg[i].begin(),edg[i].end());
			for (int j=0; j<edg[i].size(); j++)
				p[i][edg[i][j]]=edg[i][(j+edg[i].size()-1)%edg[i].size()];
		}
		int ans=100000;
		for (int i=0; i<m; i++) {
			//printf("e %d %d\n",a[i],b[i]);
			int fr=a[i],ti,cnt=1;
			int now=b[i],prev=a[i];
			do {
				ti=prev;
				prev=now;
				now=p[now][ti];
				//printf("%d %d\n",prev,now);
				cnt++;
			} while (now!=fr);
			//printf("%d\n",cnt);
			ans=min(ans,cnt);
		}
		printf("Case #%d: %d\n",T,ans);
		q.push(make_pair(1,2));
		memset(v,0,sizeof(v));
		v[1][2]=1;
		memset(ret,0,sizeof(ret));
		int st=0;
		while (!q.empty()) {
			int fr=q.front().first,init,ti;
			int now=q.front().second,prev=fr;
			init=now;
			memset(used,0,sizeof(used));
			used[ret[fr]]=1;
			if (ret[now]==0) {
				ret[now]=1;
				used[1]=1;
			}
			else {
				st=1;
				used[ret[now]]=1;
			}
			//printf("e %d %d\n",fr,now);
			do {
				ti=prev;
				//printf(" === %d %d\n",prev,now);
				//printf("%d = %d\n",now,ret[now]);
				
				prev=now;
				now=p[now][ti];
				if (prev%n+1!=now && v[prev][now]==0) {
					v[prev][now]=1;
					q.push(make_pair(now,prev));
					//printf("add\n");
				}
				//printf("%d = %d\n",now,ret[now]);
				//printf(" === %d %d %d\n",prev,now,ti);
				//for (int i=1; i<=ans; i++) printf("%d",used[i]);
				//printf("\n");
				if (ret[now]==0) {
					for (int i=1; i<=ans; i++)
						if (used[i]==0) {
							ret[now]=i; break;
						}
					if (ret[now]==0) {
						for (int i=1; i<=ans; i++) {
							if (ret[prev]==i || ret[p[now][prev]==i]) continue;
							ret[now]=i; break;
						}
					}
				}
				used[ret[now]]=1;
			} while (now!=fr);
			int ok=0;
			//printf("** %d(%d) %d %d\n",now,ret[now],prev,ti);
			/*
			if (st==0) {
				for (int i=1; i<=ans; i++)
					if (used[i]==0) {
						ret[now]=i;
						used[i]=1;
						ok=1;
						printf("%d!!\n",i);
						break;
					}
				if (ok==0) {
					for (int i=1; i<=ans; i++) {
						if (ret[prev]==i || ret[init]==i) continue;
						ret[now]=i;
						break;
					}
				}
				printf("S* %d = %d\n",now,ret[now]);
			}
			*/
			/*
			else {
				for (int i=1; i<=ans; i++)
					if (used[i]==0) {
						ret[now]=i;
						used[i]=1;
						ok=1;
						break;
					}
				if (ok==0) {
					for (int i=1; i<=ans; i++) {
						if (ret[ti]==i || ret[now]==i) continue;
						ret[prev]=i;
						break;
					}
				}
				printf("* %d = %d\n",prev,ret[prev]);
			}
			*/
			q.pop();
		}
		for (int i=1; i<=n; i++) {
			if (i>1) printf(" ");
			printf("%d",ret[i]);
		}
		printf("\n");
			
	}
}
