/*
ID: mkagenius1
LANG: C++
TASK:
*/

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<string.h>
#include<string>
#include<vector>
#include<math.h>
#include<set>
#include<queue>

using namespace std;

/* Main Code goes Here-after */
int main()
{
    string source[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    string target[] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};
    map<char, char> mapper;
    mapper['z'] = 'q'; mapper['a'] = 'y'; mapper['o'] = 'e'; mapper['q'] = 'z';

    for(int i = 0 ;  i < 3; i++){
        for(int j = 0; j < source[i].size(); j++){
            mapper[source[i][j]] = target[i][j];
        }
    }
    int Testcases; cin >> Testcases;
    scanf("%*c");
    int kase = 0;
    while(Testcases--){
        string s; getline(cin, s);
        kase ++;
        cout << "Case #"<< kase << ": " ;
        for(int i = 0; i < s.size(); i++) cout << mapper[s[i]];
        cout << endl;
    }
    //cin >> source[0];
    return 0;
}
    
