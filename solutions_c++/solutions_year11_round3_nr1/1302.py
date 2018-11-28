#include <stdio.h>

struct Run {
	Run() {
		read();
		if (solve()) {
			print();
		} else {
			printf("Impossible\n");
		}
	}
	int h,w;
	char grid[100][100];
	void read() {
		scanf("%d %d",&h,&w);
		for (int y=0;y<h;++y) {
			scanf("%s",grid[y]);
		}
	}
	bool solve() {
		for (int y=0;y<h;++y) {
			for (int x=0;x<w;++x) {
				if (grid[y][x]=='#') {
					if (y+1<h && x+1<w && grid[y][x+1]=='#' && grid[y+1][x]=='#' && grid[y+1][x+1]=='#') {
						grid[y][x] = '/';
						grid[y][x+1] = '\\';
						grid[y+1][x] = '\\';
						grid[y+1][x+1] = '/';
					} else {
						return false;
					}
				}
			}
		}
		return true;
	}
	void print() {
		for (int y=0;y<h;++y) {
			printf("%s\n",grid[y]);
		}
	}
};

int main() {
	int runs;
	scanf("%d",&runs);
	for (int i=0;i<runs;++i) {
		printf("Case #%d:\n",i+1);
		Run();
	}
	return 0;
}
