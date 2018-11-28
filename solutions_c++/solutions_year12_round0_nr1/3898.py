#include<iostream>
#include<string>
#include<map>
using namespace std;

map<char,char> trans;

void Train()
{
	string x[3] = {
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"
	};
	string y[3] = {
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up"
	};

	for(int i=0;i<3;++i)
	{
		for(int j=0;j<x[i].length();++j)
		{
			trans[x[i][j]]=y[i][j];
		}
	}
	trans['q']='z';
	trans['z']='q';
}

void Parse()
{
	freopen("A-small-attempt3.in", "r", stdin);
	freopen("A-small_out.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for(int i=1;i<=t;++i)
	{
		string str;
		getline(cin, str);
		for(int j=0;j<str.length();++j)
		{
			str[j]=trans[str[j]];
		}
		printf("Case #%d: %s\n", i, str.c_str());
	}
}

int main()
{
	Train();
	Parse();
	return 0;
}
