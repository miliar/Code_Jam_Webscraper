#include<stdio.h>
#include<algorithm>
#include<math.h>
using namespace std;

template<class _Ty> inline
_Ty GetInt(_Ty &c) {
	char t=0;
	c=0;
	while(t<'0'||t>'9')t=getchar();
	do {
		c=c*10+(t-'0');
		t=getchar();
	}while(t>='0'&&t<='9');
	return c;
}

int dist[1024][1024];
struct dat {
	short x, y;
	dat() { }
	dat(short _x, short _y) : x(_x), y(_y) { }
	bool operator<(const dat &b) const {
		return dist[x][y]>dist[b.x][b.y];
	}
};
const int quesize=1000010;
dat heap[quesize];
int idx[1024][1024];
dat from[1024][1024];

void inline hp_move(int a, const dat &b) {
	heap[a]=b;
	idx[b.x][b.y]=a;
}

template<typename HT> inline
void hp_sink(HT heap[], int hs, int p) {
	HT a=heap[p];
	heap--; p++;
	for(int q=p<<1; q<=hs; p=q, q<<=1) {
		if(q<hs && heap[q]<heap[q+1]) q++;
		if(heap[q]<a) break;
		hp_move(p-1, heap[q]);
	}
	hp_move(p-1, a);
}

template<typename HT> inline
void hp_swim(HT heap[], int hs, int p) {
	HT a=heap[p];
	heap--; p++;
	for(int q=p>>1; q>0 && heap[q]<a; p=q, q>>=1) hp_move(p-1, heap[q]);
	hp_move(p-1, a);
}

template<typename HT> inline
void hp_modify(HT heap[], int hs, int p) {
	hp_swim(heap, hs, p);
	hp_sink(heap, hs, p);
}

template<typename HT> inline
void hp_delete(HT heap[], int &hs, int p) {
	hp_move(p, heap[--hs]);
	hp_modify(heap, hs, p);
}

template<typename HT> inline
void hp_insert(HT heap[], int &hs, const HT &e) {
	hp_move(hs++, e);
	hp_modify(heap, hs, hs-1);
}

int dx[8]={0,0,-1,1,-1,-1,1,1};
int dy[8]={1,-1,0,0,-1,1,-1,1};

int dis(dat a,dat b) {
	return (a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y);
}

double solve() {
	int n, m, hs=0;	
	GetInt(n); GetInt(m);

	const int inf=200000000;
	for (int i=0;i<n;i++) {
		for (int j=0;j<m;j++) {
			char a;
			while((a=getchar())!='0'&&a!='1');
			dat b=dat(i, j);
			if (a=='1') {
				dist[i][j]=0;
				from[i][j]=b;
				heap[hs++]=b;
			} else dist[i][j]=inf;
		}
	}
	make_heap(heap, heap+hs);
	for(int i=0;i<hs;i++)
		idx[heap[i].x][heap[i].y]=i;

	while (hs>0) {
		dat b=heap[0];
		hp_delete(heap, hs, 0);

		for (int i=0;i<8;i++) {
			dat cc=dat(b.x+dx[i], b.y+dy[i]);
			double d=dis(cc, from[b.x][b.y]);
			if (cc.x>=0 && cc.x<n && cc.y>=0 && cc.y<m && dist[cc.x][cc.y]>d) {
				bool inh=(dist[cc.x][cc.y]==inf);
				dist[cc.x][cc.y]=d;
				from[cc.x][cc.y]=from[b.x][b.y];
				if(inh) hp_insert(heap, hs, cc);
				else hp_modify(heap, hs, idx[cc.x][cc.y]);
			}
		}
	}

	double mm=0;
	for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
			mm+=sqrt((double)dist[i][j]);

	return mm;
}

int main() {
	int t;
	GetInt(t);
	while(t--)
		printf("%.3lf\n", solve());
	return 0;
}