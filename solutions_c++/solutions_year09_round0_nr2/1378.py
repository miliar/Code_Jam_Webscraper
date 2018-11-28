#include<cstdio>
#include<algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);++i) 
//   N
//W     E
//   S
int dx[4]={0,-1,1,0};
int dy[4]={-1,0,0,1};
int sink[100][100];
int input[100][100];
int nsinks;
char o[26];
int h,w;
int go(int y,int x) {

  if(sink[y][x]+1) return sink[y][x];
  int a=100000;
  REP(i,4) {
      int nx=x+dx[i],ny=y+dy[i];
      if(ny>=0 && nx>=0 && nx<w && ny<h) {
	  a=min(a,input[ny][nx]);
      }
  }
  if (a>=input[y][x]) return sink[y][x]=nsinks++;
  REP(i,4) {
      int nx=x+dx[i],ny=y+dy[i];
      if(ny>=0 && nx>=0 && nx<w && ny<h) {
	  if(input[ny][nx]==a) return sink[y][x]=go(ny,nx);
      }
  }
  return 0xDEAD;
}
int main() {
    int t;
    scanf("%d",&t);
    REP(C,t) {
	scanf("%d %d",&h,&w);
	printf("Case #%d:\n",C+1);
	nsinks=0;
	
	REP(i,h) REP(j,w) scanf("%d",&input[i][j]);
	REP(i,h) REP(j,w) sink[i][j]=-1;
	REP(i,h) REP(j,w) go(i,j);
	REP(i,nsinks) o[i]='$';
	nsinks=0;

	REP(i,h) {
	    REP(j,w) {
		char c=o[sink[i][j]];
		if(c=='$') c=o[sink[i][j]]='a'+nsinks++;
		printf("%c ",c);
	    }
	    printf("\n");
	}
    }
}
