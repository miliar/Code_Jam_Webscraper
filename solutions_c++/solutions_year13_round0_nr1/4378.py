#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <cassert>
#include <cstdlib>
using namespace std;
char a[4][4];
char rcheck(void)
{
	int i,j;
	for(i=0;i<4;i++) {
		if((a[i][0]=='X'||a[i][0]=='T')&&(a[i][1]=='X'||a[i][1]=='T')&&(a[i][2]=='X'||a[i][2]=='T')&&(a[i][3]=='X'||a[i][3]=='T')) {
			return 'X';
		} else if((a[i][0]=='O'||a[i][0]=='T')&&(a[i][1]=='O'||a[i][1]=='T')&&(a[i][2]=='O'||a[i][2]=='T')&&(a[i][3]=='O'||a[i][3]=='T')) {
			return 'O';
		}
	}
	return 'N';
}
char ccheck(void)
{
	int i;
	for(i=0;i<4;i++) {
		if((a[0][i]=='X'||a[0][i]=='T')&&(a[1][i]=='X'||a[1][i]=='T')&&(a[2][i]=='X'||a[2][i]=='T')&&(a[3][i]=='X'||a[3][i]=='T')) {
			return 'X';
		} else if((a[0][i]=='O'||a[0][i]=='T')&&(a[1][i]=='O'||a[1][i]=='T')&&(a[2][i]=='O'||a[2][i]=='T')&&(a[3][i]=='O'||a[3][i]=='T')) {
			return 'O';
			
		}
	}
	return 'N';
}

char dcheck(void)
{
	if((a[0][0]=='X'||a[0][0]=='T')&&(a[1][1]=='X'||a[1][1]=='T')&&(a[2][2]=='X'||a[2][2]=='T')&&(a[3][3]=='X'||a[3][3]=='T')) {
		return 'X';
	} else if((a[0][0]=='O'||a[0][0]=='T')&&(a[1][1]=='O'||a[1][1]=='T')&&(a[2][2]=='O'||a[2][2]=='T')&&(a[3][3]=='O'||a[3][3]=='T')) {
		return 'O';
	}
	if((a[0][3]=='X'||a[0][3]=='T')&&(a[1][2]=='X'||a[1][2]=='T')&&(a[2][1]=='X'||a[2][1]=='T')&&(a[3][0]=='X'||a[3][0]=='T')) {
		return 'X';
	} else if((a[0][3]=='O'||a[0][3]=='T')&&(a[1][2]=='O'||a[1][2]=='T')&&(a[2][1]=='O'||a[2][1]=='T')&&(a[3][0]=='O'||a[3][0]=='T')) {
		return 'O';
	}
	return 'N';
}
int main()
{
	int n;
	scanf("%d",&n);
	int i,j;
	char c;
	int k=0;
	int count=1;
	scanf("%c",&c);
	for(k=1;k<=n;k++) {
		int unmarked = 0;
		for(i=0;i<4;i++) {
			for(j=0;j<4;j++) {
				scanf("%c",&a[i][j]);
				if(a[i][j]=='.') {
					unmarked++;
				}
//				scanf("%c",&c);
			}
			scanf("%c",&c);
		}
		c = rcheck();
		if(c != 'N') {
			printf("Case #%d: %c won\n",k,c);
		} else {
			c = ccheck();
			if(c != 'N') {
				printf("Case #%d: %c won\n",k,c);
			} else {
				c=dcheck();
				if(c != 'N') {
					printf("Case #%d: %c won\n",k,c);
				} else {
					if(unmarked==0) {
						printf("Case #%d: Draw\n",k);
					} else {
						printf("Case #%d: Game has not completed\n",k);
					}
				}
			}
		}
//		scanf("%c",&c);
	}
	return 0;
}
