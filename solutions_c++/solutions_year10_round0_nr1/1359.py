#include <stdio.h>
#include <string.h>

int n,k;
int s[50],l;

int main() {
	int t,c=0;
	
	scanf("%d",&t);
	while(t--) {
		memset(s,0,sizeof(s));
		scanf("%d%d",&n,&k);
		l=0;
		while(k > 0) {
			s[l++] = k%2;
			k /= 2;
		}
		bool flag = false;
		for(int i=0;i<n;i++)
			if(s[i] == 0) {
				flag = true;
				break;
			}		
		
		if(flag == false)	printf("Case #%d: ON\n",++c);
		else		printf("Case #%d: OFF\n",++c);
		
	}
	
	return 0;
}
