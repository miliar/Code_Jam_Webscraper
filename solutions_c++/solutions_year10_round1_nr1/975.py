#include <stdio.h>
#include <string.h>
#define N 60
char input[N][N];
char rote[N][N];
bool f[N][N];
int n, k;
int cr, cb;

void rotate()
{
	int i, j, i1, j1;
	memset(&rote, 0, sizeof(rote));
	for(i = 0, i1 = n - 1; i < n; i++, i1--) {
		for(j1 = n - 1, j = n - 1; j1 >= 0; j1--) {
			if(input[i1][j1] != '.')rote[j--][i] = input[i1][j1];
		}
		while(j >= 0) rote[j--][i] = '.';
	}
//	for(i = 0; i < n; i++)printf("%s\n", rote[i]);
}

void checkRight()
{
	int i, j;
	char my;
	int count = 0;
	for(i = 0; i < n; i++) {
		my = rote[i][0];
		if(my != '.')count=1;
		for(j = 1; j < n; j++) {
			if(rote[i][j] != '.') {
				if(rote[i][j] == my){
					count++;
					if(count >= k) {
						if(my == 'R')cr = 1;
						else cb = 1;
					}
				} else {
					my = rote[i][j];
					count = 1;
				}
			} else {
				my = '.';count = 0;
			}
		}
	}
}

void checkDown()
{
	int i, j;
	int my;
	int count;
	for(i = 0; i < n; i++) {
		my = rote[0][i];
		if(my != '.')count=1;
		for(j = 1; j < n; j++) {
			if(rote[j][i] != '.') {
				if(rote[j][i] == my){
					count++;
					if(count >= k) {
						if(my == 'R')cr = 1;
						else cb = 1;
					}
				} else {
					my = rote[j][i];
					count = 1;
				}
			} else {
				my = '.';count = 0;
			}
		}
	}
}

void checkRig()
{
	int i, j, t;
	int count = 0;
	char my;
	for(t = 0; t < n; t++) {
		i = 0; j = t;
		my = rote[i++][j++];
		if(my != '.') count = 1;
		while(j < n) {
			if(rote[i][j] != '.') {
				if(rote[i][j] == my){
					count++;
					if(count >= k) {
						if(my == 'R')cr = 1;
						else cb = 1;
					}
				} else {
					my = rote[i][j];
					count = 1;
				}
			} else {
				my = '.';count = 0;
			}
			i++;j++;
		}
	}

	for(t = 1; t < n; t++) {
		i = t; j = 0;
		my = rote[i++][j++];
		if(my != '.') count = 1;
		while(i < n) {
			if(rote[i][j] != '.') {
				if(rote[i][j] == my){
					count++;
					if(count >= k) {
						if(my == 'R')cr = 1;
						else cb = 1;
					}
				} else {
					my = rote[i][j];
					count = 1;
				}
			} else {
				my = '.';count = 0;
			}
			i++;j++;
		}
	}
}

void checkLeft()
{
	int i, j, t;
	int count = 0;
	char my;
	for(t = 0; t < n; t++) {
		i = 0; j = t;
		my = rote[i++][j--];
		if(my != '.') count = 1;
		while(j >= 0 && i < n) {
			if(rote[i][j] != '.') {
				if(rote[i][j] == my){
					count++;
					if(count >= k) {
						if(my == 'R')cr = 1;
						else cb = 1;
					}
				} else {
					my = rote[i][j];
					count = 1;
				}
			} else {
				my = '.';count = 0;
			}
			i++;j--;
		}
	}

	for(t = 1; t < n; t++) {
		i = t; j = n-1;
		my = rote[i++][j--];
		if(my != '.') count = 1;
		while(i < n && j >= 0) {
			if(rote[i][j] != '.') {
				if(rote[i][j] == my){
					count++;
					if(count >= k) {
						if(my == 'R')cr = 1;
						else cb = 1;
					}
				} else {
					my = rote[i][j];
					count = 1;
				}
			} else {
				my = '.';count = 0;
			}
			i++;j--;
		}
	}
}

void check()
{
	checkRight();
	checkLeft();
	checkDown();
	checkRig();
}

int main()
{
	int t;
	int i, j;
	freopen("Download A-small.in","r",stdin);freopen("Download A-small.out","w",stdout);
	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		scanf("%d %d", &n, &k);
		for(j = 0; j < n; j++)scanf("%s", &input[j]);
		rotate();
		cr = cb = 0;
		check();
		if(cr == 1 && cb == 1)printf("Case #%d: Both\n", i);
		else if(cr == 0 && cb == 0)printf("Case #%d: Neither\n", i);
		else if(cr == 1) printf("Case #%d: Red\n", i);
		else printf("Case #%d: Blue\n", i);
	}
	return 0;
}