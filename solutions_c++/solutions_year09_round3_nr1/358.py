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
   return 1;                       
    
    cout<<"done";   
    getchar();                     
}
    
