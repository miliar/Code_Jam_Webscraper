//Pipe input file to program and pipe output of program to outfile

#include <stdio.h>
#include <vector>
using namespace std;

#define debug 1
#define dprintf debug&&printf

struct sets {
	struct set_elem {
		int h, rank; // rank is a pseudo-height with height“¡=rank
		set_elem(int elem) : h(elem), rank(0) {}
	};
	vector<set_elem> elems;
	sets(int nElems) {
		for(int i = 0; i < nElems; i++) elems.push_back(set_elem(i));
	}
	int get_head(int i) { // Find set-head with path-compression
		if (i != elems[i].h) elems[i].h = get_head(elems[i].h);
		return elems[i].h;
	}
	bool equal(int a, int b){ return (get_head(a)==get_head(b)); }
	void link(int a, int b) { // union sets
		a = get_head(a); b = get_head(b);
		if(elems[a].rank > elems[b].rank) elems[b].h = a;
		else {
			elems[a].h = b;
			if(elems[a].rank == elems[b].rank) elems[b].rank++;
		}
	}
};

int height[128][128];
int dx[4] = {0,-1,1,0};
int dy[4] = {-1,0,0,1};
char headLetter[128*128];

int main(){
	int N;
	scanf("%d\n", &N);
	for(int fall=0;fall<N;fall++){	
		printf("Case #%d:\n", fall+1);
		int H, W;
		scanf("%d %d", &H, &W);
		sets s(H*W);
		for(int y=0;y<H;y++){
			for(int x=0;x<W;x++){				
				scanf("%d", &height[y][x]);
				headLetter[W*y+x] = 0;
			}
		}
		for(int y=0;y<H;y++){
			for(int x=0;x<W;x++){
				int min = 1<<30;
				for(int dir=0;dir<4;dir++){
					int y2=y+dy[dir];
					int x2=x+dx[dir];
					if(0<=y2 && y2<H && 0<=x2 && x2<W && height[y2][x2] < min){
						min = height[y2][x2];
					}
				}
				for(int dir=0;dir<4;dir++){
					int y2=y+dy[dir];
					int x2=x+dx[dir];
					if(0<=y2 && y2<H && 0<=x2 && x2<W && height[y2][x2] == min && min < height[y][x]){
						s.link(W*y+x, W*y2+x2);
						break;
					}
				}
			}
		}
		char nextLetter = 'a';
		for(int y=0;y<H;y++){
			for(int x=0;x<W;x++){				
				int head = s.get_head(W*y+x);
				if(!headLetter[head]){
					headLetter[head] = nextLetter++;
				}
				if(x)printf(" ");
				printf("%c", headLetter[head]);
			}
			printf("\n");
		}
	}
	return 0;
}
