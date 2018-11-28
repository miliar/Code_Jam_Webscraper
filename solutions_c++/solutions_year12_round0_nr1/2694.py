#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(void)
{
    int N;
    cin >> N;
    cin.ignore();

    string from[3];
    string to[3];
    from[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    to[0]   = "our language is impossible to understand";
    from[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    to[1]   = "there are twenty six factorial possibilities";
    from[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    to[2]   = "so it is okay if you want to just give up";
    
    map<char, char> trans;
    for(int s = 0; s < 3; ++s){
        for(int i = 0; i < from[s].size(); ++i){
            if (from[s][i] == ' '){
                continue;
            }

            if ( trans.find( from[s][i] ) != trans.end() ) {
                if (trans[ from[s][i] ] != to[s][i]){
                    cout << "error! " << endl;
                    exit(1);
                }
            }
            else{
                trans[ from[s][i] ] = to[s][i];
            }
        }
    }
    trans[ ' ' ] = ' ';
    trans[ 'q' ] = 'z';
    trans[ 'z' ] = 'q';

    for(int n = 0; n < N; ++n){
        string inStr;
        getline(cin, inStr);

        string ret = "";
        for(int i = 0; i < inStr.size(); ++i){
            ret += trans[ inStr[i] ];
        }

        cout << "Case #" << (n+1) << ": " << ret << endl;
    }

    return 0;
}
