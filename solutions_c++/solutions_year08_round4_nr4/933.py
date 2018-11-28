#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
char s[1001];
int main()
{
	int t,n;
	int ans;
	scanf("%d",&t);
	for (int k=1;k<=t;++k)
	{
int p[]={0,1,2,3,4};
		scanf("%d",&n);
		scanf("%s",s);
		ans=strlen(s);
		do {
			int tmp=0;
			char old=0;
			for (int i=0;;++i) {
				if (s[i*n]=='\0') break;
				for (int j=0;j<n;++j) {
					if (s[i*n+p[j]]!=old) { old=s[i*n+p[j]]; ++tmp; }
				}
			}
			if (tmp<ans) ans=tmp;
		} while (next_permutation(p,p+n));
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}