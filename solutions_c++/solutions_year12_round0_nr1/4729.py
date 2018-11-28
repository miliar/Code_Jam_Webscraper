#include <cstdio>
#include <string>
#include <map>
#include <iostream>
using namespace std;

const string str1[3]={"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

const string str2[3]={"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"};

map<char,char> trans;

int main()
{
	trans['q']='z';
	trans['z']='q';
	for(int i=0;i<3;i++)
	{
		int len=str1[i].length();
		for(int j=0;j<len;j++)
			trans[str1[i][j]]=str2[i][j];
	}
	for(char i='a';i<='z';i++)
		printf("%c %c\n",i,trans[i]);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	cin>>T;
	scanf("\n");
	for(int i=0;i<T;i++)
	{
		string str;
		getline(cin,str);
		int len=str.length();
		for(int j=0;j<len;j++)
			if (str[j]!=' ')
				str[j]=trans[str[j]];
		cout<<"Case #"<<i+1<<": "<<str<<'\n';
	}
	return 0;
}
