//BISMILLAHHIRRAHMANIRRAHIM


#include <iostream>
#include <cstring>
using namespace std;

bool visit[110][110];
char * color[110][110];
char p[]="abcdefghijklmnopqrstuvwxyz";
char s[12100];
int	h,w,lc;
int map[110][110];
int mv[4][2]={-1,0,0,-1,0,1,1,0};

void flood(int x,int y,char *c/*,int v*/) {
	if(color[x][y]) (*c)=(*color[x][y]);
	else {
		//v++;
		color[x][y]=c;
		int x1,y1,s=-1,ix,iy;
		for(int i=0;i<4;i++) {
			x1=x+mv[i][0];
			y1=y+mv[i][1];
			//cout<<x<<' '<<y<<' '<<x1<<' '<<y1<<'\n';
			if(x1>=0 && x1<h && y1>=0 && y1<w) if(map[x][y]>map[x1][y1]) {
				if(s==-1) {s=map[x1][y1];ix=x1;iy=y1;}
				else if(s>map[x1][y1]) {s=map[x1][y1];ix=x1;iy=y1;}
			}
		}
		if(s==-1) (*c)=p[lc++];
		else flood(ix,iy,c);
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,I=1,c,i,j;
	for(scanf("%d",&t);I<=t;I++) {
		scanf("%d %d",&h,&w);
		for(i=0;i<h;i++) for(j=0;j<w;j++) scanf("%d",&map[i][j]);
		printf("Case #%d:\n",I);
		lc=0;
		memset(color,0,sizeof(color));
		memset(s,0,sizeof(s));
		c=0;
		for(i=0;i<h;i++) for(j=0;j<w;j++) if(!color[i][j]) flood(i,j,&s[c++]);
		for(i=0;i<h;i++) {
			putchar(*color[i][0]);
			for(j=1;j<w;j++) printf(" %c",*color[i][j]);
			putchar('\n');
		}
	}
	return 0;
}
