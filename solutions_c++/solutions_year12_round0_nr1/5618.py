#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>

#define For(i,n) for(int i = 0;i<n;i++)
#define Fors(var,start,finish) for(int var = start, var <=finish, var++)

using namespace std;

const int maxn = 1000;
char m[maxn];
bool d[maxn]  = {0};
bool p[maxn] = {0};
int n,t;
string s;
string gc = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string en = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

void init(){
    For(i,gc.size()) m[gc[i]] = en[i];
    m['q'] = 'z';
    m['z'] = 'q';
    m[' '] = ' ';
}

int main(){
    init();
    cin>>t;
    cin.ignore();
    For(i,t){
        getline(cin,s);
        cout<<"Case #"<<i+1<<": ";
        For(i,s.size()) cout<<m[s[i]];
        cout<<endl;
    }
}
