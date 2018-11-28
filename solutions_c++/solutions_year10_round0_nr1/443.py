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
#define pb push_back
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
int n, k; 
int  main(){
   freopen("in.txt ", "r" ,stdin);
   freopen("out1.txt ", "w" ,stdout);
	int tt ;
    scanf("%d",&tt); 
	for(int i=1; i<=tt; ++i){
		scanf("%d%d",&n, &k); 
		 printf(  "Case #%d: ", i);
		int aa= (1<<n) ;
		k%=aa; 
        if(k==aa-1){
				 printf(  "ON\n");
		}
		else  printf(  "OFF\n");
	}
	fclose(stdin); 
	fclose(stdout); 
	return 0; 
}