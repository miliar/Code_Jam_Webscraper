#include <cstdio>
#include <algorithm>
using namespace std;

int c,n,m,f,AC;
char s[100][100];

void dfs(int x,int y,int w,int c,int p){
	if (c>f) return;
	if (AC!=-1&&w>AC) return;
	if (x==n-1){
		if (AC==-1||w<AC) AC=w;
	}
	else{
		if (s[x+1][y]=='.') dfs(x+1,y,w,c+1,0);
		else{
			if (y>0&&s[x][y-1]=='.'){
				if (p!=2) dfs(x,y-1,w,0,1);
				if (s[x+1][y-1]=='#'){
				s[x+1][y-1]='.';
				dfs(x,y,w+1,c,0);
				s[x+1][y-1]='#';
				}
			}
			if (y<m-1&&s[x][y+1]=='.'){
				if (p!=1) dfs(x,y+1,w,0,2);
				if (s[x+1][y+1]=='#'){
				s[x+1][y+1]='.';
				dfs(x,y,w+1,c,0);
				s[x+1][y+1]='#';
				}			
			}
		}
	}
}


int main(){
	scanf("%d",&c);
		for (int tc=1;tc<=c;tc++){
		scanf("%d%d%d",&n,&m,&f);
			for (int i=0;i<n;i++) scanf("%s",s[i]);
		AC=-1;
		dfs(0,0,0,0,0);		
			if (AC>=0) printf("Case #%d: Yes %d\n",tc,AC);
			else  printf("Case #%d: No\n",tc);
		}
	return 0;
}



