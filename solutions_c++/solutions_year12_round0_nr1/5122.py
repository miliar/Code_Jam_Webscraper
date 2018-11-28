#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<deque>
#include<set>
using namespace std;
#define ll long long
#define VI vector<ll>
#define VS vector<string>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back


int main() {

string s="ejp mysljylc kd kxveddknmc re jsicpdrysi";
s+="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
s+="de kr kd eoya kw aej tysr re ujdr lkgc jv";

string t="our language is impossible to understand";
t+="there are twenty six factorial possibilities";
t+="so it is okay if you want to just give up";

char a[256];
a['z']='q';
a['q']='z';
for (int i=0;i<s.size();i++) a[s[i]]=t[i];
//for (char c='a';c<='z';c++) cout<<c<<" "<<a[c]<<endl;

string snum="";
getline(cin,snum);
stringstream ss;
ss<<snum;
int num;
ss>>num;
string inp;
for (int i=0;i<num;i++) {
    getline(cin,inp);
    cout<<"Case #"<<i+1<<": ";
    for (int j=0;j<inp.size();j++) {
        cout<<a[inp[j]];
    }
    cout<<endl;
}


}
