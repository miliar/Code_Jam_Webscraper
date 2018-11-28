#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

const int NORTH=0;
const int SOUTH=2;
const int MOVE[][2] = { {-1,0}, {0,1}, {1,0}, {0,-1} };

const int MAXSZ=6500;
const int MID=3250;

bool poly[MAXSZ][MAXSZ];
bool pocket[MAXSZ][MAXSZ];
int x,y, dir;
int MINX, MAXX, MINY, MAXY;
char str[50];
vector<int> wall[MAXSZ];

void doCmd()
{
  int len=strlen(str);
  for(int i=0;i<len;i++) {
    MAXX=max(MAXX, x); MINX=min(MINX, x);
    MAXY=max(MAXY, y); MINY=min(MINY, y);

    if(str[i]=='F' && dir==NORTH) {
      y+=MOVE[dir][0], x+=MOVE[dir][1];
      wall[y].push_back(x);

    } else if(str[i]=='F' && dir==SOUTH) {
      wall[y].push_back(x);
      y+=MOVE[dir][0], x+=MOVE[dir][1];

    } else if(str[i]=='F') {
      y+=MOVE[dir][0], x+=MOVE[dir][1];
    } else if(str[i]=='R') {
      dir++;
      dir%=4;
    } else if(str[i]=='L') {
      dir--;
      if(dir<0) dir+=4;
    }
  }
}

int main()
{
  int tt;
  scanf("%d", &tt);
  for(int t=1;t<=tt;t++) {
    memset(poly,0,sizeof(poly));
    for(int i=0;i<MAXSZ;i++) wall[i].clear();
    int n, l;
    scanf("%d", &n);
    x=MID, y=MID, dir=0;
    MINX=MINY=MAXSZ-5;
    MAXX=MAXY=0;

    while(n--) {
      int rep;
      scanf("%s %d", str, &rep);
      while(rep--)
	doCmd();
    }
    MINX-=5; MINY-=5; MAXX+=5; MAXY+=5;
    for(int i=0;i<MAXSZ;i++)
      sort(wall[i].begin(),wall[i].end());
    
    for(int i=0;i<MAXSZ;i++) {
      for(int j=0;j<wall[i].size();j+=2) {
	int p=wall[i][j];
	while(p<wall[i][j+1])
	  { poly[i][p]=1; p++; }
      }
    }

    //print polygon
    /*printf("POLYGON:\n");
    for(int i=MINY; i<MAXY;i++) {
      for(int j=MINX; j<MAXX;j++)
	printf("%d", poly[i][j]);
      printf("\n");
      }*/
    
    //calc pockets
    memset(pocket,0,sizeof(pocket));
    //horizontal
    int next=-1;
    for(int i=MINY;i<MAXY;i++) {
      for(int j=MINX;j<MAXX;) {
	if(!poly[i][j] && poly[i][j-1]) {
	  int next=j;
	  while(next<MAXSZ && !poly[i][next]) next++;
	  if(next==MAXSZ)
	    { j=MAXSZ; break; }
	  while(j<next)
	    { pocket[i][j]=1; j++; }

	} else
	  j++;
      }
    }

    //vertical
    next=-1;
    int tmp;
    //for(int j=MINX;j<MAXX;j++)
    for(int X=MINX; X<MAXX; X++)
      for(int i=MINY;i<MAXY;) {
	if(!poly[i][X] && poly[i-1][X]) {
	  //printf("Start at y,x= %d, %d\n", i, X);
	  next=i;
	  while(next<MAXSZ && !poly[next][X]) next++;
	  if(next==MAXSZ)
	    { i=MAXSZ; break; }
	  while(i<next)
	    { pocket[i][X]=1; i++; }
	} else 
	  i++;
      }
    
    //print pockets
    /*printf("POCKETS:\n");
    for(int i=MINY; i<MAXY;i++) {
      for(int j=MINX; j<MAXX;j++)
        printf("%d", pocket[i][j]);
      printf("\n");
      }*/
    

    int res=0;
    for(int i=0;i<MAXSZ;i++)
      for(int j=0;j<MAXSZ;j++)
	if(pocket[i][j]) res++;
    printf("Case #%d: %d\n", t, res);

  }
  return 0;
}
