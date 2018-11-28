#include <stdio.h>
#include <string.h>
#include <algorithm>

int n,ans[800],digit[30],len,s[30],d,answer;
char used[30];

void go(int now) {
	if(now >= len) {
		int sum=0,i;
		for(i=0;i<len;i++)
			sum = sum*10+s[i];
		ans[d++] = sum;
		return;
	}
	int i,c=-1;
	for(i=0;i<len;i++)
		if(used[i] == 0 && c != digit[i]) {
			used[i] = 1;
			c = digit[i];
			s[now] = digit[i];
			go(now+1);
			used[i] = 0;
		}
}

int main() {
	int t,i,j,tmp,c=0;
	
	scanf("%d",&t);
	while(t--) {
		scanf("%d",&n);
		tmp = n;
		len = 0;
		while(tmp > 0) {
			digit[len++] = tmp%10;
			tmp /= 10;
		}
		std::sort(digit,digit+len);
		memset(used,0,sizeof(used));
		
		d = 0;
		go(0);
		
		std::sort(ans,ans+d);
		for(i=0;i<d;i++)
			if(ans[i] == n)	break;
		
		if(i == d-1) {
			answer = 1;
			for(i=0;i<len && digit[i] == 0;i++,answer*=10);
			answer *= digit[i]*10;
			i++;
			for(;i<len;i++)
				answer = answer*10+digit[i];
		} else {
			answer = ans[i+1];
		}
		
		printf("Case #%d: %d\n",++c,answer);
	}
	
	return 0;
}
