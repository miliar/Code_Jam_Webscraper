#include<cstdio>
#include<cstdlib>

#define MAXW 105
#define MAXH 105

using namespace std;

struct node {
	char name;
	int rank;
	node *parent;
} *nodes[MAXW][MAXH];

int W, H, h[MAXW][MAXH];
int dx[5] = {0,-1,1,0,0}, dy[5] = {-1,0,0,1,0};

bool valid(int x, int y) {
	return x >= 0 && y >= 0 && x < W && y < H;
}

node *root(node *n) {
	if(n->parent == NULL) return n;
	else return n->parent = root(n->parent);
}

void merge(node *a, node *b) {
	a = root(a); b = root(b);
	if(a==b) return;
	if(a->rank < b->rank) {
		a->parent = b;
	} else if(b->rank < a->rank) {
		b->parent = a;
	} else {
		b->parent = a;
		a->rank++;
	}
}

int main() {
	FILE *fin = fopen("B.in","r"), *fout = fopen("B.out","w");
	int K;
	fscanf(fin,"%d",&K);
	for(int x = 0; x<MAXW; x++) {
		for(int y = 0; y<MAXH; y++) {
			nodes[x][y] = new node;
		}
	}
	for(int k = 0; k<K; k++) {
		fscanf(fin,"%d%d",&H,&W);
		for(int y = 0; y<H; y++) {
			for(int x = 0; x<W; x++) {
				fscanf(fin,"%d",&h[x][y]);
				nodes[x][y]->parent = NULL;
				nodes[x][y]->name = ' ';
				nodes[x][y]->rank = 1;
			}
		}
		for(int x = 0; x<W; x++) {
			for(int y = 0; y<H; y++) {
				int best = 4;
				for(int i = 0; i<4; i++) {
					if(valid(x+dx[i],y+dy[i])) {
						if(best == -1 || h[x+dx[i]][y+dy[i]] < h[x+dx[best]][y+dy[best]]) {
							best = i;
						}
					}
				}
				merge(nodes[x][y],nodes[x+dx[best]][y+dy[best]]);
			}
		}
		char next = 'a';
		fprintf(fout,"Case #%d:\n",k+1);
		for(int y = 0; y < H; y++) {
			for(int x = 0; x<W; x++) {
				if(root(nodes[x][y])->name == ' ') {
					root(nodes[x][y])->name = next;
					next++;
				}
				if(x == 0) {
					fprintf(fout,"%c",root(nodes[x][y])->name);
				} else {
					fprintf(fout," %c",root(nodes[x][y])->name);
				}
			}
			fprintf(fout,"\n");
		}
	}
	fclose(fin); fclose(fout);
	return 0;
}
