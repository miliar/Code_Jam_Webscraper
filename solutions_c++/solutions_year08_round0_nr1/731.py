#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<set>
using namespace std;
 
//double PI =  3.14159265358979323846;
#define ll long long
#define VI vector<int>
#define VS vector<string>
#define PB push_back

int s2i (string s) {
    stringstream ss;
    ss<<s;
    int ret;
    ss>>ret;
    return ret;    
}

int main() {
    string nn;
    string ss;
    string qq;
    int n,s,q;
    getline(cin,nn);n=s2i(nn);
    for (int i=0;i<n;i++) {
        int ret=0;
        getline(cin,ss);s=s2i(ss);
        set<string> engine;
        for (int j=0;j<s;j++) {
            string eng;
            getline(cin,eng);
            //engine.PB(eng);    
        }            
        getline(cin,qq);q=s2i(qq);
        set<string> qs;
        for (int j=0;j<q;j++) {
            string qe;
            getline(cin,qe);
            qs.insert(qe);
            if (qs.size()==s) {
                  ret++;
                  qs.clear();
                  qs.insert(qe);            
            }
        }
        cout<<"Case #"<<i+1<<": "<<ret<<endl;
        
    }
    
        
    
    
}
