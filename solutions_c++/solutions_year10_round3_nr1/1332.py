#include <stdio.h>
int height[1009][2];
int num;
int id;

void input() {
	int j;
	
	scanf("%d",&num);
	for(j = 0; j < num; j++)
		scanf("%d%d",&height[j][0],&height[j][1]);
}

void solve() {
	int i,j,rus = 0;
	for(i = 0; i < num; i++) {
		for(j = i + 1; j < num; j++) {
			if((height[j][0] > height[i][0] && height[j][1] < height[i][1])
				||height[j][0] < height[i][0] && height[j][1] > height[i][1])
				++rus;
		}
	}
	printf("Case #%d: %d\n",++id,rus);
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,size;
	scanf("%d",&size);
	for(i = 0; i < size; i++) {
		input();
		solve();
	}
	return 0;
}