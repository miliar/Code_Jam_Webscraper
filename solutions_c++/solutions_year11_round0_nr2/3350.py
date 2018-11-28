#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <map>
#include <set>
#include <fstream>
#define x first
#define y second
#define mp make_pair
using namespace std;

int main(){
    ifstream fin  ("B-large.in");
    ofstream fout ("B-large.out");
    map <pair <char,char>, char> m;
    int z;
    fin>>z;
    for (int cases=1;cases<=z;cases++){
        int c,d,n;
        map <pair <char,char>, char> mc;
        fin>>c;
        for (int i=0;i<c;i++){
            string s;
            fin>>s;
            mc[mp(s[0],s[1])]=s[2];
            mc[mp(s[1],s[0])]=s[2];
        }
        map <pair <char,char>, char> md;
        fin>>d;
        for (int i=0;i<d;i++){
            string s;
            fin>>s;
            md[mp(s[0],s[1])]='#';
            md[mp(s[1],s[0])]='#';
        }
        fin>>n;
        string s="";
        for (int i=0;i<n;i++){
            char aux;
            fin>>aux;
            s+=aux;
            if (s.size()<2) continue;
            if (mc[mp(s[s.size()-1],s[s.size()-2])]){
                s[s.size()-2]=mc[mp(s[s.size()-1],s[s.size()-2])];
                s.erase(s.begin()+s.size()-1);
                continue;
            }
            for (int i=0;i<s.size()-1;i++){
                if (md[mp(s[i],s[s.size()-1])]){
                    s="";
                    break;
                }
            }
        }
        fout<<"Case #"<<cases<<": [";
        for (int i=0;i<s.size();i++){
            if (i) fout<<", ";
            fout<<s[i];
        }
        fout<<"]"<<endl;
    }
}
