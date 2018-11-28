#include <stdio.h>
#include <string.h>

#define MAX 1000

int buttons[MAX][2];

inline int abs(int x) {
	return x>0 ? x : -x;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i) {
			char str[10];
			int k;
			scanf("%s%d",str,&k);
			buttons[i][0]=k-1;
			buttons[i][1]=str[0]=='O';
		}
		int ans=0;
		int posb=0, poso=0;
		for(int i=0;i<n;++i) {
			if(!buttons[i][1]) {
				int d=abs(posb-buttons[i][0]);
				ans+=d+1;
				posb=buttons[i][0];
				for(int j=i+1;j<n;++j)
					if(buttons[j][1]) {
						if(poso<buttons[j][0]) {
							poso+=d+1;
							if(poso>buttons[j][0])
								poso=buttons[j][0];
						}
						else if(poso>buttons[j][0]) {
							poso-=d+1;
							if(poso<buttons[j][0])
								poso=buttons[j][0];
						}
						break;
					}
			}
			else {
				int d=abs(poso-buttons[i][0]);
				ans+=d+1;
				poso=buttons[i][0];
				for(int j=i+1;j<n;++j)
					if(!buttons[j][1]) {
						if(posb<buttons[j][0]) {
							posb+=d+1;
							if(posb>buttons[j][0])
								posb=buttons[j][0];
						}
						else if(posb>buttons[j][0]) {
							posb-=d+1;
							if(posb<buttons[j][0])
								posb=buttons[j][0];
						}
						break;
					}
			}
		}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
