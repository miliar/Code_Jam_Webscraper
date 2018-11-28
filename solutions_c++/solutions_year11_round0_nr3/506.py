#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int a[2010],n;

int main() {
	//  freopen("d:\\C-small-attempt0.in","r",stdin);freopen("d:\\C-small-attempt0.out","w",stdout);
	//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("d:\\C-large.in","r",stdin);freopen("d:\\C-large.out","w",stdout);
	int cse, i,j,s,g=1,ss;
	scanf("%d",&cse);
	while(cse--){
		scanf("%d",&n);
		s=ss=0;
		int minx=100000000;
		for(i=0;i<n;++i){
			scanf("%d",&a[i]);
			if(a[i]<minx)minx=a[i];
			ss+=a[i];
			s^=a[i];
		}
		if(s!=0) {
			printf("Case #%d: NO\n",g++);
		}
		else{
			printf("Case #%d: %d\n",g++,ss-minx);
		}
	}
	return 0;
}
