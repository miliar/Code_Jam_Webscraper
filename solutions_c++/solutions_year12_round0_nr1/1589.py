#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

#define F(i,a,b) for(i=a;i<=b;++i)

char c[300];

void ss()
{
	string s,t;
	int i;

	s = "ejp mysljylc kd kxveddknmc re jsicpdrysi"; t = "our language is impossible to understand";
	for(i=0;s[i];++i) c[s[i]] = t[i];

	s = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"; t = "there are twenty six factorial possibilities";
	for(i=0;s[i];++i) c[s[i]] = t[i];

	s = "de kr kd eoya kw aej tysr re ujdr lkgc jv"; t = "so it is okay if you want to just give up";
	for(i=0;s[i];++i) c[s[i]] = t[i];

	c['q'] = 'z'; c['z'] = 'q';
}

int main()
{
	//freopen("A-small-attempt1.in","r",stdin);
	//freopen("A-small-attempt1.out","w",stdout);

	int t,cs=0,i;
	char xx[1000];
	ss();

	scanf("%d",&t); gets(xx);
	while(t--){
		gets(xx);
		printf("Case #%d: ",++cs);
		for(i=0;xx[i];++i)
			printf("%c",c[xx[i]]);
		printf("\n");
	}

	return 0;
}