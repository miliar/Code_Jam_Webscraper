#include <algorithm>
#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <vector>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair <char,int> pci;
const double eps = 1e-11;
const double pi = acos(-1.0);
const double inf = 1e17;
#define swap(a,b) {a^=b;b^a=;a^=b;}
#define two(X) (1<<(X))
#define pair <int,int> pii
#define SZ(x) ((int)x.size())
template<class T> T gcd(const T &a,const T &b) {return (b==0)?a:gcd(b,a%b);}
template<class T> T lcm(const T &a,const T &b) {return a*(b/gcd(a,b));}
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
string word = "welcome to code jam";
int solve(int i,int j,vector <pci> s){
     int rst = 0,k;
     if ( i == SZ(word) ) return 1;
     for (k=j;k<SZ(s);k++){
          if (s[k].first == word[i]){
             rst += (s[k].second * solve(i+1,k+1,s))%10000;
          }      
     }
     return rst;
}

int main(){
    int i,j,k,tmp,cnt;
    int N;
    int flag;
    string s;
    char icld[]={' ','w','e','l','c','o','m','t','d','j','a'};
    vector <char> s1;
    vector <pci> s2;
    cin>>N;
    getline(cin,s);
    for (i=0;i<N;i++){
        s1.erase(s1.begin(),s1.end());
        s2.erase(s2.begin(),s2.end());
        getline(cin,s);
        for (j=0;j<SZ(s);j++){
            flag = 0;
            for (k=0;k<11;k++){
                if (s[j]==icld[k]){
                   flag = 1;
                   break;
                }
            }
            if (flag){
               s1.push_back(s[j]);
            }
        }
        //for (j=0;j<SZ(s1);j++)    cout<<s1[j];cout<<endl;
        j = 0;
        cnt = 1;
        while ( j < SZ(s1) - 1 ){
              if (s1[j] == s1[j+1]){
                 cnt++;
              }else{
                 s2.push_back(make_pair<char,int>(s1[j],cnt));
                 cnt = 1;
              }
              j++;
        }
        s2.push_back(make_pair<char,int>(s1[j],cnt));
        //for (j=0;j<SZ(s2);j++)    cout<<s2[j].first<<s2[j].second; cout<<endl;

        //while (s2[0].first != 'w') s2.erase(s2.begin());
        cout<<"Case #"<<i+1<<": ";
        cout.width(4);
        cout.fill('0');
        cout<<solve(0,0,s2)%10000<<endl;
        //printf("Case #%d: %d\n",i+1, solve(0,0,s2) % 10000 );
        
    }
    return 0;
}
