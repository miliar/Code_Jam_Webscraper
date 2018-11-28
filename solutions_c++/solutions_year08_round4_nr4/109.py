#include <cstdio>
#include <algorithm>
#include <cstdlib>

using namespace std;

char st[20000];
char s1[20000];
int a[20];
int i,j,k,s,t,n,m;
int ans,I,T;
main()
{
	scanf("%d",&T);
	while (T--){
		scanf("%d\n",&n);
		for (i=0;i<n;++i)
			a[i]=i;
		gets(st);
		ans=10000000;
		do{
			for (i=0;i<strlen(st);++i)
				s1[i]=st[a[i%n]+(i/n)*n];
			s=1;
			t=1;
			for (i=1;i<strlen(st);++i)
			{
				if (s1[i]!=s1[i-1]) ++s;
			}
			if (s<ans) ans=s;
		}while (next_permutation(a,a+n));
		printf("Case #%d: %d\n",++I,ans);
	}
	return 0;
}
