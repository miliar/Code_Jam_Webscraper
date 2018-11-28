#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<queue>
#include<deque>
#include<set>
using namespace std;

//double PI =  3.14159265358979323846;
#define dd long double
#define ll long long
#define VI vector<int>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back
#define VVI vector<VI >
#define PS pair<string,string>
#define PD pair<double,double>
#define VS vector<string>
int ri() {
    string s;
    getline(cin,s);
    stringstream ss;
    ss<<s;
    int x;
    ss>>x;
    return x;
}

double cd(string s) {
    stringstream ss;
    ss<<s;
    double x;
    ss>>x;
    return x;
}
map<ll,double> p;
map<ll,string> meno;
map<string,ll> cislo;
VS tok;
map<string,int> f;

double eval(ll x) {
    double ret=p[x];
    if (meno.find(x)==meno.end()) return ret;
    else {
        if (f.find(meno[x])==f.end()) return ret*eval(2*x+1);
        else return ret*eval(2*x);
    }
}

void par(int root,int start,int end) {
  //  cout<<"# "<<root<<": "<<start<<" - "<<end<<endl;
    if (end-start==2) {
        p[root]=cd(tok[start+1]);
    } else {
        p[root]=cd(tok[start+1]);
        meno[root]=tok[start+2];
        cislo[meno[root]]=root;
        int poc=1;
        int pos=start+4;
        while (poc!=0) {
            if (tok[pos]==")") poc--;
            else if (tok[pos]=="(") poc++;
            pos++;
        }
        par(2*root,start+3,pos-1);
        par(2*root+1,pos,end-1);
    }

}

void parse(string& s) {
    p.clear();
    meno.clear();
    cislo.clear();
    tok.clear();
    ll current=1;
    string t=" ";
    for (int i=0;i<s.size();i++) {
        if (s[i]=='('||s[i]==')') { t+=" ";t+=s[i];t+=" ";}
        else t+=s[i];
    }
    stringstream ss;ss<<t;
    string pom;
    while (ss>>pom) tok.PB(pom);    
    par(1,0,tok.size()-1);
}

void solve() {
    string all="";
    int L=ri();
    for (int i=0;i<L;i++) { string s; getline(cin,s); all+=" "+s;}
    parse(all);
    int A=ri();
    for (int i=0;i<A;i++) {
        f.clear();
        string s;
        getline(cin,s);
        stringstream ss;
        ss<<s;
        ss>>s;
        ss>>s;
        while (ss>>s) { f[s]=1;}
        cout<<eval(1)<<endl;
    }
}


int main() {
   cout.setf(ios::fixed, ios::floatfield); cout.precision(10);
    int t=ri();
    for (int tt=0;tt<t;tt++) {
        cout<<"Case #"<<tt+1<<":"<<endl;
        solve();
    }
}
