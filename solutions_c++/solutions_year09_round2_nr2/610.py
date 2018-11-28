#include <cstdio>
#include <algorithm>
int main()
{
	char n[64];
	int t,l;
	scanf("%d",&t);
	for(int i=1;i<=t;++i)
	{
		scanf("%s",&n[2]);
		n[0]='0';
		n[1]='0';
		l=strlen(n);
		std::next_permutation(n,n+l);
		int pos=0;
		while(n[pos]=='0')++pos;
		printf("Case #%d: %s\n",i,&n[pos]);
	}
	return 0;
}

