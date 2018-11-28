//Made by: Albert Villalobos

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>
using namespace std;

long long elevar(long long a, long long b){
    if (b==0) return 1;
    long long result=a;
    for (int i=1;i<b;i++) result*=a;
    return result;
}


int main(){
    ifstream fin("A-Large.in");
    ofstream fout("A-Large.out");
    long long n;
    fin>>n;
    for (long long z=1;z<=n;z++){
        string s;
        fin>>s;
        set <char> st;
        for (long long i=0;i<s.size();i++) st.insert(s[i]);
        map <char,char> m;
        m[s[0]]='1';
        string res="1";
        char cont='0';
        for (long long i=1;i<s.size();i++){
            if (cont=='1') cont+=1;
            if (m[s[i]]==0){
                if (cont=='0') m[s[i]]='?';
                else m[s[i]]=cont;
                cont+=1;
            }
            if (m[s[i]]=='?') res+='0';
            else res+=m[s[i]];
        }
        int bas=st.size();
        if (bas==1) bas++;
        long long tot=0;
        for (long long i=0;res.size();i++){
            tot+=(res[res.size()-1]-'0')*elevar(bas,i);
            res.erase(res.begin()+res.size()-1);
        }
        fout<<"Case #"<<z<<": "<<tot<<endl;
    }
    fin.close();
    fout.close();
}
