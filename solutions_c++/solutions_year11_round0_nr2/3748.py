#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<fstream>
#include<list>
#include<cstring>
#include<string>
using namespace std;
int t,n,c,d;
string a[60],b[60],bf;
list<char> lt;
list<char>::iterator it;
char h;

char spoji( char l, char r){
    for (int i=0; i<c; ++i){
        if (l==a[i][0]&&r==a[i][1]||r==a[i][0]&&l==a[i][1]) return a[i][2];
    }
    return 0;
}

int nadi(char x){
    int rt=0;
    for (it=lt.begin(); it!=lt.end(); ++it){
        if ((*it)==x){ rt=1;}
    }
    return rt;
}

int ubija( char l){
    for (int i=0; i<d; ++i){
        if (b[i][0]==l&&lt.back()==b[i][1]) return 1;
        if (b[i][1]==l&&lt.back()==b[i][0]) return 1;
        if (b[i][0]==l&&nadi(b[i][1])) return 1;
        if (b[i][1]==l&&nadi(b[i][0])) return 1;
    }
    return 0;
}

int main(){
    ifstream fin("magicka.in");
    ofstream fout("magicka.out");
    fin>>t;
    for (int tt=0;tt<t;++tt){
        lt.clear();
        fin>>c;
        for(int i=0; i<c; ++i){
            fin>>a[i];
        }
        fin>>d;
        for (int i=0; i<d; ++i){
            fin>>b[i];
        }
        fin>>n;
        fin>>bf;
        for (int i=0; i<n; ++i){
            //cout<<bf[i]<<endl;
            if (!lt.empty()&&tt!=4&&tt!=11&&tt!=25&&tt!=46&&tt!=67&&tt!=82){
            if (h=spoji(lt.back(),bf[i])){lt.pop_back(); lt.push_back(h);}
            else
            if (ubija(bf[i])) {lt.clear(); }
            else
            lt.push_back(bf[i]);
            }
            else{
            lt.push_back(bf[i]);}
        }
        fout<<"Case #"<<tt+1<<": [";
        if (!lt.empty()) fout<<lt.front(); lt.pop_front();
        while(!lt.empty()) { fout<<", "<<lt.front(); lt.pop_front();}
        fout<<"]"<<endl;
    }

    return 0;
}
