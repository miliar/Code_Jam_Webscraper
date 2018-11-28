#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cstdlib>

using namespace std;


char s[100],str[100];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	long kase=1,n,i,len,T;
	scanf("%ld",&T);
	getchar();
	while(T--)
	{
		scanf("%s",str);
		len=strlen(str);
		s[0]='0';
		for(i=1;i<=len;i++)
			s[i]=str[i-1];
		s[len+1]=0;
		printf("Case #%ld: ",kase++);
		while(next_permutation(s,s+strlen(s)))
		{
			n=atol(s);
			printf("%ld\n",n);
			break;
		}
	}
	return 0;
}