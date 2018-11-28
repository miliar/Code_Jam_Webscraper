#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
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

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,a) for(int i=0;i<(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

typedef vector<int> vi;
typedef vector<vector<int> > vvi;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

void printvec(vector<int> a)
{
 cout<<"Vecteur:  ";
 REP(i,a.size()) cout<<a[i]<<"  ";
 cout<<endl;
}

string w;
int c;

void solve(string s, int ind, int wi)
{
     if(wi == w.size()) { c++; return; }
    if(ind >= s.size())
    { 
           if(wi == w.size()) c = (c+1)%10000;
           return;
    
    }
    for(int i = ind; i < s.size(); i++) if(s[i] == w[wi]) solve(s,i,wi+1);
}


int main()
{
   
   freopen("C-small-attempt0.in","r",stdin);
   freopen("C-small.out","w",stdout);
   
   w = "welcome to code jam";
   string s;
   getline(cin,s);
   int n;
   sscanf(s.c_str(),"%d",&n);
   REP(k,n)
   {
           getline(cin,s);
           c = 0;
           solve(s, 0, 0);
           printf("Case #%d: ",k+1);
           string sc = i2a(c);
           while(sc.size()<4)sc = "0" + sc;
           cout<<sc<<endl;
                   
   }


    return 0;
}
