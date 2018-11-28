#include <iostream>
#include <string>
#include <cstring>
#include <map>
#define M 100010

using namespace std;
struct box{
	int to;
	box *s;
}edge[M],*h[M],*cur;
map <string,int> mp;
int cnt,fa[M];
bool u[M];
void addEdge(int x,int y){
//	printf("Add %d to %d\n",x,y);
	cur->to = y,cur->s = h[x],h[x] = cur++;
}
int getId(string st,bool f){
	if (!mp[st]){
		mp[st] = ++cnt;
		if (f && !u[cnt])
			u[cnt] = true;
	}
	return mp[st];
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,t,P,n,m,i,j,cL,lx,cd,r;
	string st,cst;
	scanf("%d",&T);
	for (t = 1;t <= T;t++){
		memset(fa,-1,sizeof(fa));
		memset(h,0,sizeof(h));
		memset(u,0,sizeof(u));
		mp.clear();
		cur = edge,cnt = 0;
		scanf("%d%d",&n,&m);
		P = n+m;
		for (i = 0;i < P;i++){
			cin >> st;
			cL = st.size();
			lx = getId("root",1);
//			printf("%d : (%d)",i,lx);
			j = 0,cst = "";
			while (j < cL){
				cst += st[j++];
				while (j < cL && st[j] != '/')
					cst += st[j++];
				cd = getId(cst,i < n);
				if (fa[cd] == -1){
					fa[cd] = lx;
					addEdge(lx,cd);
				}
//				cout << cst+" " << cd << " " << fa[cd] << endl;
				lx = cd;
			}
		}
		r = 0;
		for (i = 2;i <= cnt;i++)
			if (!u[i])
				r++;
		printf("Case #%d: %d\n",t,r);
	}
	fclose(stdout);
}
