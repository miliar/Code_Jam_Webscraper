#include<iostream>
#include<stack>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstdio>
#include<string>
#include<cstring>
#include<cmath>
#include<complex>
#include<sstream>
#include<map>
#include<set>
#define DEBUG(x) cout<<"line"<<__LINE__<<":"<<#x" == "<<x<<endl
#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define ALL(x) (x).begin(),(x).end()
#define INF 1000000
using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef long long ll;
typedef pair<int,int> P;

///////////////////////////////////////////////////////////////
int main(){
    int T;
    map<char,char> mapping;
    string a ="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv a z o q";
    string b ="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up y q e z";

    for(int i = 0;i<(int)a.length();i++){
        mapping.insert(map<char,char>::value_type(a[i],b[i]));
    }
    cin>> T;
    cin.ignore();
    vector<string> in(100);
    vector<string> out(100);
    string test;
     for(int i =0;i<T;i++){
         // if(i==0) {getline(cin,test);
         //     continue;}
         getline(cin,in[i]);
         for(int j = 0 ; j < (int)in[i].length();j++){
            out[i].push_back(mapping[in[i][j]]);
        }
        cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
     }

    return 0;
  
}

