#include<cstdio>
#include<utility>
#include<cstring>
#include<set>
using namespace std;

int p[110][110];

inline bool nob(int k){
	return k==0||k==-1;
}

inline bool isb(int k){
	return !nob(k);
}



bool process(){
	bool flag=0;
	for(int i=0;i<110;i++)
		for(int j=0;j<110;j++)
			if(p[i][j]){
				flag=1;
				break;
			}
	if(!flag)return 0;
	for(int i=1;i<110;i++)
		for(int j=1;j<110;j++)
			if(p[i][j])
				if(nob(p[i-1][j]) && nob(p[i][j-1]))
					p[i][j]=2;
				else p[i][j]=1;
			else if(isb(p[i-1][j]) && isb(p[i][j-1]))
				p[i][j]=-1;
			else p[i][j]=0;
	for(int i=0;i<110;i++)
		for(int j=0;j<110;j++){
			if(p[i][j]==2)p[i][j]=0;
			if(p[i][j]==-1)p[i][j]=1;
		}
	return 1;
}

void work()
{
	memset(p, 0, sizeof(p));
	int n;
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++) {
		int x1, y1, x2, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int x = x1; x <= x2; x++)
			for (int y = y1; y <= y2; y++)
				p[x][y] = 1;
	}
	int ans = 0;
	while (process()){
		ans++;
	}
	printf("%d\n", ans);
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output","w",stdout);
	int n, m = 0;
	scanf("%d\n", &n);
	while (n--) {
		printf("Case #%d: ", ++m);
		work();
	}
}
