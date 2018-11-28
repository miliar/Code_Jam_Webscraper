#include <cstdio>
#include <algorithm>
using namespace std;

int c,n,m,R,B,e,t,x,y;
char s[55],S[55][55];

int main(){
	scanf("%d",&c);
	for (int tc=1;tc<=c;tc++){
		scanf("%d%d",&n,&m);
 		memset(S,'.',sizeof(S));
		for (int i=0;i<n;i++){
			scanf("%s",s);
			t=n;
			for (int j=n-1;j>=0;j--)
				if (s[j]!='.') S[--t][n-i-1]=s[j];
		}
		R=B=0;
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++){
				if (S[i][j]=='.') continue;
				e=0;
				x=i;
				y=j;
				for (int k=0;k<m;k++){
					if (x>=n||y>=n) break;
					if (S[x][y]!=S[i][j]) break;
					if (k==m-1) e=1;
    				x++;
				}
				x=i;
				y=j;
				for (int k=0;k<m;k++){
					if (x>=n||y>=n) break;
					if (S[x][y]!=S[i][j]) break;
					if (k==m-1) e=1;
    				y++;
				}
				x=i;
				y=j;
				for (int k=0;k<m;k++){
					if (x>=n||y>=n) break;
					if (S[x][y]!=S[i][j]) break;
					if (k==m-1) e=1;
    				x++,y++;
				}
				x=i;
				y=j;
				for (int k=0;k<m;k++){
					if (x<0||y>=n) break;
					if (S[x][y]!=S[i][j]) break;
					if (k==m-1) e=1;
   					x--,y++;
				}
				if (e){
					if (S[i][j]=='R') R=1;
					else B=1;
				}
			}
		}
		if (!R&&!B) printf("Case #%d: Neither\n",tc);
		if (!R&&B) printf("Case #%d: Blue\n",tc);
 		if (R&&!B) printf("Case #%d: Red\n",tc);
  		if (R&&B) printf("Case #%d: Both\n",tc);

	}
	return 0;
}
