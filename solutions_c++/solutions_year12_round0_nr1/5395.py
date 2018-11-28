#include<iostream>
#include<cstdio>

using namespace std;

char source[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char dest[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char map[256];
char s[2000];

int main()
{
	freopen( "A-small-attempt1.in", "r", stdin );
	freopen( "out.txt", "w", stdout ); 
	int l = strlen(source);
	for (int i = 0; i < l; i++ ) map[source[i]] = dest[i];
	for (char i = 'a'; i <= 'z'; i++ ) {
		bool ok = false;
		for (char j = 'a'; j <= 'z'; j++ )
			if ( map[j] == i )
				ok = true;
			if (!ok ) cout << i << " unmapped\n";
		}
	map['q'] = 'z'; map['z'] = 'q';
	int casen = 0;
	fgets(s, 2000, stdin ); 
	while (fgets(s, 2000, stdin)) {
		l = strlen(s);
		for (int i = 0; i < l; i++ ) 
			if (s[i] >= 'a' && s[i] <= 'z' )
				s[i] = map[s[i]];
		printf( "Case #%d: %s", ++casen, s ); 
	}
}
 