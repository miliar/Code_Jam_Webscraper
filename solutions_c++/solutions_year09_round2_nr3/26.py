#include<iostream>
#include<string>
using namespace std;

const int dir[4][2]={{0,-1},{-1,0},{1,0},{0,1}};

const int Lo = -1000;
const int Hi = 1000;
const int bas = 1000;

const int MaxN = 22;
const int Size = Hi-Lo+1;

int d[MaxN][MaxN][Size];

string chs[MaxN][MaxN][Size];

int que[MaxN*MaxN*Size][3], fron, tail;

char g[MaxN][MaxN];
int N, Q;

int run() {
	scanf("%d %d", &N, &Q);
	for(int i=0;i<N;++i) 
		scanf("%s", g[i]);
	memset(d, -1, sizeof(d));
	fron=tail=0;
	for(int i=0;i<N;++i)
		for(int j=0;j<N;++j)
			if(isdigit(g[i][j])) {
				que[tail][0]=i;que[tail][1]=j;que[tail++][2]=bas;
				d[i][j][bas]=0; chs[i][j][bas]="";
			}
	while(fron<tail) {
		int x=que[fron][0], y=que[fron][1], k=que[fron][2];
		++fron;
		int cd = d[x][y][k];
		string now=chs[x][y][k];
		for(int d1=0;d1<4;++d1) {
			int mx=x+dir[d1][0], my=y+dir[d1][1];
			if(mx<0||my<0||mx>=N||my>=N) continue;
			int sg=(g[mx][my]=='+'?1:-1);
			int tk = k + sg * (g[x][y]-'0');
			if(tk<0||tk>=Size) continue;
			for(int d2=0;d2<4;++d2) {
				int sx=mx+dir[d2][0],sy=my+dir[d2][1];
				if(sx<0||sy<0||sx>=N||sy>=N) continue;
				int &td=d[sx][sy][tk];
				if(td>-1 && td<cd+1) continue;
				string cur;
				cur.push_back(g[mx][my]);cur.push_back(g[x][y]);cur.insert(cur.end(),now.begin(),now.end());
				string &tarchs = chs[sx][sy][tk];
				if(td<0||tarchs > cur) {
					if(td<0) {
						que[tail][0]=sx;que[tail][1]=sy;que[tail][2]=tk;++tail;
					}
					td=cd+1;tarchs=cur;
				}
			}
		}
	}
	while(Q--) {
		int k; cin>>k;
		int len = 0x7fffffff;
		string ans = "Z";
		for(int i=0;i<N;++i)
			for(int j=0;j<N;++j)
				if(isdigit(g[i][j])) {
					int tk=k-(g[i][j]-'0')+bas;
					if(d[i][j][tk]<0) continue;
					int td=d[i][j][tk];
					string now;
					now.push_back(g[i][j]); now+=chs[i][j][tk];
					if(td<len||(td==len&&now<ans)) {
						len = td; ans = now;
					}
				}
		cout<<ans<<endl;
	}
}

int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int test; scanf("%d", &test);
	for(int no=1; no<=test; ++ no) {
		printf("Case #%d:\n", no);
		run();
	}
}
