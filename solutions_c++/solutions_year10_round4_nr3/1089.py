#include <cstdio>
#include <cstring>

bool a[101][101];
bool b[101][101];
int C,R;
int x1,x2,y1,y2;
int m,n;
bool flag;

void transform(bool p[101][101],bool q[101][101]){
	memset(q,0,sizeof(a));
	for(int i = 1;i <= m;++i){
		for(int j = 1;j <= n;++j){
			q[i][j] = p[i][j];
			if(p[i][j] == 0 && p[i-1][j] && p[i][j-1]){
				flag = 1;
				q[i][j] = 1;
				continue;
			}
			if(p[i][j]){
				if(p[i-1][j] == 0 && p[i][j-1] == 0){
					q[i][j] = 0;
					continue;
				}
				flag = 1;
			}
		}
	}
}

int main(){
	freopen("out.txt","w",stdout);
	scanf("%d",&C);
	for(int c = 1;c <= C;++c){
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		scanf("%d",&R);
		m = 0;n = 0;
		while(R--){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			m = x2>m?x2:m;
			n = y2>n?y2:n;
			for(int i = x1;i <= x2;++i)
				for(int j = y1;j <= y2;++j)
					a[i][j] = 1;
		}
		flag = 1;
		int t = 0;
		while(flag){
			++t;
			flag = 0;
			if(t%2==0)
				transform(b,a);
			else
				transform(a,b);
		}
		printf("Case #%d: %d\n",c,t);
	}
}