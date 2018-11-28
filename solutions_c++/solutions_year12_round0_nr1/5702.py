#include <string>
#include <cstdio>
#include <iostream>

using namespace std;

int code[365];

int main (){
    string s1 = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
    string s2 = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
    code['z'-'a'] = 'q'-'a';
    code['q'-'a'] = 'z'-'a';
    for ( int i = 0; i < s1.size(); ++i )
        code[s1[i]-'a'] = s2[i]-'a';
    int t;
    scanf ( "%d" , &t );
    char ch;
    cin.get(ch);
    int i = 1;
    printf ( "Case #%d: " , i ) ;
    while ( i <= t) {
        cin.get(ch);
        if ( ch< 'a' || ch> 'z' ) cout<<ch;
        else cout << char ( code [ch-'a'] + 'a');
        if ( ch == '\n' ) {
            i++;
           if ( i <= t ) printf ( "Case #%d: " , i ) ;
        }
    }
    return 0;
}
