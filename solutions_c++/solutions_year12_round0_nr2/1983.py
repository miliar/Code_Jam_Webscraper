//C 
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <ctype.h> 
#include <math.h> 
#include <time.h> 
//C++ 
#include <iostream> 
#include <algorithm> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <cctype> 
#include <stack> 
#include <string> 
#include <list> 
#include <queue> 
#include <map> 
#include <vector> 
#include <deque> 
#include <set> 
using namespace std; 

//*************************JUDGE************************** 
#define LOCAL_HOST 
#define ONLINE_JUDGE 
#define TIME_OUT_PUT 

//**************************CONSTANT*********************** 
#define INF 0x7F7F7F7F 
#define eps 1e-8 
#define PI acos( -1. ) 
#define PI2 asin ( 1. ); 
typedef long long LL; 
//typedef __int64 LL;   //codeforces 
#define MP make_pair 
typedef vector<int> VI; 
typedef vector<int> VS; 
typedef pair<int , int> PII; 
#define pb push_back 
#define mp make_pair 

//***************************SENTENCE************************ 
#define FOR(a,b,i) for ( i = a ; i < b ; i++ ) 
#define FORE(a,b,i) for ( i = a ; i <= b ; i++ ) 
#define REP(i,n) FOR(0,n,i) 
#define CL(a,b) memset ( a , b , sizeof ( a ) ) 
#define sqr(a,b) sqrt ( (double)(a)*(a) + (b)*(b) ) 

//****************************FUNCTION************************ 
template < typename T > double DIS ( T va , T vb ) { return sqr ( va.x - vb.x , va.y - vb.y ); } 
template <class T> inline T INT_LEN( T v ) { int len = 1 ; while ( v /= 10 ) ++len; return len; } 

//end 

int dd[1024];
int s,p,n;

void input(){
	scanf("%d %d %d",&n,&s,&p);
	
	for (int i = 0; i < n; i++)
	{
		scanf("%d",dd+i);
	}

}

bool cmp(const int a,const int b){
	return a > b;
}

int solve(){
	int lim = (p - 1)*2+p;
	int lim2 = (p - 2)*2 + p;
	int i,ans = 0,ii = 0;
	sort(dd,dd+n,cmp);

	 if (p == 0)
	 {
		 lim = lim2 = 0;
	 }
	 else if (p == 1)
	 {
		 lim = 1;
		 lim2 =1;
	 }

	for (i = 0; i < n; i++)
	{
		if (dd[i] >= lim)
		{
			ans++;
		}
		else break;
	}
	for (ii = 0; i < n && ii < s; i++){
		if (dd[i] >= lim2)
		{
			ii++;
			ans++;
		}
		else break;
	}
	return ans;
	
}

int main(){
	int nCase;
	int ans;
	//	freopen("d:/2.in","r",stdin);
	//	freopen("d:/2.out","w",stdout);
	while (scanf("%d",&nCase) != EOF)
	{
		for (int i = 1; i <= nCase; i++)
		{
			input();
			printf("Case #%d: ",i);
			ans = solve();
			printf("%d\n",ans);
		}
	}
	return 0;
}