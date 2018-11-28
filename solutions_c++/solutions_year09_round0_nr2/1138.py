#include<cstdio>
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))
int nb[10000];
int pre[10000];
int deg[10000];
char letter[10000];
int H,W;
int dx[4]={0,-1,1,0},dy[4]={-1,0,0,1};
int FIND(int a){
    if(pre[a]==a) return a;
    return pre[a]=FIND(pre[a]);
}
void UNION(int x, int y){
    int a = FIND(x), b = FIND(y);
    if(a!=b){
	if(deg[a]>deg[b]){pre[b]=a; ++deg[a];}
	else {pre[a]=b; ++deg[b];}
    }
}
inline bool OK(const int &a, const int &b){return 0<=a&&a<H&&0<=b&&b<W;}
int findmin(int i, int j){
    int res=W*i+j, h=nb[res];
    REP(k,4)
	if(OK(i+dy[k],j+dx[k])&&h>nb[W*(i+dy[k])+j+dx[k]]){
	    h=nb[W*(i+dy[k])+j+dx[k]];
	    res = W*(i+dy[k])+j+dx[k];}
    return res;
}
int main()
{
  int T;
  scanf("%d", &T);
  REP(iT,T){
    printf("Case #%d:\n", iT+1);
    int tmp; char tmpc='a'; scanf("%d%d", &H, &W);
    REP(i,H) REP(j,W) scanf("%d", &nb[W*i+j]);
    REP(i,H) REP(j,W) pre[W*i+j]=W*i+j;
    REP(i,H) REP(j,W) deg[W*i+j]=0;
    REP(i,H) REP(j,W) {tmp=findmin(i,j); UNION(tmp, W*i+j);}
    REP(i,H) REP(j,W) letter[W*i+j]=0;
    REP(i,H) REP(j,W) {
	tmp=FIND(W*i+j);
	if(letter[tmp]) letter[W*i+j]= letter[tmp];
	else {letter[tmp]=letter[W*i+j]=tmpc; ++tmpc;}
      }
    REP(i,H) {REP(j,W) printf("%c ", letter[W*i+j]); printf("\n");}
  }
  return 0;
}
