#include <stdio.h>
#include <string>
#include <map>

using namespace std;

int next[1005][105], q[1005];

int main() {
	int t = 1, cases, n, m, i, j, inuse, ans;
	char s[105];
	
	scanf("%d",&cases);
	while (cases--) {
		map <string,int> names;
		
		scanf("%d\n",&n);
		for (i=0; i < n; i++) {
			gets(s);
			names[s] = i;
		}
		
		scanf("%d\n",&m);
		for (i=0; i < m; i++) {
			gets(s);
			q[i] = names[s];
		}
		
		for (j=0; j < n; j++)
			next[m][j] = 1000000000;
		for (i=m-1; i >= 0; i--) {
			for (j=0; j < n; j++)
				next[i][j] = next[i+1][j] + 1;
			next[i][q[i]] = 0;
		}
		
		for (i=0,inuse=-1; i < n; i++)
			if (i != q[0] && (inuse == -1 || next[0][i] > next[0][inuse]))
				inuse = i;
		
		for (i=ans=0; i < m; i++) {
			if (q[i] == inuse) {
				for (j=0,inuse=-1; j < n; j++)
					if (j != q[i] && (inuse == -1 || next[i][j] > next[i][inuse]))
						inuse = j;
				ans++;
			}
		}
		
		printf("Case #%d: %d\n",t++,ans);
	}
	
	return 0;
}
