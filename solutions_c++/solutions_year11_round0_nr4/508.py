#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
// 	freopen("d:\\D-small-attempt0.in","r",stdin);freopen("d:\\D-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("d:\\D-large.in","r",stdin);freopen("d:\\D-large.out","w",stdout);
	int cse, i, x, n, g=1;
	double cnt;
	scanf("%d",&cse);
	while(cse--){
        cnt = 0.0;
        scanf("%d",&n);
        for(i=1;i<=n;++i){
            scanf("%d",&x);
            if(x!=i)cnt+=1.0;
        }
        printf("Case #%d: %.6lf\n",g++, cnt);
    }
	//system("PAUSE");
	return 0;
}
