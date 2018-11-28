#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<cstdio>
#include<string>
using namespace std;
int mp[30];
int main(){
freopen("A-small-attempt0.in", "r", stdin);
freopen("A.out", "w", stdout);
	memset(mp, -1, sizeof mp);
	string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	for(int i = 0; i < s1.length(); i++)
		if(s1[i] != ' ')
			mp[s1[i] - 'a'] = s2[i] - 'a';
	mp['z' - 'a'] = 'q' - 'a';
	int mark[30] = {0};
	mp[16] = 'z' - 'a';
	int t;
	cin >> t;
	getline(cin, s1);
	for(int i = 0; i < t; i++){
		getline(cin, s1);
		cout << "Case #" << i + 1 << ": ";
		for(int j = 0; j < s1.length(); j++)
			if(s1[j] != ' ')
				s1[j] = mp[s1[j] - 'a'] + 'a';
		cout << s1 << endl;
	}

	return 0;
}


