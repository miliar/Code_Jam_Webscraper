#include <stdio.h>
#include <string>
#include <algorithm>

using namespace std;

char str[600];
int n,m,grid[600][600],cut[600];
bool visit[600][600];

void pro(int pos, string s) {
	int i,j,x;
	int tmp[600];
	for (i=0;i<s.length();i++) {
		if (s[i]>='0'&&s[i]<='9') x = s[i]-'0';
		else x = s[i]-'A'+10;
		for (j=4*i+3;j>=4*i;j--) {
			tmp[j] = x%2;
			x /= 2;
		}
	}
	for (i=0;i<n;i++) grid[pos][i] = tmp[i];
}

bool ok(int a,int b,int c) { //srow,scol,size
	int i,j,cen = grid[a][b],x;
	//printf ("start %d %d %d\n",a,b,c);
	for (i=a;i<=a+c;i++)
		for (j=b;j<=b+c;j++) {
			x = (cen+i-a+j-b)%2;
			if (visit[i][j] || grid[i][j]!=x) {
				//printf ("fail %d %d\n",i,j);
				return false;
			}
		}
	for (i=a;i<=a+c;i++)
		for (j=b;j<=b+c;j++)
			visit[i][j] = true;
	return true;
}

int main () {
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	int t,ii,in,i,j,lim;
	string s;
	scanf ("%d",&t);
	for (ii=1;ii<=t;ii++) {
		scanf ("%d%d",&m,&n);
		for (i=0;i<m;i++) {
			scanf ("%s",&str); s = str;
			pro(i,s);
			for (j=0;j<n;j++) visit[i][j] = false;
		}
		/*for (i=0;i<m;i++) {
			for (j=0;j<n;j++) printf ("%d",grid[i][j]);
			printf ("\n");
		}*/
		lim = min(m,n);
		for (i=1;i<=lim;i++) cut[i] = 0;
		for(in=lim;in>=0;in--)
			for (i=0;i<m-in;i++)
				for (j=0;j<n-in;j++)
					if (ok(i,j,in)) {
						//printf ("yes %d %d\n",i,j);
						cut[in+1]++;
					}
		int res = 0;
		for (i=lim;i>=0;i--) if (cut[i]>0) res++;
		printf ("Case #%d: %d\n",ii,res);
		for (i=lim;i>=0;i--)
			if (cut[i]>0)
				printf ("%d %d\n",i,cut[i]);
	}
	return 0;
}
