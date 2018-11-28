//BISMILLAHIRRAHMANIRRAHIM


#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <vector>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <string>
using namespace std;
#define pii pair < int , int >


struct gr{
	bool g[600][600];
}c,n;




int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	int T,I,i,j,k,l,r,x1,x2,y1,y2,y,x;
	cin>>T;
	for(I=1;I<=T;I++) {
		fprintf(stderr,"%d\n",I);
		cin>>r;
		memset(&c,0,sizeof(c));
		l=0;
		queue < pii > q1;
		while(r--) {
			cin>>x1>>y1>>x2>>y2;
			y=y1;
			for(x=x1;x<=x2;x++) for(y=y1;y<=y2;y++) if(!c.g[x][y]){
				c.g[x][y]=1;
				q1.push(pii(x,y));
			}
		}
		k=0;
		//cout<<l<<'\n';
		while(!q1.empty()) {
			k++;
			memset(&n,0,sizeof(n));
			queue < pii > qt;
			l=0;
			while(!q1.empty()) {
				x=q1.front().first;
				y=q1.front().second;
				q1.pop();
				if(c.g[x-1][y] || c.g[x][y-1]) {
					n.g[x][y]=1;
					qt.push(pii(x,y));
					if(!c.g[x+1][y] && !n.g[x+1][y] && c.g[x+1][y-1]) {
						qt.push(pii(x+1,y));
						n.g[x+1][y]=1;
						//cout<<(x+1)<<' '<<y<<'\n';
					}
					if(!c.g[x][y+1] && !n.g[x][y+1] && c.g[x-1][y+1]) {
						qt.push(pii(x,y+1));
						n.g[x][y+1]=1;
						//cout<<x<<' '<<(y+1)<<'\n';
					}
				}
			}
			c=n;
			q1=qt;
			//cout<<l<<'\n';
		}
		printf("Case #%d: %d\n",I,k);
	}
	return 0;
}
