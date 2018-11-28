#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
	freopen("C:\\Documents and Settings\\liyingxin\\×ÀÃæ\\A-small-attempt1.in","r",stdin);
	freopen("C:\\Documents and Settings\\liyingxin\\×ÀÃæ\\output.txt","w",stdout);
	
	string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string b = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string c = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string aa = "our language is impossible to understand";
	string bb = "there are twenty six factorial possibilities";
	string cc = "so it is okay if you want to just give up";
	char dict[30] = "";
	for(int i = 0;i < a.size();i++)
	{
		if(a[i] == ' ') continue;
		dict[a[i]-'a'] = aa[i];
	}
	for(int i = 0;i < b.size();i++)
	{
		if(b[i] == ' ') continue;
		dict[b[i]-'a'] = bb[i];
	}
	for(int i = 0;i < c.size();i++)
	{
		if(c[i] == ' ') continue;
		dict[c[i]-'a'] = cc[i];
	}
	dict['q'-'a'] = 'z';
	dict['z'-'a'] = 'q';
	//sort(dict,dict+30);
	//for(int i = 0;i <30;i++) cout<<i<<"  "<<dict[i]<<endl;
	
	int cas;
	scanf("%d",&cas);
	char aaa[5];
	gets(aaa);
	for(int t = 1;t <= cas; t++)
	{
		string tmp;
		getline(cin, tmp);
		string ans = string(tmp.size(),' ');
		for(int i = 0;i <tmp.size();i++)
		{
			if(tmp[i] == ' ')
			{
				ans[i] = ' ';
				continue;
			}
			ans[i] = dict[tmp[i]-'a'];
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}
