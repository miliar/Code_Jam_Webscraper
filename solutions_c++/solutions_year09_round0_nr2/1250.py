#include <cstdio>
#include <cstring>
#include <queue>
#include <map>
using namespace std;

const int dh[] = {-1,0,0,1};
const int dw[] = {0,-1,1,0};

int main() {
  int T,H,W,m[110][110],d[110][110];
  char c[110][110];
  scanf("%d",&T);
  for(int t=0;t<T;++t) {
    scanf("%d %d",&H,&W);
    for(int h=0;h<H;++h)
      for(int w=0;w<W;++w)
	scanf("%d",&m[h][w]);
    for(int h=0;h<H;++h)
      for(int w=0;w<W;++w) {
	d[h][w]=-1;
	int min=m[h][w];
	for(int i=0;i<4;++i)
	  if(h+dh[i]>=0 && w+dw[i]>=0 && h+dh[i]<H && w+dw[i]<W && m[h+dh[i]][w+dw[i]]<min) 
	    min=m[h+dh[i]][w+dw[i]], d[h][w]=i;
      }
    char color='a'-1;
    memset(c,0,sizeof(c));
    for(int h=0;h<H;++h)
      for(int w=0;w<W;++w) {
	if(!c[h][w]) {
	  typedef pair<int,int> pii;
	  queue<pii> q;
	  q.push(pii(h,w));
	  c[h][w]=++color;
	  while(!q.empty()) {
	    pii p = q.front(); q.pop();
	    if(d[p.first][p.second]>=0) {
	      const int _h = p.first+dh[d[p.first][p.second]];
	      const int _w = p.second+dw[d[p.first][p.second]];
	      if(!c[_h][_w])
		c[_h][_w]=color, q.push(pii(_h,_w));
	    }
	    for(int i=0;i<4;++i) {
	      const int _h = p.first+dh[i];
	      const int _w = p.second+dw[i];
	      if(_h>=0 && _w>=0 && _h<H && _w<W)
		if(dh[d[_h][_w]]+dh[i]==0 && dw[d[_h][_w]]+dw[i]==0 && !c[_h][_w])
		  c[_h][_w]=color, q.push(pii(_h,_w));
	    }
	  }
	}
      }
    printf("Case #%d:\n",t+1);
    for(int h=0;h<H;++h) {
      for(int w=0;w<W;++w)
	printf(w?" %c":"%c",c[h][w]);
      printf("\n");
    }
  }
}
