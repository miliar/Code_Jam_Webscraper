#include <map>
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

long long getn(vi &a, int base){
     long long ans = 0,t=1;
     int n=a.sz;
     F(i,0,n){
                 ans= ans + t*a[n-i-1];
                 t*=base;
     }
     //F(i,0,n) cout<<a[i]<<" ";
     //cout<<endl;
     //cout<<" = "<<ans<<endl;
     
     return ans;
}

int main()
{
    int T;
    
    ifstream in("c.in");
    ofstream out("c.out");
    
    in>>T;
    //string s;
    //getline(in,s);
    F(i,0,T){
             int P=0,Q;
             in>>P>>Q;
             //getline(in,s);
             vi rel(Q,0);
             F(j,0,Q) in>>rel[j];
             
             string s="";
             F(j,0,Q) {
                      char c= '0'+j ;
                      s+= c;
             }
             
             //F(j,0,Q) cout<<rel[j]<<" ";
             //cout<<endl;
             
             long long ans = 600;
             do{
                  long long t=0;
                  vector< pair<int, int> > cell;
                  cell.pb( make_pair(1,P) );    
                  F(j,0,s.sz){
                              int r = rel[ s[j] - '0' ];
                              F(k,0,cell.sz){
                                             if( r== cell[k].first ){
                                                 if ( cell[k].second <= cell[k].first ) continue;
                                                 t+= cell[k].second - cell[k].first ;
                                                 cell[k].first++;
                                                 break;
                                             }
                                             else if( r== cell[k].second ){
                                                 if ( cell[k].second <= cell[k].first ) continue;
                                                 t+= cell[k].second - cell[k].first ;
                                                 cell[k].second--;
                                                 break;
                                             }
                                             else if( r> cell[k].first and r< cell[k].second ){
                                                  t+= cell[k].second - cell[k].first ;
                                                  cell.pb( mp(r+1, cell[k].second) );
                                                  cell[k] = mp( cell[k].first, r-1 );
                                                  
                                                  break;
                                             }
                              }
                              
                              //cout<<"t= "<<t<<endl<<"grps: ";
                              //F(k,0,cell.sz) cout<<"("<<cell[k].first<<","<<cell[k].second<<") ";
                              //cout<<endl;
                  }
                  ans<?=t;                  
             }while( next_permutation( s.bn,s.en) );
                 
             
             out << "Case #"<<i+1<<": "<< ans<<endl;
    }
    
    out.close();
    in.close();                       
    
    cout<<"done";   
    getchar();                     
}
    
