// All includes 
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

#include <list>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>

#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <ctime>

#include <functional>
#include <numeric>
#include <iomanip>
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

long long STL(string s){
     long long a=s[0]-'0';
     for(int i=1;i<s.size();i++)
             a=a*10+(s[i]-'0');
     return a;
} 
vector<string> SPstring(string s,const string delim){               
            vector<string> ans(0);
            string::size_type t=0,p=0;
            while(true){
                   p= s.find_first_of(delim,t);
                   if(p== string::npos  ){ ans.pb( s.substr(t) ) ; break; }
                   if(p!=t) ans.pb( s.substr(t,p-t) );
                   t=p+1;
            }
            if( ans[ ans.size() - 1] == "" ) ans.erase( ans.end() );
            return ans;
}
long long getn(string s)
{
     vs ip=SPstring(s," ");
     long long N = STL(ip[0]);
     
     long long no=1,nb=1,to=0,tb=0,ans=0,ta=0,cb=0;
     F(i,0,N){       
              cb= STL( ip[1+2*i+1] );             
              if( ip[ 1+2*i ][0] == 'O' ){
                  ta = max(0LL, abs(cb-no)-(ans-to) );
                  ans+= ta+1;
                  no = cb;
                  to = ans;
              }
              else{
                  ta = max(0LL, abs(cb-nb)-(ans-tb) );
                  ans+= ta+1;
                  nb = cb;
                  tb = ans;
              }
     }
     return ans;                 
}

int main()
{
    //ifstream in("A-small-attempt0.in");
    //ofstream out("A-Soutput.out");
    
    ifstream in("A-large.in");
    ofstream out("A-Loutput.out");
    
    //while(in){
              string s;
              getline(in,s);
              int T = STL(s);
              F(i,0,T){
                       getline(in,s);
                       cout<<s;
                       long long ans = getn(s);
                       cout<<" : "<<ans<<endl;
                       out<<"Case #"<<i+1<<": "<<ans<<endl;
              }
    //}
    out.close();
    in.close();
    getchar();
}
