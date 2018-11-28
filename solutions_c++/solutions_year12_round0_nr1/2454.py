#include <iostream>
#include <map>
#include <string>

using namespace std;

char g[]="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
char s1[]="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";

map<char,char> dict;
string in;
int T;

void main()
{
	int len = sizeof(g)/sizeof(g[0]);
	for(int i=0;i<len;i++)
	{
		if(g[i])
			dict.insert(pair<char,char>(s1[i],g[i]));
	}
	dict.insert(pair<char,char>('q','z'));
	dict.insert(pair<char,char>('z','q'));

	//for(map<char,char>::iterator it = dict.begin();it!=dict.end();++it)
	//	cout << (*it).first << " => " << (*it).second << endl;

	freopen("A-small-attempt0.in","r",stdin);
	freopen("A.out","w",stdout);

	scanf("%d",&T);
	getline(cin,in);
	int c=1;
	while(T--)
	{
		getline(cin, in);
		for(int i=0;i<in.length();i++)
		{
			char tmp = dict.find(in[i])->second;
			in[i] = tmp;
		}

		cout << "Case #" << c++ <<": " << in << endl;
	}
}