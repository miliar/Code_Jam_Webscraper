#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>

using namespace std;
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define REP(a,b) FOR(a,0,b)
/*
int toint(string s){
     stringstream ss;
     ss<<s;
     int t;
     ss>>t;
     return t;
}
string tostring(int s){
     stringstream ss;
     ss<<s;
     string t;
     ss>>t;
     return t;
}

 bool isPrime(int x){
         for(int i=2;i*i<=x;i++){
                 if(x % i == 0){
                         return false;
                 }
         }
         return x != 1;
 }
*/

int main(){
map<char,char> ch;
ch['y']='a';
ch['n'] = 'b';
ch['f'] = 'c';
ch['i']='d';
ch['c']='e';
ch['w']='f';
ch['l']='g';
ch['b']='h';
ch['k']='i';
ch['u']='j';
ch['o']='k';
ch['m']='l';
ch['x']='m';
ch['s']='n';
ch['e']='o';
ch['v']='p';
ch['z']='q';
ch['p']='r';
ch['d']='s';
ch['r']='t';
ch['j']='u';
ch['g']='v';
ch['t']='w';
ch['h']='x';
ch['a']='y';
ch['q']='z';
int n;
string s1;
cin>>n;
cin.get();
for(int i=0;i<n;i++){
        getline(cin,s1);
        cout<<"Case #"<<i+1<<": ";
        string s2="";
        for(int j=0;j<s1.size();j++){
                if(s1[j]!=' '){
                                s2+=ch[s1[j]];
                }else{
                      s2+=' ';
                }
        }
        cout<<s2<<"\n";
}

//while(1);
return 0;
}
