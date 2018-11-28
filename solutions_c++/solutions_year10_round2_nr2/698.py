#include <vector>
#include <cassert>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include<string.h>

using namespace std;

#define FOR(i,a,b)         for(int i= (int )a ; i < (int )b ; i++)
#define REP(i,n)           FOR(i,0,n)
#define F                  first
#define S                  second
#define MP                 make_pair
#define SORT(x)            sort(x.begin(),x.end())
#define V(x)               vector< x >

typedef map<int,int>    MI;
typedef pair<int,int>   PI;
typedef long long int   LL;
typedef V( int )        VI;
typedef V( VI )         VVI;
typedef V( PI  )        VPI;
typedef V( string )     VS;
typedef V( VS )         VVS;

int main(){
                int Case=1;
                        int nt;
                                cin>>nt;
                                        while(nt--){
                                                                int n,k,b,t;
                                                                                cin>>n>>k>>b>>t;
                                                                                                V(PI ) a(n);
                                                                                                                REP(i,n)cin>>a[i].F;
                                                                                                                                REP(i,n)cin>>a[i].S;

                                                                                                                                            SORT(a);
                                                                                                                                            int count=0;
                                                                                                                                            for(int i=n-1;i>=0;i--){
                                                                                                                                                    if(k==0)break;
                                                                                                                                                    if(a[i].F+t*a[i].S>=b){
                                                                                                                                                            k--;
                                                                                                                                                            FOR(j,i+1,n){
                                                                                                                                                                    if(a[j].F+t*a[j].S<b)
                                                                                                                                                                            count++;
                                                                                                                                                            }
                                                                                                                                                    }
                                                                                                                                            }
                                                                                                                                            if(k==0)
                                                                                                                                                    cout<<"Case #"<<Case++<<": "<<count<<endl;
                                                                                                                                            else
                                                                                                                                                    cout<<"Case #"<<Case++<<": "<<"IMPOSSIBLE\n";
                                                                                                                                    }
}

