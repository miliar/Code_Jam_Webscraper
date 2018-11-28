#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
#include<utility>

#define mm(a,b) memset(a,b,sizeof(a))
#define rep(i,a,b) for(i=a;i<b;++i)
#define repr(i,a,b) for(i=a;i>b;--i)
#define maxn 256

using namespace std;

char t[256];

void init(void)
{
	string a,b;
	a="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	b="our language is impossible to understand";
	int i;
	for(i=0;i<a.size();++i)
		t[a[i]]=b[i];
	a="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	b="there are twenty six factorial possibilities";
	for(i=0;i<a.size();++i)
		t[a[i]]=b[i];
	a="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	b="so it is okay if you want to just give up";
	for(i=0;i<a.size();++i)
		t[a[i]]=b[i];
	t['q']='z';
	t['z']='q';
}

int main(void)
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small.out","w",stdout);
	init();
	int i,T,j;
	string str;
	for(scanf("%d\n",&T),i=1;i<=T;++i)
	{
		printf("Case #%d: ",i);
		getline(cin,str);
		for(j=0;j<str.length();++j)
		 {
		     if((t[str[j]]>='a'&&t[str[j]]<='z')||(t[str[j]]==' '))
		     putchar(t[str[j]]);
		 }
		cout<<endl;
	}
	return 0;
}
