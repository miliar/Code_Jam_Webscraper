#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <cctype>
#include <map>
#include <iomanip>
//#include <fostream>
                   
using namespace std;
                   
#define eps 1e-8
#define pi acos(-1.0)
#define inf 1<<30
#define linf 1LL<<60
#define pb push_back
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long


char a[30];
int T;

int main() {
    string s1,s2;
    s1="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
    s2="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
    for (int i=0; i<s1.size(); i++){
        if (s1[i]!=' '){
            a[s1[i]-'a']=s2[i];
        }
    }
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);
    
    a[25]='q';
    a['q'-'a']='z';
    //for (int i=0; i<26; i++) cout <<(char)(i+'a') << " " << a[i] << endl;
    cin >> T;
    getchar();
    int Cas=0;
    while (T--){
        getline(cin,s1);
        //cout << s1 << endl;
        Cas++;
        cout << "Case #" << Cas << ": " ;
        for (int i=0; i<s1.size(); i++){
            if (!islower(s1[i])) cout << " " ;
            else cout << a[s1[i]-'a'] ;
        }
        cout << endl;
    }
    return 0;
}
