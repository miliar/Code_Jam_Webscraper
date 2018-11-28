#include<iostream>
#include<cmath>
#include<algorithm>
#include<cctype>
#include<vector>
#include<cassert>
#include<set>
#include<string>
#include<ctime>
#include<map>
using namespace std;
string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
char table [26];
bool flag [26];
int main (){
	memset(table,0,sizeof table);
	memset(flag,0,sizeof flag);
	for ( int i=0 ; i<s1.size() ; i++ ){
		if ( s1[i] == ' ' ) continue ;
		char first = s1[i] , second = s2[i] ;
		table[first-'a'] = s2[i];
	}
	table['z'-'a'] = 'q';
	table['q'-'a'] = 'z';
	

	freopen ( "A-small-attempt0.in" , "r" , stdin );
	freopen ( "A-small-attempt0.out" , "w" , stdout ) ;
	int n ;
	cin >> n ;
	cin.get();
	for ( int i=0 ; i<n ; i++ ){
		string s;
		getline ( cin , s ) ;
		cout << "Case #" << i+1 << ": ";
		for ( int j=0 ; j<s.size(); j++ )
			if ( s[j] == ' ' ) cout << " " ;
			else cout << table[s[j]-'a'];
		cout << endl;
	}
	
}