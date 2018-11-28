#include <stdio.h>

char a[5005][25];
char s[100005];

int main(void)
{
	int L,D,N;
	int i, j, k, cnt, flag;
	scanf("%d%d%d",&L,&D,&N);
	for(i=0;i<D;i++){
		scanf("%s",a[i]);
	}
	for(int cs=1;cs<=N;cs++){
		scanf("%s",s);
		cnt=0;
		for(i=0;i<D;i++){
		k=0;
		for(j=0;s[j];j++, k++){
			flag=0;
			if(s[j]=='('){
				while(s[++j]!=')')
					if(s[j]==a[i][k])
						flag=1;
			}else if(s[j]==a[i][k])
				flag=1;
			if(!flag)
				break;
		}
		if(k==L)
			++cnt;
		}
		printf("Case #%d: %d\n",cs,cnt);
	}
	return 0;
}
