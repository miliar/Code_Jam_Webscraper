#define _CRT_SECURE_NO_WARNINGS
#include <map> 
#include <set> 
#include <queue> 
#include <bitset> 
#include <valarray> 
#include <complex> 
#include <iostream> 
#include <sstream> 
#include <cmath> 
#include <algorithm> 
#include <string> 
#include <cassert>
#include <ctime>

#ifdef _MSC_VER
#pragma comment(linker,"/STACK:20000000")
#endif

using namespace std;

// prewritten code

#define Size(x) (int)(x).size()
#define For(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define RepV(i,v) for (int i=0;i<Size(v);++i)
#define All(c) (c).begin(),(c).end()
#define Fill(a,b) memset(&a,b,sizeof(a))
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define Abs(a) ((a)<0?-(a):(a))
#define VVI vector<vector<int> >
#define VI vector<int>
#define VVS vector<vector<string> >
#define VS vector<string>
#define ForEach(it,a) for (typeof((a).begin()) it=(a).begin(); it!=(a).end(); ++it)
#define DBG(x) cout << #x <<" = "<< x << endl;
#define DBGA(x) {cout << #x <<": "; for (int i=0; i<(int)sizeof(x)/(int)sizeof(x[0]); ++i) cout<<x[i]<<' '; cout<<endl;}
#define DBGV(x) {cout << #x <<": "; for (int i=0; i<(int)Size(x); ++i) cout<<x[i]<<' '; cout<<endl;}
#define PB push_back
#define MP make_pair

const string problem_name = "2";

struct state{
	int r, c, rr, cc, dir;
};

int rows, cols, needR=-1, needC=-1;
char s[20][20];
int was[20][20][20][20][5];

const int dr[]={0,0,-1,1};
const int dc[]={-1,1,0,0};

void solve_case(){
	
	scanf("%d%d\n",&rows,&cols);
	For(i,0,rows-1) gets(s[i]);
	
	state st;
	For(i,0,rows-1) For(j,0,cols-1) if (s[i][j] == 'O'){
		st.r=i; st.c=j; st.rr=0;st.cc=0; st.dir=4;
		s[i][j]='.';
	} else if (s[i][j]=='X'){
		needR=i; needC=j;
		s[i][j]='.';
	}
	
	deque<state> q;
	int res=-1;
	q.PB(st);
	Fill(was,-1);
	was[st.r][st.c][st.rr][st.cc][st.dir] = 0;
	while (!q.empty()){
		state cur = q[0]; q.erase(q.begin());
		int dist=was[cur.r][cur.c][cur.rr][cur.cc][cur.dir];
		if (cur.r==needR && cur.c==needC) {
			res = dist;
			break;
		}
		
		For(i,0,3) {
			int r=cur.r, c=cur.c;
			while (r>=0&&r<rows&&c>=0&&c<cols&&s[r][c]=='.') r+=dr[i],c+=dc[i];
			r-=dr[i]; c-=dc[i];
			state next = cur;
			next.rr=r; next.cc=c; next.dir=i;
			if (was[next.r][next.c][next.rr][next.cc][next.dir]==-1){
				was[next.r][next.c][next.rr][next.cc][next.dir]=dist;
				q.push_front(next);
			}
		}

		For(i,0,3) {
			int nr=cur.r+dr[i];
			int nc=cur.c+dc[i];
			if (nr>=0&&nr<rows&&nc>=0&&nc<cols&&s[nr][nc]=='.'&&was[nr][nc][cur.rr][cur.cc][cur.dir]==-1){
				state next=cur;
				next.r=nr; next.c=nc;
				was[nr][nc][cur.rr][cur.cc][cur.dir] = dist+1;
				q.PB(next);
			}
		}

		For(i,0,3){
			int r=cur.r+dr[i], c=cur.c+dc[i];
			if ((r==-1||c==-1||r==rows||c==cols||s[r][c]=='#') && cur.dir!=4){
				state next=cur;
				next.r=cur.rr; next.c=cur.cc;
				if (was[next.r][next.c][next.rr][next.cc][next.dir]==-1){
					was[next.r][next.c][next.rr][next.cc][next.dir]=dist+1;
					q.PB(next);
				}
			}
		}
	}

	if (res == -1) printf("THE CAKE IS A LIE\n");
	else printf("%d\n",res);
}

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
	
	int _t;
	scanf("%d\n",&_t);
	
	For(_z,1,_t){
		printf("Case #%d: ",_z);
		
		solve_case();
		
		fflush(stdout);
	}
	
	return 0;
}
