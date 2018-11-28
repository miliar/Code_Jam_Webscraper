#include <cstdio>
#include <queue>
using namespace std;

int main(){
	int a[150][150];
	int b[150][150];
	int c[150][150];
	char r[150][150];
	int x[5],y[5];
	char mp[300];
	x[0]=y[0]=0;
	x[1]=-1;y[1]=0;
	x[2]=0;y[2]=-1;
	x[3]=0;y[3]=1;
	x[4]=1;y[4]=0;
	int i,j,k,h,w,t,T;
	scanf("%d", &T);
	for (t=1; t<=T; t++) {
		scanf("%d %d",&h, &w);
		for (i=0; i<h+2; i++)
			for (j=0; j<w+2; j++)
				a[i][j]=22222;
		for (i=1; i<=h; i++)
			for (j=1; j<=w; j++) {
				scanf("%d", &a[i][j]);
				c[i][j]=0;
			}

		for (i=1; i<=h; i++)
			for (j=1; j<=w; j++) {
				b[i][j]=0;
				for (k=1; k<5; k++) {
					if (a[i+x[k]][j+y[k]]<a[i+x[b[i][j]]][j+y[b[i][j]]])
						b[i][j]=k;
				}
				k=b[i][j];
				if (k!=0) {
					c[i+x[k]][j+y[k]] |= (1<<k);
				}
			}

		queue<pair<pair<int,int>, char> > q;
		char ch='A';
		for (i=1; i<=h; i++)
			for (j=1; j<=w; j++) {
				if (b[i][j]==0) {
					q.push(make_pair(make_pair(i,j),ch));
					r[i][j]=ch;
					ch++;
				}
			}

		while (!q.empty()) {
			pair<pair<int,int>,char> p=q.front();
			int X, Y;
			char C;
			X=p.first.first;
			Y=p.first.second;
			C=p.second;
			r[X][Y]=C;
			//printf("---- (%d,%d) - %c\n",X,Y,C);
			q.pop();
			for (k=1; k<5; k++) {
				if (c[X][Y] & (1<<k)) {
					q.push(make_pair(make_pair(X-x[k],Y-y[k]), C));
				}
			}
		}

		printf("Case #%d:\n", t);
		for (k=0; k<200; k++)
			mp[k]=k;
		ch='a';
		for (i=1; i<=h; i++) {
			for (j=1; j<=w; j++) {
				if (mp[r[i][j]]>='A' && mp[r[i][j]]<='Z') {
					mp[r[i][j]]=ch;
					r[i][j]=ch;
					printf("%c ", ch);
					ch++;
				} else {
					r[i][j]=mp[r[i][j]];
					printf("%c ",r[i][j]);
				}
			}
			printf("\n");
		}
	}
	return 0;
}
