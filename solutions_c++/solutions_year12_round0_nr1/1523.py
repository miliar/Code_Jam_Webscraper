#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl

int T,mp[26],bl[26];
char s[10100];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	char *a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char *b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	memset(mp,-1,sizeof mp);
	memset(bl,-1,sizeof bl);
	for (int i=0;a[i];i++) if (a[i]>='a' && a[i]<='z')
	{
		mp[a[i]-'a'] = b[i]-'a';
		bl[b[i]-'a'] = 1;
	}
	
	mp['q'-'a'] = 'z' - 'a';
	mp['z'-'a'] = 'q' - 'a';
	
	
	//for (int i=0;i<26;i++) if (mp[i]==-1) printf("%c ",'a'+i); printf("\n");
	//for (int i=0;i<26;i++) if (bl[i]==-1) printf("%c ",'a'+i); printf("\n");
	
	scanf("%d",&T);
	gets(s);
	for (int test=1;test<=T;test++)
	{
		printf("Case #%d: ",test);
		gets(s);
		for (int i=0;s[i];i++)
			if (s[i]>='a' && s[i]<='z') printf("%c",'a'+mp[s[i]-'a']);
			else printf("%c",s[i]);
		printf("\n");
	}
	
	
	return 0;
}
