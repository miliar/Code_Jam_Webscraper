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

int mod=100003;

VI toBit(int a, int n){
//	cout<<"a= "<<a<<"n= "<<n<<endl;
	VI ret;
	FOR(i,1,n){
		if((a&(1<<i))!=0){
		//	cout<<"QQQ"<<endl;
			ret.PB(i+1);
		}
	//	else {
	//		cout<<"a = "<<a<<" i= "<<i<<" 1<<(i)= "<<(1<<i)<<endl;
	//	}
	}
//	cout<<"SZ= "<<ret.size()<<endl;
	return ret;
}

int main(){
	int C=1;
	map<int , int > mp ; 
	mp[25]=84884;
	mp[24]=13335;
	mp[23]=68060;
	mp[22]=40265;
	NT(){
		int n=SI ;
		if(mp.find(n)!=mp.end()){
			cout<<"Case #"<<C++<<": "<<mp[n]<<endl;
			continue;
		}
		int count=0;
		REP(i,1<<(n)){
			int a=i;
			if((a&1)==0 && (a&(1<<(n-1)))!=0){
			//	cout<<"inside a= "<<a<<endl;
				VI  b=toBit(i,n);
			//	PRV(b);
				int l=b.size();
				while(1){
					if(l==1){
						count++;
						break;
					}
					int ind=-1;
					REP(j,b.size()){
						if(b[j]==l){
							ind=j+1;
							break;
						}
					}
					l=ind;
					if(ind==-1)break;
				}
			}
		}
		mp[n]=count%mod;
		cout<<"Case #"<<C++<<": "<<count%mod<<endl;
	}
}
