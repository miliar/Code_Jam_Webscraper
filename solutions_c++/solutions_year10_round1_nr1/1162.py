#include <stdio.h>
#include <memory.h>
#define N 51
int n, m;
char map[N][N];

bool awin;
bool bwin;

void print()
{
	int j;
	for(j = 0; j < n; j++) 
	{		
		printf("%s\n", map[j]);		
	}
}

bool check(char c, int x, int y)
{
	int i;

	int k = 1;
	
	for(i = x + 1; i < n; i++) {
		if(map[i][y] == c) {
			k++;
		}else {
			break;
		}
	}
	for(i = x - 1; i >= 0; i--) {
		if(map[i][y] == c) {
			k++;
		}else {
			break;
		}
	}
	if(k >= m) {
		return true;
	}

	k = 1;
	for(i = y + 1; i < n; i++) {
		if(map[x][i] == c) {
			k++;
		} else {
			break;
		}
	}
	for(i = y - 1; i >= 0; i--) {
		if(map[x][i] == c) {
			k++;
		}else {
			break;
		}
	}
	if(k >= m) {
		return true;
	}

	k = 1;
	for(i = 1; x + i < n && y + i < n && i < n; i++) {
		if(map[x + i][y + i] == c) {
			k++;
		}else {
			break;
		}
	}
	for(i = 1; x - i >= 0 && y - i>= 0 && i <= n; i++) {
		if(map[x - i][y - i] == c) {
			k++;
		}else {
			break;
		}
	}
	if(k >= m){
		return true;
	}

	k = 1;
	for(i = 1; x - i < n && y + i < n && i < n; i++) {
		if(map[x - i][y + i] == c) {
			k++;
		}else {
			break;
		}
	}
	for(i = 1; x + i >= 0 && y - i>= 0 && i <= n; i++) {
		if(map[x + i][y - i] == c) {
			k++;
		}else {
			break;
		}
	}
	if(k >= m){
		return true;
	}

	return false;

}

int main()
{
	//freopen("A-small.in.txt", "r", stdin);
	//freopen("A-small.out.txt", "w", stdout);
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);

	int t, i, j, k;
	scanf("%d", &t);
	for(i = 0; i < t; i++)
	{
		memset(map, 0, sizeof(map));
		scanf("%d %d", &n, &m);	
		//printf("%d %d\n", n, m);	
		for(j = 0; j < n; j++) 
		{
			scanf("%s", map + j);			
		}
		//if(i == 63 || i==64)		print();
		for(j = 0; j < n; j++)
		{
			int pos = n - 1;
			for(k = n - 1; k >= 0; k--)
			{
				if(map[j][k] != '.')
				{
					map[j][pos] = map[j][k];
					if(pos != k) {
						map[j][k] = '.';
					}
					pos--;
				}
			}
		}
		//if(i == 63 || i==64)		print();
		awin = false; bwin = false;
		for(j = 0; j < n; j++)
		{			
			for(k = 0; k < n; k++)
			{
				if(!awin && map[j][k] == 'R') {
					if(check('R', j, k)) {
						//printf("R:%d %d\n", j, k);
						awin = true;
					}
				} else if(!bwin && map[j][k] == 'B') {
					if(check('B', j, k)) {
						//printf("B:%d %d\n", j, k);
						bwin = true;
					}
				}
			}
		}
		if(!awin && !bwin) {
			printf("Case #%d: Neither\n", i + 1);
		} else if(awin && bwin) {
			printf("Case #%d: Both\n", i + 1);
		} else if(awin && !bwin) {
			printf("Case #%d: Red\n", i + 1);
		} else if(!awin && bwin) {
			printf("Case #%d: Blue\n", i + 1);
		}
	}
	return 0;
}