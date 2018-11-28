#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,t,n;
	char s[22];
	scanf("%d",&t);
	gets(s);
	for (i=1;i<=t;i++){
		gets(s+1);
		n=strlen(s+1);
		if (next_permutation(s+1,s+n+1))
			printf("Case #%d: %s\n",i,s+1);
		else{
			prev_permutation(s+1,s+n+1);
			s[0]='0';
			next_permutation(s,s+n+1);
			printf("Case #%d: %s\n",i,s);
		}
	}
}
