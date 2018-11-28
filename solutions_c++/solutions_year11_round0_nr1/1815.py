#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int abs(int a){return a<0?-a:a;}
int main(){
	int t, ans, nowo, nowb, n, poso, posb, i, k, time=0;
	char ch;
	scanf("%d", &t);
	while(t--){
		scanf("%d", &n);
		nowo=nowb=0;
		poso=posb=1;
		ans=0;
		for(i=0; i<n; i++){
			scanf(" %c %d", &ch, &k);
			if(ch=='O'){
				if(ans-nowo<abs(poso-k)+1)
					ans=nowo+abs(poso-k)+1;
				else
					ans++;
				nowo=ans;
				poso=k;
			}
			else if(ch=='B'){
				if(ans-nowb<abs(posb-k)+1)
					ans=nowb+abs(posb-k)+1;
				else
					ans++;
				nowb=ans;
				posb=k;
			}
			//printf("now ans=%d\n", ans);
			//printf("poso=%d, nowo=%d, posb=%d, nowb=%d\n", poso, nowo, posb, nowb);
		}
		printf("Case #%d: %d\n", ++time, ans);
	}
    return 0;
}
