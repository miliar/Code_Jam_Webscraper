#include <string.h>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
#define mr 3200000
#define INF 1000000100

string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
string a1 = "our language is impossible to understand";

string s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string a2 = "there are twenty six factorial possibilities";

string s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
string a3 = "so it is okay if you want to just give up";

map<char, char> mp;
map<char, char>::iterator it;

int main()
{
	freopen("C:\\Users\\weilong.li.QUNARSERVERS\\Desktop\\A-small-attempt7.in", "r", stdin);
	freopen("C:\\Users\\weilong.li.QUNARSERVERS\\Desktop\\out.txt", "w", stdout);
//	setbuf(stdout, NULL);
	int i,j;
	for(i=0;i<s1.size();i++)
	{
	    if(mp.find(s1[i]) == mp.end()) {
	    	mp[s1[i]] = a1[i];
	    }else {
	    	if(mp[s1[i]] != a1[i]) cout << "??????" << endl;
	    }
	}
	for(i=0;i<s2.size();i++)
	{
	    if(mp.find(s2[i]) == mp.end()) {
	    	mp[s2[i]] = a2[i];
	    }else {
	    	if(mp[s2[i]] != a2[i]) cout << "??????" << endl;
	    }
	}
	for(i=0;i<s3.size();i++)
	{
	    if(mp.find(s3[i]) == mp.end()) {
	    	mp[s3[i]] = a3[i];
	    }else {
	    	if(mp[s3[i]] != a3[i]) cout << "??????" << endl;
	    }
	}
	if(mp.find('q') == mp.end()) mp['q'] = 'z';
	else cout << "???" << endl;
//	int tmp[26] = {0};
//	for(it=mp.begin();it!=mp.end();it++) {
//		if(it->second>='a' && it->second<='z') {
//			tmp[it->second - 'a'] = 1;
//		}
//	}
//	for(i=0;i<26;i++) if(!tmp[i]) {
//		mp['z'] = 'a'+i;
//	}
	mp['z'] = 'q';
//	cout << mp.size() << endl;
//	for(it=mp.begin();it!=mp.end();it++) {
//		cout << it->first << "=>" << it->second << endl;
//	}
	int n;
	int cs = 1;
	char op[5];
	string str = "";
	cin >> n;
	gets(op);
	while(n--)
	{
		printf("Case #%d: ",cs++);
		getline(cin, str);
		for(i=0;i<str.size();i++)
		{
			putchar(mp[str[i]]);
		}
		puts("");
	}
	return 0;
}
