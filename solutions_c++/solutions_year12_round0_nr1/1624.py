#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

string t[3] = { "ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv" };
string a[3] = { "our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up" };

int map[300];
char buff[500];

int cnt[500];

int main( void ){
 //freopen( "out.txt", "w", stdout );
 for( int i = 0; i < 3; ++i ) {
    for( int j = 0; j < t[i].size(); ++j )
        map[t[i][j]] = a[i][j];
 }

 map['q'] = 'z';
 map['z'] = 'q';

 int n;
 cin >> n;
 getchar();

 for( int i = 0; i < n; ++i ){
    char c = 5;
    int cnt = 0;
    while( ( c = getchar() ) != '\n' ) buff[cnt++] = c;
    buff[cnt] = 0;
    string x = buff;
    for( int j = 0; j < x.size(); ++j ) x[j] = map[x[j]];
    printf( "Case #%d: %s\n", i+1, x.c_str() );
 }



 return 0;
}
