#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

char ch[22];
char pre[22];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca;
	scanf("%d",&T);
	int i,j,k,t;
	for(ca=1;ca<=T;ca++)
	{
		printf("Case #%d: ",ca);
		scanf("%s",ch);
		k=strlen(ch);
		for(i=1;i<k;i++) if(ch[i]>ch[i-1]) break;
		if(i==k)
		{
			for(j=k-1;j>=0;j--) if(ch[j]!='0') break;
			printf("%c",ch[j]);
			for(i=k;i>j;i--) printf("0");
			for(j--;j>=0;j--) printf("%c",ch[j]);
			puts("");
			continue;
		}
		memset(pre,0,sizeof(pre));
		strcpy(pre,ch);
		while(next_permutation(pre,pre+k))
		{
			if(strcmp(pre,ch)!=0) break;
		}
		printf("%s\n",pre);

	}
	return 0;
}