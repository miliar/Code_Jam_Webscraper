#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

map<char, char> M;
void init()
{
	string str1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string str2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string str3="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string out1="our language is impossible to understand";
	string out2="there are twenty six factorial possibilities";
	string out3="so it is okay if you want to just give up";

	for(int i=0;i<str1.size();++i)
		M[str1[i]]=out1[i];

	for(int i=0;i<str1.size();++i)
		M[str2[i]]=out2[i];

	for(int i=0;i<str1.size();++i)
		M[str3[i]]=out3[i];
	M['q']='z';
	M['z']='q';
}

int main()
{
	int n;
	init();
	cin>>n;
	getchar();

	for(int j=1;j<=n;++j)
	{
		char ch[128];
		cin.getline(ch, 128);

		for(int i=0;ch[i];++i)
			ch[i]=M[ch[i]];

		cout<<"Case #"<<j<<": "<<ch<<endl;
	}
	return 0;
}
