#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define len(X) ((int)(X.length()))
#define size(X) ((int) (X.size()))


using namespace std;

typedef long long ll;
typedef unsigned long long ull;

template<class T> inline T lowbit(T n){return (n^(n-1))&n;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}

template<class T> inline T sqr(T x){return x*x;}
template<class T> inline T powx10(int x){T res=1; while(x){res*=10;x--;} return res;}
template<class T> inline T powxy(T x,int y){T res=1; while(y){res*=x;y--;} return res;}
template<class T> inline T gcd(T a,T b)
  {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline bool isPrime(T n)
  {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}

int main(){
	string fname = "alarge";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int t=1,T,n,*a,*b,i,j,k,c,temp;
	scanf("%d",&T);
	while(t<=T){
		cin>>n;
		a=(int *)malloc(sizeof(int) *n);
		b=(int *)malloc(sizeof(int) *n);
		c=0;
		for(i=0;i<n;i++){
			cin>>a[i]>>b[i];
		}
		for(j=n-1;j>0;j--){
			for(k=0;k<j;k++){
				if(a[k]>a[k+1]){
					temp=a[k];
					a[k]=a[k+1];
					a[k+1]=temp;
					temp=b[k];
					b[k]=b[k+1];
					b[k+1]=temp;
					//c++;
				}
			}
		}
		for(j=n-1;j>0;j--){
			for(k=0;k<j;k++){
				if(b[k]>b[k+1]){
					temp=b[k];
					b[k]=b[k+1];
					b[k+1]=temp;
					c++;
				}
			}
		}
  		printf("Case #%d: %d\n",t,c);
		t++;
	}
	return 0;
}

/*	Soumya Ranjan Maharana
	soumya.r.maharana@gmail.com  */

/*	Dev C++ portable    version 4.9.9.2
	http://www.bloodshed.net/
	Copyright (C) Bloodshed software 		*/

