#include<cstdio>
#include<cstring>

#define NMAX 8

class Room {
	public:
		int m,data[NMAX];

		bool contain(int u,int v) {
			int i,cnt=0;
			for(i=0;i<m;i++)if(data[i]==u||data[i]==v)cnt++;
			return cnt==2;
		}

		void add(int x) {
			data[m++]=x;
		}

		void split(int u,int v,Room *a,Room *b) {
			int i,j,k; bool flag=false;
			a->m=0;
			b->m=0;
			for(i=0;i<m;i++)if(data[i]==u)break;
			for(j=0;j<m;j++)if(data[j]==v)break;
			for(k=i;k<m;k++) {
				a->add(data[k]);
				if(k==j)break;
			}
			if(k==m) {
				for(k=0;k<=j;k++)a->add(data[k]);
				for(k=j;k<=i;k++)b->add(data[k]);
			} else {
				for(k=j;k<m;k++)b->add(data[k]);
				for(k=0;k<=i;k++)b->add(data[k]);
			}
		}
};

int n,color[NMAX],mc;
int r; Room room[NMAX-2];
int a,bests[NMAX];

void output(int S) {
	int i;
	printf("Case #%d: %d\n",S,a);
	for(i=0;i<n;i++) {
		if(i)putchar(' ');
		printf("%d",bests[i]+1);
	}
	puts("");
}

void check() {
	static bool has[NMAX];
	int i,j,c,cnt;
	if(mc<=a)return;
	for(i=0;i<r;i++) {
		memset(has,0,mc);
		cnt=0;
		for(j=0;j<room[i].m;j++) {
			c=color[room[i].data[j]];
			if(!has[c]) {
				has[c]=true;
				cnt++;
			}
		}
		if(cnt!=mc)return;
	}
	a=mc;
	memcpy(bests,color,sizeof(color));
}

void dfs(int dep) {
	int i;
	if(dep==n) {
		check();
		return;
	}
	for(i=0;i<mc;i++) {
		color[dep]=i;
		dfs(dep+1);
	}
	color[dep]=mc++;
	dfs(dep+1);
	mc--;
}

void solve() {
	a=0;
	mc=1;
	dfs(0);
}

void line(int u,int v) {
	int i,k=r; Room a,b;
	for(i=0;i<r;i++) {
		if(room[i].contain(u,v)) {
			room[i].split(u,v,&a,&b);
			room[i]=a;
			room[k++]=b;
		}
	}
	r=k;
}

void input() {
	static int L[NMAX-3],R[NMAX-3];
	int m,i;
	scanf("%d%d",&n,&m);
	room[0].m=n;
	for(i=0;i<n;i++)room[0].data[i]=i;
	r=1;
	for(i=0;i<m;i++)scanf("%d",L+i);
	for(i=0;i<m;i++)scanf("%d",R+i);
	for(i=0;i<m;i++)line(L[i]-1,R[i]-1);
}

int main() {
	int T,S;
	scanf("%d",&T);
	for(S=1;S<=T;S++) {
		input();
		solve();
		output(S);
	}
	return 0;
}
