#include <iostream>
#include <algorithm>
using namespace std;

int T, P, Q, a[101], m[101][101];
int ans, tmp;
bool visited[101];

void perm(int list[], int len, int nNext)
{
	int i, j;
	while(nNext--) {
		ans = 0;
		memset(visited, 0, sizeof(visited));
		for(i = 0; i < len; i++) {
			for(j = a[list[i]]+1; j <= P; j++) {
				if(visited[j]) break;
				ans++;
			}
			for(j = a[list[i]]-1; j >= 1; j--) {
				if(visited[j]) break;
				ans++;
			}
			visited[a[list[i]]] = true;
		}
		if(ans < tmp) tmp = ans;
		bool flag = false;
		for(i = len-1; i > 0; i--) {
			if(list[i-1] < list[i]) {
				flag = true;
				break;
			}
		}
		if(flag) {
			int min = list[i], pos = i;
			for(j = i+1; j < len; j++) {
				if(list[j] > list[i-1] && min > list[j]) {
					min = list[j];
					pos = j;
				}
			}
			swap(list[i-1], list[pos]);
			sort(&list[i], &list[len]);
		} else {
			for(i = 0; i < len; i++) {
				list[i] = i+1;
			}
		}
	}
}

int main()
{
	FILE *fp;
	fp = fopen("output.txt", "w");
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases++) {
		scanf("%d%d", &P, &Q);
		int i, j;
		for(i = 1; i <= Q; i++)
			scanf("%d", &a[i]);
		tmp = 100000000;
		int L[100];
		for(i = 0; i < Q; i++) L[i] = i+1;
		if(Q==1) tmp = P-1;
		else if(Q==2) {
			perm(L, 2, 2);
		} else if(Q==3) {
			perm(L, 3, 6);
		} else if(Q==4) {
			perm(L, 4, 24);
		} else if(Q==5) {
			perm(L, 5, 120);
		}
	/*	for(i = 1; i <= Q; i++) {
			memset(visited, 0, sizeof(visited));
			ans = 0;
			DFS(a[i]);
			if(tmp > ans)
				tmp = ans;
		}*/
		fprintf(fp, "Case #%d: %d\n", cases, tmp);
	}
	fclose(fp);
	return 0;
}