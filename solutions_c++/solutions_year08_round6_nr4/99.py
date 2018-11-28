#include <cstdio>
#include <memory.h>
int a[11][11];
int b[11][11];
int n,m;
int c[11];
int d[11];
bool ok = false;
void go(int x, int y, int z){
	if(x==n+1){
		bool gg = true;
		for(int i=1; i<=m; i++){
			for(int j=1; j<=m; j++){
				if(a[c[i]][c[j]] == false && b[i][j] == true)
					gg = false;
			}
		}
		if(gg)
			ok=true;
	}
	for(int i=1; i<=m; i++){
		if(c[i]==0){
			c[i] = x;
			d[x] = i;
			go(x+1,y,z+1);
			c[i] = 0;
			d[x] = 0;
		}
	}
	if(y < n-m){
		go(x+1,y+1,z);
	}
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tt;
	scanf("%d\n",&tt);
	for(int tc=1; tc<=tt; tc++){
		scanf("%d\n",&n);
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));

		for(int i=1; i<=n-1; i++){
			int t1,t2;
			scanf("%d %d\n",&t1,&t2);
			a[t1][t2] = a[t2][t1] = 1;
		}
		scanf("%d\n",&m);
		for(int i=1; i<=m-1; i++){
			int t1,t2;
			scanf("%d %d\n",&t1,&t2);
			b[t1][t2] = b[t2][t1] = 1;
		}
		ok = false;
		memset(c,0,sizeof(c));
		memset(d,0,sizeof(d));
		go(1,0,0);
		printf("Case #%d: ",tc);
		if(ok)
			printf("YES\n");
		else
			printf("NO\n");
		
	}

	return 0;
}