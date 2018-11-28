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
int scount(string b,string d){
    int c=0;
    for(int i=0;i<b.size();i++){
            for(int j=0;j<d.size();j++){
                    if(b[i]==d[j]){
                                   c++;
                                   break;
                    }
            }
    }
    return c;
}
string getn(string s)
{
     vs ip=SPstring(s," ");
     map<string,char> comb;
     map<char,string> opps;
     string p1,p2;
     int k=0,c=STL(ip[0]);
     F(i,1,c+1){
            p1 = ""; p1+= ip[i][0]; p1+= ip[i][1];   
            p2 = ""; p2+= ip[i][1]; p2+= ip[i][0];
            comb[ p1 ] = ip[i][2];
            comb[ p2 ] = ip[i][2];   
     }   
     k+=c+1;
     int d= STL(ip[k]);
     F(i,k+1,d+k+1){
            opps[ ip[i][0] ]+= ip[i][1];
            opps[ ip[i][1] ]+= ip[i][0];   
     }
     k+=d+1;
     int n=STL(ip[k]),as=0;
     string ans="",ws=ip[k+1],tp="";        
     F(i,0,n){   
            as=ans.sz;        
            if(as == 0){ ans+= ws[i]; continue; }
            if(as>0){
                  tp= ""; tp+=ans[as-1]; tp+=ws[i];
                  if( comb.find( tp)!= comb.en ) ans = ans.substr(0,as-1)+comb[tp];
                  else if( scount(ans,opps[ws[i]]) > 0 )   ans = "";
                  else ans+= ws[i];
            }     
     }
     tp=ans;ans="[";
     if(tp.sz>0) ans+= tp[0];
     F(i,1,tp.sz) { ans+= ", "; ans+=tp[i]; }
     ans+="]";
     return ans;                 
}

int main()
{
    ifstream in("B-large.in");
    //ofstream out("B-Soutput.out");
    ofstream out("B-Loutput.out");
    
    //while(in){
              string s;
              getline(in,s);
              int T = STL(s);
              F(i,0,T){
                       getline(in,s);
                       cout<<s;
                       string ans = getn(s);
                       cout<<" : "<<ans<<endl;
                       out<<"Case #"<<i+1<<": "<<ans<<endl;
              }
    //}
    out.close();
    in.close();
    getchar();
}
