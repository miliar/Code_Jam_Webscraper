#include <iostream>
#include <cstring>

using namespace std;

string in[3] = { "ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv" };
string out[3] ={ "our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up" };

string a;
char mp[256];

void scan(){
    getline ( cin, a);
}

string translate ( string t ){
    for ( int i = 0; i < t.size(); ++i )
        t[i] = mp[ t[i] ];
    return t;
}
void solve ( int test ){
    cout << "Case #" << test <<": " << translate ( a ) << "\n";
}

void init(){
    memset ( mp, -1, sizeof ( mp ) );

    for ( int i = 0; i < 3; ++i )
        for ( int j = 0; j < in[i].size(); ++j )
            mp[ in[i][j]  ] = out[i][j];

    mp['q'] = 'z';
    mp['y'] = 'a';
    mp['z'] = 'q';
   // for ( int i = 0; i < 256; ++i )
     //   if ( mp[i] != -1 )
       //     cout << (char)i << " " << (char)mp[i] << endl;
}

int main(){
    init();

    int tests;
    cin >> tests;
    getline ( cin, a );
    for ( int i = 0; i < tests; ++i ){
        scan();
        solve(i + 1);
    }
}
