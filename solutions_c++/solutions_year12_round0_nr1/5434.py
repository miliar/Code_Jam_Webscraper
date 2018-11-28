#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

#define pb push_back
#define mp make_pair
#define sz size()
#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define vint vector<int>
#define forn(i,n) for (int (i)=0; (i)<(n); (i)++)

using namespace std;
const int INF=~(1<<31);
const double EPS=1e-6;
const double PI=3.141592653589793;

int main(){
#ifdef HOME
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
   string s1="abcdefghijklmnopqrstuvwxyz ";
   string s2="yhesocvxduiglbkrztnwjpfmaq ";
   map<char,char>m;
   forn(i,s1.sz) m[s1[i]]=s2[i];
   int n;
   string s;
   cin>>n;
   getline(cin,s);
   forn(i,n) {
	   cout<<"Case #"<<i+1<<": ";
	   getline(cin,s);
	   forn(j,s.sz) cout<<m[s[j]];
	   cout<<endl;
   }
   return 0;
}