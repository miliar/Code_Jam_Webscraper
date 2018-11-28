/*
 * A.cpp
 *
 *  Created on: 13-Apr-2012
 *      Author: ram
 */



#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <stdlib.h>
#include <bitset>
using namespace std;

#define f(i,a,b) for( i = ( a ); i < ( b ); ++ i )
#define fo(i,b) f( i, 0, ( b ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define m memset
int main(){
	int T,i;
	cin >> T;
	int a[26];
	m(a,-1,26*4);


		string s = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
		s += "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
		s += "de kr kd eoya kw aej tysr re ujdr lkgc jv";

		string t = "our language is impossible to understand";
		t += "there are twenty six factorial possibilities";
		t += "so it is okay if you want to just give up";
		unsigned int j;
		fo(j,s.length()){

			if (s[j] <= 'z' && s[j]>='a')
					if(a[s[j]-'a']==-1){
						a[s[j]-'a']=t[j]-'a';

					}

		}
	a['z'-'a'] = 'q'-'a';
	bitset<26> b;
	b.reset();
	fo(i,26){
		if (a[i]!=-1)
		b.set(a[i],true);
	}
	int itemp;
	fo (i,26){

		if(b.test(i)==false)
			itemp = i;
	}
	fo(i,26){
		if (a[i]==-1) a[i]=itemp;
		//putchar(a[i]+'a'); cout << endl;
	}

	string temp;
	cin >> temp;	
	bool flag = true;

	fo(i,T){
		string s = "";
	
		cout << "Case #" << i+1 << ": ";
		getline(cin,s);
		if (flag) {s = temp+s;
			flag = false;
		}
	
		fo(j,s.length()){
			if (s[j] <= 'z' && s[j]>='a')
				putchar(a[s[j]-'a']+'a');
			else
				putchar(s[j]);
		}
		cout << endl;

	}

}

