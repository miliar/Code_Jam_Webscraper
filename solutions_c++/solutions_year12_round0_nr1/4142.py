#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <algorithm>

using namespace std;

int main( )
{
	char mapping[26];
	int len;
	
	for(int i=0;i<26;i++){
		mapping[i] = ' ';
	}
	
	mapping['y'-'a'] = 'a';
	mapping['e'-'a'] = 'o';
	mapping['q'-'a'] = 'z';
	mapping['z'-'a'] = 'q';
	
	string src = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string res = "our language is impossible to understand";
	
	len = src.length( );
	
	for(int i=0;i<len;i++){
		mapping[src[i]-'a'] = res[i];
	}
	
	src = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	res = "there are twenty six factorial possibilities";
	
	len = src.length( );
	
	for(int i=0;i<len;i++){
		mapping[src[i]-'a'] = res[i];
	}
	
	src = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	res = "so it is okay if you want to just give up";
	
	len = src.length( );
	
	for(int i=0;i<len;i++){
		mapping[src[i]-'a'] = res[i];
	}
	
	int t;
	
	scanf("%d",&t);
	
	getchar( );
	
	for(int cnt=1;cnt<=t;cnt++){
		getline(cin,src);
		len = src.length( );
		for(int i=0;i<len;i++){
			if(src[i]==' ')
				continue;
			else
				src[i] = mapping[src[i]-'a'];
		}
		
		cout<<"Case #"<<cnt<<": "<<src<<endl;
	}
			
	return 0;
}

