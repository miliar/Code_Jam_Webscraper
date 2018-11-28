#include <iostream>
using namespace std;
string a['z'+1];
int b['z' + 1];
int main() {
    string x[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi" , 
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
     "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    string y[3] = {"our language is impossible to understand", 
    "there are twenty six factorial possibilities", 
    "so it is okay if you want to just give up"};
    for (int i = 0;i<3;i++)
        for(int j = 0;j < x[i].length() ; j++ ) {
          a[x[i][j]] = y[i][j];
          b[y[i][j]] = 1;
          }
    a['q'] = 'z';
    b['z'] = 1;
    freopen("A-small-attempt0 (1).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    char tmp;
    for(char i = 'a'; i <= 'z' ; i++) 
             if (!b[i] ) tmp = i;
    a['z'] = tmp;
    int t;
    scanf("%d\n", &t);
    for(int i = 0;i<t;i++) {
            cout << "Case #" << i+1 << ": ";
            string s;
            getline(cin, s);
            for(int i = 0;i<s.length(); i++) cout << a[s[i]] ;
            cout << endl;
    }
    return 0;   
}
