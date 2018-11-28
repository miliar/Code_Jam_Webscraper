#include <stdio.h>
#include <string.h>

char a[100][100];
char b[100][100];

int main(void)
{
	int T,cs=0,n,i,j,k,l;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%s",a[i]);
			strcpy(b[i],a[i]);
		}
		int cnt=0,flag=0;
		for(i=0;i<n;i++){
			for(j=i;j<n;j++){
				for(k=i+1;k<n;k++)
					if(a[j][k]=='1')
						break;
				if(k==n){
					for(l=j;l>i;l--){
						static char tmp[100];
						strcpy(tmp, a[l]);
						strcpy(a[l], a[l-1]);
						strcpy(a[l-1], tmp);
						++cnt;
					}
					break;
				}
			}
			if(j==n) flag=1;
		}
		/*int cnt2=0, flag2=0;
		for(i=n-1;i>=0;i--){
			for(j=i;j>=0;j--){
				for(k=0;k<i;k++)
					if(b[j][k]=='1')
						break;
				if(k==i){
					for(l=j;l<i;l++){
						static char tmp2[100];
						strcpy(tmp2, b[l]);
						strcpy(b[l], b[l+1]);
						strcpy(b[l+1], tmp2);
						++cnt2;
					}
					break;
				}
			}
			if(j<0) {flag2=1;break;}
		}*/
		int ans=cnt;
		/*if(flag) ans = cnt2;
		else if(flag2) ans = cnt;
		else if(cnt < cnt2)
			ans = cnt;
		else
			ans = cnt2;*/
		printf("Case #%d: %d\n",++cs, ans);
	}
	return 0;
}
