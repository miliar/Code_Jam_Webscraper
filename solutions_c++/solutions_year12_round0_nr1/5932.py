#include <map>
#include <iostream>
#include <string>

using namespace std;

int main (){
    int n;
    map<char, char> mp;
    string resp[6], str;
    resp[0] = "our language is impossible to understand";
    resp[1] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    resp[2] = "there are twenty six factorial possibilities";
    resp[3] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    resp[4] = "so it is okay if you want to just give up";
    resp[5] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    for ( int i = 0; i < 6; i += 2 ){
        for ( int j = 0; j < resp[i].size(); ++j ){
            mp.insert( make_pair( resp[i+1][j], resp[i][j]));
            //mp[resp[i+1][j]] = resp[i][j];
        }
    }
    mp['q'] = 'z';
    mp['z'] = 'q';
    cin >> n;
    cin.ignore();
    for ( int i = 0; i < n; ++i ){
        getline( cin, str );
        cout << "Case " << "#" << i+1 << ": ";
        for ( int i = 0; i < str.size(); ++i ){
            cout << mp[str[i]];
        }
        cout << endl;
    }
    return 0;
}
