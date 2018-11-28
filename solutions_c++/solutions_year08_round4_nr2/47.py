#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

struct Tpoint{
	int x,y;
}p1,p2;
int a,n,m;
bool flag;

void init(){
	scanf("%d%d%d",&n,&m,&a);
}

int abs(int x){
	if (x<0) return -x;
	return x;
}

void solve(){
	flag=false;
	for (p1.x=0;p1.x<=n;p1.x++)
	for (p1.y=0;p1.y<=m;p1.y++)
	for (p2.x=0;p2.x<=n;p2.x++)
	for (p2.y=0;p2.y<=m;p2.y++){
		if (abs(p1.x*p2.y-p1.y*p2.x)==a) flag=true;
		if (flag) return;
	}
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T,num=0;
	scanf("%d",&T);
	while (T--){
		num++;
		init();
		solve();
		if (flag) printf("Case #%d: %d %d %d %d %d %d\n",num,0,0,p1.x,p1.y,p2.x,p2.y);
		else
			printf("Case #%d: IMPOSSIBLE\n",num);
	}

	return 0;
}