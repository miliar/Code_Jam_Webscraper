#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
using namespace std;

int a[30][30]; // what would be like?
int vis[200];
bool opp[30][30];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("large.out","w",stdout);
	int T, C, D, N;
	char ch[110], tmp[110];
	scanf("%d",&T);
	for(int it = 1;it <= T; ++it){
		memset(vis,0,sizeof(vis));
		memset(opp,false,sizeof(opp));
		memset(a,-1,sizeof(a));
		stack<int> st;
		while(!st.empty()) st.pop();
		scanf("%d",&C);
		for(int i = 1;i <= C; ++i){
			scanf("%s",tmp);
			int u = tmp[0]-'A', v = tmp[1]-'A', w = tmp[2]-'A';
			a[u][v] = a[v][u] = w;
		}
		scanf("%d",&D);
		for(int i = 1;i <= D; ++i){
			scanf("%s",tmp);
			int u = tmp[0]-'A', v = tmp[1]-'A';
			opp[u][v] = opp[v][u] = true;
		}
		scanf("%d",&N);
		scanf("%s",ch);
		for(int i = 0;i < N; ++i){
			int v = ch[i]-'A';	
			if(st.empty()){ st.push(v);vis[v] ++;}
			else{
				bool clear = false, com = false;
				int u = st.top();
				if(a[u][v] != -1){  // combine
					st.pop();
					st.push(a[u][v]);
					vis[u] --;
					vis[a[u][v]] ++;
					com = true;
					for(int j = 0;j < 26; ++j){
						if((vis[j] > 0) && opp[a[u][v]][j]){
							while(!st.empty()) st.pop();
							memset(vis,0,sizeof(vis));
							break;
						}
					}
				}else{
					for(int j = 0;j < 26; ++j){
						if((vis[j]>0) && opp[j][v]){
							while(!st.empty()) st.pop();
							memset(vis,0,sizeof(vis));
							clear = true;
							break;
						}
					}
				}// clear
				if((!clear) && (!com)) { st.push(v);vis[v] ++;}
			}
		}
		int ans[200], cnt = 0;
		while(!st.empty()){ ans[cnt++] = st.top(); st.pop(); }
		printf("Case #%d: ",it);
		if(cnt == 0) printf("[]\n");
		else if(cnt == 1) printf("[%c]\n",ans[0]+'A');
		else{
			printf("[%c",ans[cnt-1]+'A');
			for(int i = cnt-2;i >= 0;--i) 
				printf(", %c",ans[i]+'A');
			printf("]");
			puts("");
		}
	}




}
