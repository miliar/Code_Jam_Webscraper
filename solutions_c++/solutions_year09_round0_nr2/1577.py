#include "iostream"
#include "set"
using namespace std;

const int maxn=128;
struct node{
	int x,y,val;
	bool operator < (const node& b) const{
		return val < b.val;
	}
};
int g[maxn*maxn];
int f[maxn*maxn];
int H,W;
int flag[maxn*maxn];

int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};

int getid(int x,int y)
{
	return x*W+y;
}

void getxy(int id, int& x,int &y)
{
	x=id/W;
	y=id%W;
}

int getf(int id)
{
	if(f[id] != id){
		f[id] = getf(f[id]);
	}
	return f[id];
}

void input()
{
	int i,j;
	scanf("%d%d",&H,&W);
	for(i=0;i<H;++i){
		for(j=0;j<W;++j){
			scanf("%d",&g[getid(i,j)]);
			f[getid(i,j)]=getid(i,j);
		}
	}
}

void merge(int id1,int id2)
{
	if(getf(id1)!=getf(id2)){
		f[getf(id1)] = getf(id2);
	}
}

bool inside(int x,int y)
{
	if(x<0 || y<0 || x>=H || y>=W) return false;
	return true;
}

void solve()
{
	int k;
	int i,j,x,y,d,ch1,ch2;
	for(i=0;i<H;++i){
		for(j=0;j<W;++j){
			ch1=-1;
			for(d=0;d<4;++d){
				x=i+dx[d];
				y=j+dy[d];
				if(!inside(x,y)) continue;
				if(g[getid(i,j)]>g[getid(x,y)]){
					//merge(getid(i,j),getid(x,y));
					//break;
					if(ch1<0 || g[getid(x,y)] <ch2){
						ch1=getid(x,y);
						ch2=g[ch1];
					}
				}
			}
			if(ch1>=0){
				merge(getid(i,j),ch1);
			}
		}
	}
	int cot=0;
	memset(flag,-1,sizeof(flag));
	for(i=0;i<H;++i){
		for(j=0;j<W;++j){
			k=getf(getid(i,j));
			if(flag[k]<0) flag[k]=cot++;
		}
	}
	for(i=0;i<H;++i){
		for(j=0;j<W;++j){
			k=getf(getid(i,j));
			printf("%c",flag[k]+'a');
			if(j!=W-1) printf(" ");
			else printf("\n");
		}
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B2.out","w",stdout);
	int i,T;
	scanf("%d",&T);
	for(i=1;i<=T;++i){
		input();
		printf("Case #%d:\n",i);
		solve();
	}
	return 0;
}