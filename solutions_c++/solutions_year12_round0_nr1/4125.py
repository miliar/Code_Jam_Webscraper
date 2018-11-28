#include<iostream>
using namespace std;
const string s1="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
const string s2="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
int times,use[1000],use2[1000];
string s;
int main()
{
	memset(use,-1,sizeof(use));
	memset(use2,-1,sizeof(use2));
	for (int a=0;a<s1.size();++a)
	if (s1[a]!=' ')
	{
		use[s1[a]-'a']=s2[a]-'a';
		use2[s2[a]-'a']=s1[a]-'a';
	}
//	for (int a=0;a<26;++a) if (use[a]==-1) printf("[%d]",a);
	use[16]=25;
	use[25]=16;
//	for (int a=0;a<26;++a) if (use2[a]==-1)printf("<%d>",a);
//	system("pause");
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	cin>>times;
	getchar();
	int z=0;
	while (times--)
	{
		++z;
		getline(cin,s);
		for (int a=0;a<s.size();++a)
		if (s[a]!=' ')
		{
			s[a]=use[s[a]-'a']+'a';
		}
		cout<<"Case #"<<z<<": "<<s<<endl;
	}
}
