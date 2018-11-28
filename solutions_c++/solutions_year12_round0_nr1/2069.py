#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>
#include <fstream>
#include<bitset>


using namespace std;

typedef long long int64;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define sz(x) ((int) (x).size())
#define pb push_back

int main(){

ifstream fin("a.txt");
ofstream fout("out.txt");

map<char,char> t;
t['y']='a';
t['e']='o';
t['q']='z';
t['z']='q';
string a1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
string a2="our language is impossible to understand";
string b1="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string b2="there are twenty six factorial possibilities";
string c1="de kr kd eoya kw aej tysr re ujdr lkgc jv";
string c2="so it is okay if you want to just give up";\

forn(i,a1.size())
t[a1[i]]=a2[i];
forn(i,b1.size())
t[b1[i]]=b2[i];
forn(i,c1.size())
t[c1[i]]=c2[i];

int T;
string k;
fin>>T;
getline(fin,k);
forn(tt,T){
getline(fin,k);
fout<<"Case #"<<tt+1<<": ";
forn(i,k.size())
fout<<t[k[i]];
fout<<endl;
}
}






