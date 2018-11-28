#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

string s = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string t = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

char tb[256];
bool b[256];

void prepare(){
    memset(tb, 0, sizeof tb);
    memset(b, 0, sizeof b);
    for (int i=0; i<s.length(); ++i) tb[s[i]] = t[i];
    tb['z']='q';
    tb['q']='z';
}

int main(){
    prepare();
    int test; cin >> test; getchar();
    for (int cas=1; cas<=test; ++cas){
        getline(cin, s);
        cout << "Case #" << cas << ": ";
        for (int i=0; i<s.length(); ++i) s[i]=tb[s[i]];
        cout << s << endl;
    }
    return 0;
}
