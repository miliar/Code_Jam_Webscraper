#include <iostream>
#include <string>

using namespace std;

const int maxd = 5010;

int L,D,N;

string words[maxd];

bool match(string &s, string &w) {
    for(int i=0,p=0;i<L;i++,p++) {
        bool m=false;
        if(s[p]=='(') {
            while(s[p]!=')') {
                if(s[p]==w[i]) m=true;
                ++p;
            }
        }
        else {
            if(s[p]==w[i]) m=true;
        }
        if(!m) return false;
    }
    return true;
}

int cnt(string &s) {
    int res = 0;
    for(int i=0;i<D;i++) {
        if(match(s,words[i])) res++;
    }
    return res;
}

int main() {
    cin>>L>>D>>N;
    for(int i=0;i<D;i++) {
        cin>>words[i];
    }
    for(int i=1;i<=N;i++) {
        string s;
        cin>>s;
        cout<<"Case #"<<i<<": "<<cnt(s)<<endl;
    }
    return 0;
}

