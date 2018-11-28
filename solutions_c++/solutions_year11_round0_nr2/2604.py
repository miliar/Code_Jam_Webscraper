#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <math.h>
#include <map>

using namespace std;

ifstream fin("B-small-attempt2.in");
ofstream fout("B-small.out");

int N, C, D;
map<string,char> base;
map<char,char> op;
string res = "";

bool search(char c, int idx) {
    for(int i = 0;i<idx;++i) {
        if(res[i] == c) {
            return true;
        }
    }
    return false;
}

int main() {
    int T;
    fin>>T;
    for(int k = 1;k<=T;++k) {
        fin>>C;
        base.clear();
        op.clear();
        for(int i = 0;i<C;++i) {
            string s;
            fin>>s;
            base[s.substr(0,2)] = s[2];
            reverse(s.begin(),s.end()-1);
            base[s.substr(0,2)] = s[2];
        }
        fin>>D;
        for(int i = 0;i<D;++i) {
            string s;
            fin>>s;
            op[s[0]] = s[1];
            op[s[1]] = s[0];
        }
        fin>>N;
        string s;
        fin>>s;
        res = "";
        for(int i = 0;i<N;++i) {
            res += s[i];
            if(res.size()>=2) {
                string b = res.substr(res.size()-2,2);
                if(base.find(b) != base.end())
                    res = res.substr(0,res.size()-2)+base[b];
            }
            char b = res[res.size()-1];
            if(op.find(b) != op.end() && search(op[b],res.size()-1)) res = "";
        }

        fout<<"Case #"<<k<<": "<<"[";
        for(int i = 0;i<((int)res.size())-1;++i)
            fout<<res[i]<<", ";
        if(res.size()>0)
            fout<<res[res.size()-1];
        fout<<"]"<<endl;
    }
    return 0;
}
