#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <sstream>
#include <limits>
using namespace std;

int main()
{
		string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
		string s2 = "our language is impossible to understand";
		string s3 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
		string s4 = "there are twenty six factorial possibilities";
		string s5 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
		string s6 = "so it is okay if you want to just give up";
		vector<char> v(26);
		for (int i = 0; i < s1.size(); i++) v[s1[i]-'a']=s2[i];
		for (int i = 0; i < s3.size(); i++) v[s3[i]-'a']=s4[i];
		for (int i = 0; i < s5.size(); i++) v[s5[i]-'a']=s6[i];
		for (int i = 0; i < 26; i++){
			if('a'+i == 'q')v[i]='z';
			if('a'+i=='z')v[i]='q';
		}
		int t; cin>>t;
		cin.get();
		for (int i = 1; i <= t; i++){
			string ss;
			getline(cin,ss);
			for (int j = 0; j < ss.size(); j++) 
				if(isalpha(ss[j]))ss[j]=v[ss[j]-'a'];
			cout<<"Case #" <<i<<": "<<ss<<endl;
		}	
}


