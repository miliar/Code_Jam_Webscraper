#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <map>

//#define DEBUG

using namespace std;

char src[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
"de kr kd eoya kw aej tysr re ujdr lkgc jv";

char dst[] = "our language is impossible to understand"
"there are twenty six factorial possibilities"
"so it is okay if you want to just give up";

char table[26];

void getTable(){
	char *ps = src, *pd = dst;
	while(*ps != 0){
		table[*ps++ - 'a'] = *pd++;
	}
	table['q'-'a'] = 'z';
	table['z'-'a'] = 'q';
#ifdef DEBUG
	for (int i=0; i<26; i++){
		cout<<table[i]<<' ';
	}
	cout<<endl;
#endif
}

int main(){
	getTable();

	freopen("A-small-attempt1.in", "r", stdin);
	freopen("Aout.txt", "w", stdout);

	char s[200];
	int t, tcase;
	cin>>t;
	cin.ignore();
	for (tcase=1; tcase<=t; tcase++){
		cin.getline(s,200);
		char *p = s;
		while(*p != 0){
			*p = table[*p-'a'];
			++p;
		}
		cout<<"Case #"<<tcase<<": "<<s<<endl;
	}

	return 0;
}