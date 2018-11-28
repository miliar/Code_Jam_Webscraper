#include<stdio.h>
#include<string.h>

char s[700];
int d[500];
bool flag[500];
int main()
{
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-small-attempt1.out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int kk=1; kk<=t; kk++){
		scanf("%s", s);
		memset(d, -1, sizeof(d));
		memset(flag, 0, sizeof(flag));
		int len=strlen(s), sum=0;
		for(int i=0; i<len; i++){
			if(!flag[s[i]]){
				flag[s[i]]=true;
				sum++;
			}
		}
		d[s[0]]=1;
		int aa=0;
		for(int i=1; i<len; i++){
			if(d[s[i]]<0){
				if(aa==1) aa++;
				d[s[i]]=aa++;
			}
		}
		long long ans=0;
		printf("Case #%d: ", kk);
		if(sum==1){
			sum=2;
		}
		for(int i=0; i<len; i++){
			ans=ans*sum+d[s[i]];
		}
		printf("%lld\n", ans);
	}
	return 0;
}