#include <list>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>

#include <utility>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <ctime>

#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>

// All Macros
#define foreach(it,c) for(typeof((c).begin()) it=(c).begin(); it != (c).end() ; it++ )
#define F(i,mi,ma) for(int i=mi;i<ma;i++)

#define vi vector< int >
#define vs vector< string >
#define bn begin()
#define en end()
#define sz size()
#define pb push_back

#define mp make_pair
#define itr iterator

#define ld long double
#define ll long long

#define Fu(i,min,ma,inc) for(int i=min;i<ma;i+= inc)
#define Fd(i,ma,min,dec) for(int i=ma;i>=min;i-= dec)
#define vvi vector< vector< int > >
#define vvs vector < vs >
#define vd vector< double >
#define vvd vector< vd >
#define vb vector< bool >
#define vll vector< ll >

#define ERR 0.000000000001

using namespace std;

string rev(string a){
       string b="";
       F(i,0,a.size()) b+=a[a.size()-i-1];
       return b;
}

int main()
{
    int T;
    
    ifstream in("bbb.in");
    ofstream out("bbb.out");
    
    in>>T;
    string s;
    getline(in,s);
    F(i,0,T){
             getline(in,s);
             int m=s.sz;

             string ans=s;
             if( m > 1 ) {
                 for(int j=m-1; j>=0; j-- ){
                         bool f=false;
                         F(k,j+1,m) if( s[j] < s[k] ) { f=true; break; }
                         if(!f) continue;
                         
                         //cout<<s.substr(j)<<endl;
                         
                         ans = s.substr(0,j);
                         string t= s.substr(j);
                         char st = t[0];
                         sort(t.bn,t.en);
                         //t=rev(t);
                         int kk=-1;
                         F(k,1,t.sz) if( t[k] > st ) { kk = k; break; }
                         if( kk != -1){
                             ans += t[kk];
                             ans += t.substr(0,kk);
                             ans+= t.substr( kk+1 );
                             break;
                         }
                 }                      
             }
             if( ans == s ){
                 ans = s+"0";
                 sort(ans.bn,ans.en);
                 F(j,0,ans.sz){
                               if(ans[j]!= '0' ) { 
                                           string t="";
                                           t+=ans[j];
                                           t+= ans.substr(0,j);
                                           t+= ans.substr(j+1);
                                           ans =t;
                                           break;
                               }
                 }
             }
             
             out << "Case #"<<i+1<<": "<< ans<<endl;
    }
    
    out.close();
    in.close();                       
    
    cout<<"done";   
    getchar();                     
}
    
