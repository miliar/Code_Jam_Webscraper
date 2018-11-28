#include <stdio.h>
#include <string.h>
char a[100][104], b[100][104];
int last[100];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T, n, m;
	scanf("%d",&T);
	while(T>0){T--;
		scanf("%d %d",&n,&m);
		int i, j, k;
		for(i=0;i<n;i++){
			scanf("%s",a[i]);
			int l = strlen(a[i]);
			a[i][l] = '/';
			a[i][l+1] = '\0';
		}
		for(i=0;i<m;i++){
			scanf("%s",b[i]);
			int l = strlen(b[i]);
			b[i][l] = '/';
			b[i][l+1] = '\0';
		}
		for(i=0;i<m;i++){
			last[i] = 1;
			for(j=0;j<n;j++){
				for(k=0; ;k++){
					if(b[i][k] != a[j][k] || b[i][k] == '\0'){
						break;
					}
				}
				if(last[i] < k) last[i] = k;
			}
		}
		for(i=0;i<m;i++){
			for(j=0;j<i;j++){
				for(k=0; ;k++){
					if(b[i][k] != b[j][k] || b[i][k] == '\0'){
						break;
					}
				}
				if(last[i] < k) last[i] = k;
			}
		}
		int cnt = 0;
		for(i=0;i<m;i++){
			for(j=last[i];b[i][j] != '\0';j++){
				if(b[i][j] == '/') cnt ++;
			}
		}
		static int t = 1;
		printf("Case #%d: %d\n", t++, cnt);
	}
	return 0;
}