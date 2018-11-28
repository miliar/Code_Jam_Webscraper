/* Author - Rishi */
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
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include<string.h>
#include<math.h>
#include <climits>
#include <fstream>
#include <sstream>

using namespace std;

#define FOR(i,a,b)         for(int i= (int )a ; i < (int )b ; i++) 
#define FORD(i,a,b)        for(int i= (int )a ; i >= (int )b ; i--) 
#define REP(i,n)           FOR(i,0,n)
#define REPD(i,n)          FORD(i,n-1,0)
#define F                  first
#define S                  second
#define MP                 make_pair
#define PB                 push_back
#define PP                 pop()
#define EM                 empty()
#define INF                2000000000
#define PF                 push_front
#define ALL(x)             x.begin(),x.end()
#define SORT(x)            sort(ALL(x))
#define V(x)               vector< x >
#define PRINT(x)           cout << #x << " " << x << endl
#define SZ(x)              x.size();
#define PRV(v)             REP(Ind,v.size())cout<<v[Ind]<<" ";cout<<endl;
#define NT()               int nt;for(scanf("%d",&nt);nt;nt--)
#define SI                 ({int t;scanf("%d",&t);t;})

typedef map<int,int>    MI;
typedef pair<int,int>   PI;
typedef long long int   LL;
typedef V( int )        VI;
typedef V( VI )         VVI;
typedef V( PI  )        VPI;
typedef V( string )     VS;
typedef V( VS )         VVS;


VS PS(string a, char del)
{
        int  l=a.size();
        VS ret;
        REP(i,l)
        {
                if(a[i]!=del)
                {
                        string s;
                        while(i<l and a[i]!=del)
                                s.PB(a[i++]);
                        ret.PB(s);
                }
        }
        return ret;
}


int main(){
	int C=1;
	NT(){
		int n=SI ,  m=SI ;
		map<string , int > mp ; 
		REP(i,n){
			string str;
			cin>>str;

			VS a=PS(str , '/');
			string s="";
			REP(j,a.size()){
				s+="/"+a[j];
				mp[s]=1;
			}
		}
		int ans=0;
		REP(i,m){
			string str;
			cin>>str;
			
			VS a=PS(str , '/');
			string s="";
			REP(j,a.size()){
				s+="/"+a[j];
				if(mp.find(s)==mp.end()){
					mp[s]=1;
					ans++;
				}
			}
		}
		cout<<"Case #"<<C++<<": "<<ans<<endl;

	
	}
}
