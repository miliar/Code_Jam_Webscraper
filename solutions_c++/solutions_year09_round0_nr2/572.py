#include "stdio.h"
#include <vector>
#include <stack>
using namespace std;

class point {
public:
	int a;
	char basin;
	int need_assign;
	point *nxt_p;
	vector <point *> former;
public:
	point() { a=0; nxt_p=this; need_assign=1;};
};

class stack_p {
private:
	int num;
	point *p[10001];
public:
	stack_p() { num=0;};
	bool empty() {return (num==0);}
	point * pop() {num--; return p[num]; };
	void push( point *np ) { p[num]=np; num++; return;};
};

int main ( int argc,char *argv[] ) {
	FILE *fin, *fout;
	fin = fopen ( argv[1], "r" );
	if ( ! fin ) return 0;
	fout = fopen ( argv[2], "w" );
	if ( ! fout ) return 0;
	int T, W, H;
	int i,j,k,l,ll;
	int temp;
	fscanf(fin, "%d\n", &T);
	point ** map=NULL;
	char c;
	stack_p s_p;
	point *cp, *np, *bp;
	for (i=0; i<T; i++) {
		c = 'a';
		fscanf(fin, "%d %d\n", &H, &W);
		if ( map ) delete map;
		map = new point* [H];
		for(j=0; j<H; j++) {
			map[j] = new point [W];
			for (k=0; k<W-1; k++) {
				fscanf(fin, "%d ", &(map[j][k].a));
			}
			fscanf(fin, "%d\n", &(map[j][k].a));
		}
		for(j=0; j<H; j++) {
			for(k=0; k<W; k++) {
				temp = map[j][k].a;
				if(j!=0) {
					if ( map[j-1][k].a<temp) {
						temp = map[j-1][k].a;
						map[j][k].nxt_p = &(map[j-1][k]);
					}
				}
				if(k!=0) {
					if ( map[j][k-1].a<temp) {
						temp = map[j][k-1].a;
						map[j][k].nxt_p = &(map[j][k-1]);
					}
				}
				if(k!=W-1) {
					if ( map[j][k+1].a<temp) {
						temp = map[j][k+1].a;
						map[j][k].nxt_p = &(map[j][k+1]);
					}
				}
				if(j!=H-1) {
					if ( map[j+1][k].a<temp) {
						temp = map[j+1][k].a;
						map[j][k].nxt_p = &(map[j+1][k]);
					}
				}
				if (map[j][k].nxt_p != &(map[j][k])) {
					map[j][k].nxt_p->former.push_back(&(map[j][k]));
				}
			}
		}
		for(j=0; j<H; j++) {
			for(k=0; k<W; k++) {
				if(map[j][k].need_assign) {
					map[j][k].basin=c;
					map[j][k].need_assign=0;
					cp = &(map[j][k]);
					np = cp->nxt_p;
					while (cp != np ) {
						cp = np;
						np = np->nxt_p;
					}
					bp = np;
					s_p.push(bp);
					while(!s_p.empty()) {
						cp = (point *)s_p.pop();
						ll = cp->former.size();
						if (cp->need_assign) {
							cp->basin = c;
							cp->need_assign = 0;
						}
						for (l=0; l<ll; l++)	s_p.push(cp->former[l]);
					}
					c++;
				}
			}
		}
		fprintf(fout,"Case #%d:\n", i+1);
		for (j=0; j<H; j++) {
			for (k=0; k<W-1; k++) {
				fprintf(fout, "%c ", map[j][k].basin);
			}
			fprintf(fout, "%c\n", map[j][k].basin);
		}
	}
	fclose ( fin );
	fclose (fout);
	return 1;
}