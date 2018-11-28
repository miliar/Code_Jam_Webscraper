#include <iostream>
#include <string>
#include <cstdio>
using namespace std;
string t,input;
int h[300],n;
int main () {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    for (char c='a';c<='z';++c) h[c] = c;

    string i1 = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
    string o1 = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

    for (int i=0;i<i1.length();++i) {
        if (i1[i]!=' ') {
            h[i1[i]]=o1[i];
        }
    }
    h['q'] = 'z';
    h['z'] = 'q';
    cin>>n;
    getline(cin, input);
    for (int i=0;i<n;++i) {

        getline(cin, input);
        t="";
        for (int i=0;i<input.length();++i) {
            if (input[i]==' ')
                t+=' ';
            else
                t+=h[input[i]];
        }
        cout<<"Case #";
        cout<<(i+1);
        cout<<": ";
        cout<<t<<endl;
    }
    return 0;
}
