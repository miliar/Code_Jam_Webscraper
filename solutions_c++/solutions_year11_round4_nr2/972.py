#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>

#define maxn 111

using namespace std;

int test,n,m,d,res;
int a[maxn][maxn];
struct point {
	double x,y;
};
point p[maxn][maxn];

int search(char key){
	int i;
	char ch='0';
	for (i=0;i<=9;i++)
		if (ch==key) return i; else ch++;
}

void input(){
	int i,j,v;
	string s;
	scanf("%d%d%d\n",&m,&n,&d);
	for (j=1;j<=m;j++){
		getline(cin,s);
		for (i=0;i<s.length();i++){
			v=search(s[i]);
			a[i+1][j]=d+v;
		}
	}
}

void process(){
	int i,j,u,v,t;
	double x,y,xx,yy;
	bool ok;
	p[1][1].x=0;
	p[1][1].y=0;
	for (i=2;i<=n;i++){
		p[i][1].x=p[i-1][1].x+1;
		p[i][1].y=p[i-1][1].y;
	}
	for (j=2;j<=m;j++)
		for (i=1;i<=n;i++){
			p[i][j].x=p[i][j-1].x;
			p[i][j].y=p[i][j-1].y+1;
		}
	res=0;
	for (t=3;t<=min(n,m);t++){
		ok=false;
		for (i=1;i<=n;i++){
			for (j=1;j<=m;j++){
				if (i+t-1>n) continue;
				if (j+t-1>m) continue;
				x=(p[i][j].x+p[i+t-1][j+t-1].x)/2;
				y=(p[i][j].y+p[i+t-1][j+t-1].y)/2;
				xx=0;
				yy=0;
				for (u=i;u<=i+t-1;u++)
					for (v=j;v<=j+t-1;v++){
						if ((u==i)&&(v==j)) continue;
						if ((u==i+t-1)&&(v==j)) continue;
						if ((u==i)&&(v==j+t-1)) continue;
						if ((u==i+t-1)&&(v==j+t-1)) continue;
						xx=xx+(p[u][v].x-x)*(double)(a[u][v]);
						yy=yy+(p[u][v].y-y)*(double)(a[u][v]);
					}
				if ((xx==0)&&(yy==0)){
					ok=true;
					break;
				}
			}
			if (ok) break;
		}
		if (ok) res=t;
	}
}

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d\n",&test);
	int i;
	for (i=1;i<=test;i++){
		input();
		process();
		if (res==0) cout<<"Case #"<<i<<": IMPOSSIBLE\n"; else
			cout<<"Case #"<<i<<": "<<res<<"\n";
	}
}
