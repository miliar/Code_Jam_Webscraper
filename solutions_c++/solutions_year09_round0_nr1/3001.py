
#include<conio.h>

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

vector<string> SPstring(string s){               
            vector<string> ans(0);
            string::size_type t=0,p=0;
            while(true){
                   if(t>=s.sz) break;     
                   if(s[t]!= '('){
                             ans.pb( s.substr(t++,1) );
                             continue;
                   }     
                   p= s.find_first_of(")",t);
                   //if(p== string::npos  ){ ans.pb( s.substr(t) ) ; break; }
                   if(p!=t) ans.pb( s.substr(t+1,p-t-1) );
                   t=p+1;
            }
            if( ans[ ans.size() - 1] == "" ) ans.erase( ans.end() );
            return ans;
}

int main()
{
    int L,D,N;
    
    ifstream in("a.in");
    ofstream out("a.out");
    
    in>>L>>D>>N;
    vector<string> w(D);
    
    string s;
    getline(in,s);
    for(int i=0; i<D; i++) getline(in,w[i]);
    for(int i=0; i<N; i++){
            getline(in,s);
            vs t = SPstring( s );
            
            int T[16];
            memset(T,0,sizeof T );
            
            bool f = true;
            for(int j=0; j<t.sz;j++){
                    for(int k=0; k<t[j].sz ; k++)
                            T[j]|= 1<<(t[j][k]-'a') ;
            }
            
            for(int j=0; j<t.sz;j++) cout<<t[j]<<" ";
            cout<<endl;
            for(int j=0; j<t.sz;j++) cout<<T[j]<<" ";
            cout<<endl;
            
            int ct=0;
            F(j,0,D){
                     bool f=true;
                     F(k,0,L)
                             if( !( T[k]&(1<<(w[j][k]-'a')) ) ){
                                 f=false;
                                 break;
                             }
                     if(f) ct++;
            }
            
            out << "Case #" << i+1 <<": " << ct <<endl;
    }
     
    out.close();
    in.close();                       
       
    getch();                     
}
