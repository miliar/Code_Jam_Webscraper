#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int a,b,d,n,t,tt=1,x,y;
	char c;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		a=b=1;x=y=0;
		while(n--){
			scanf(" %c%d",&c,&d);
			if(c=='O'){
				x+=abs(a-d)+1;
				if(x<y+1)x=y+1;
				a=d;
			}
			if(c=='B'){
				y+=abs(b-d)+1;
				if(y<x+1)y=x+1;
				b=d;
			}
		}
		printf("Case #%d: %d\n",tt++,max(x,y));
	}
	return 0;
}