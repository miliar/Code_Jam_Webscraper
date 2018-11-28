#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<set>
#include<bitset>
#include<algorithm>
#include<numeric>
#include<queue>
#include<list>
#include<limits>
#include<stack>
#include<sstream>
#include<fstream>
#include<ctime>
#include<cstdlib>
#include <complex>
#include <cctype>
#include <iomanip>
#include <functional>
#include<cstring>
using namespace std;
typedef long long int64 ;
typedef unsigned long long uint64 ;

#define two(X) (1<<(X)) 
#define twoL(X) (((int64)(1))<<(X))
#define PB push_back
const double PI= acos(-1.0) ;
const double eps= 1e-11 ; 
#define SZ(X) ((int)(X.size()))
#define LEN(X) ((int)(X.length()))
#define MP(X,Y) make_pair(X,Y) 
#define CLR(que)   while(!que.empty()) que.pop() 
#define CA(a, m, n) for(int ii=0; ii<m; ++ii){  for(int jj=0;  jj<n; ++jj)   cout<<a[ii][jj]<<"¡¡" ; puts("")  ;}
inline int  lowbit(int n) { return n&(-n) ;} 
template<class T> inline void chkmin(T &a, T b) { if(b<a) a=b ;} 
template<class T> inline void chkmax(T &a, T b) { if(b>a) a=b ;} 
static int dirx[4] ={ -1 , 0, 1, 0}  ;
static int diry[4] ={ 0,  1, 0, -1}  ;
int main(){
	int n , m ;
	int tt; 
	freopen("in.txt","r" ,stdin) ;
	freopen("out.txt", "w", stdout); 
	scanf("%d",&tt); 
	for(int Cas=1; Cas<=tt; ++Cas){
	    scanf("%d%d",&n ,&m) ;
		int ans=0; 
		map<string , bool > lne ; 
		lne.clear(); 
		for(int i=0; i<n ;++i){
			string  tmp=""; 
			cin>>tmp; 
			lne[tmp]=1; 
		}
		for(int i=0; i<m; ++i){
			string tmp=""; 
			string god="/"; 
			cin>>tmp; 
			for(int  j=1; j<LEN(tmp); ++j){
				if(tmp[j]=='/'){
					if(lne.find(god)==lne.end()){
						++ans; 
						lne[god]=1; 
	
					}
				}
				god+=tmp[j]  ;
				if(j==LEN(tmp)-1){
										if(lne.find(god)==lne.end()){
						++ans; 
						lne[god]=1; 

					}
				}
					
			}
		}
		cout<<"Case #"<<Cas<<": "<<ans<<endl; 
	}
	return 0; 
}//D:\programme files\npp.5.6.8.bin\ansi\gcja.cpp
				
	