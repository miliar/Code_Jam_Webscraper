#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int d[11111],l[11111];
int f[11111];


int main(){
	//freopen("test.in","r",stdin);
	//freopen("test.out","w",stdout);
	int T,n,m,now,h,ps,yes,maxlen,maxnow,maxh,len;
	cin >> T;
	for(int Case = 1; Case <= T ;Case ++){
		cin >> n;
		for(int i = 1 ; i <= n; i ++){
			scanf("%d %d",&d[i],&l[i]);
		}
		scanf("%d",&m);
		memset(f,0,sizeof(f));
		f[1] = min(l[1],d[1]);
		yes = 0;
		for(int i = 1; i <= n; i ++){
			if(f[i] == 0)break;
			if(f[i] + d[i] >= m){
				yes = 1;
				break;
			}
			ps = i + 1;
			while(ps <= n && d[i] + f[i] >= d[ps]){
				len = min(d[ps]-d[i],l[ps]);
				if(len > f[ps])
					f[ps] = len;
				ps ++;
			}
		}
		
		
		printf("Case #%d: ",Case);
		if(yes)
			printf("YES\n");
		else
			printf("NO\n");
	}

	return 0;
}
