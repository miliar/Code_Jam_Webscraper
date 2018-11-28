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
int T,p,N,S,score;
fin>>T;
forn(tt,T){

fin>>N>>S>>p;
int sum=0;
forn(i,N){
fin>>score;
if(p==0) {sum++; continue;}
if((score-1)/3+1>=p && (score-1)/3+1<=score) sum++;
else if(S>0) {
    if((score-2)/3+2>=p && (score-2)/3+2<=score) {sum++; S--;}
}
}
fout<<"Case #"<<tt+1<<": "<<sum<<endl;
}
}






