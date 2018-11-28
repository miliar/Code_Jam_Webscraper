#include<cstdio>
#include<algorithm>
using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++){
		int n,s,p,cnt=0;
		scanf("%d %d %d",&n,&s,&p);
		for(int i=0;i<n;i++){
			int x, has1=0, has2=0;
			scanf("%d",&x);
			for(int a = 0; a<=x;a++)
				for(int b = a; a+b<=x; b++){
					int c = x -a -b;
					int d = max(b,c) - min(a,c);
					if(d>2) continue;
					if(max(b,c)>=p){
						if(d<2) has1 = 1;
						else has2 = 1;
					}
				}
			if(has1)
				cnt++;
			else if(has2 && s){
				s--;
				cnt++;
			}
		}
		printf("Case #%d: %d\n",caso,cnt);
	}
	return 0;
}
