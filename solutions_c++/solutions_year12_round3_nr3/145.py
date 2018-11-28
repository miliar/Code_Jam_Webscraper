/*
Some famous quotes about the greatest batsman on earth =>  <--------------SACHIN TENDULKAR------------------->
"I want my son to become Sachin Tendulkar."-Brian Lara(WI)
"We did not lose to a team called India, we lost to a man called Sachin."-Mark Taylor(AUS)
"There are 2 kinds of batsmen in this world. 1)Sachin Tendulkar 2)All of the others."-Andy Flower(ZIM)
"I have seen God. He bats at no.4 for India in tests."-Matthew Hayden(AUS)
"I see myself when i see Sachin batting."-Don Bradman(AUS)
"Commit you sins while Sachin is batting, for even the lord is watching"-(AUS fan)
"Sachin is a genius , i am a mere mortal!"-Brian Lara(WI)
"I would go to bed having nightemares of sachin dancing down the ground and hitting me for sixes."-Shane Warne(AUS)
"Don't bowl him bad balls, he hits the good ones for fours."-Michael Kasprowicz(AUS)
"Nothing bad can happen to us if we're on a plane in India with Sachin Tendulkar on it.(After terror attacks)"-Hashim Amla(RSA)
"I never get tired during umpiring whenever sachin is on crease"-Rudi Kortzen(umpire)
"Sachin Tendulkar! If he isn't the best player in the world, I want to see the best player in the world".-David Shepard(umpire)
"If cricket is religion, Sachin is god"-(all fans)
*/

// <-------TEMPLATE--------->
// Author: suh_ash2008
#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cassert>
#include <string.h>
using namespace std;
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define SET(x,a) memset(x,a,sizeof(x))
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define tr(i,a) for(__typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define sz(a) (int)(a.size())
#define INF (int)1e9
#define EPS (double)1e-9
#define is istringstream
#define os ostringstream
#define lb lower_bound
#define ub upper_bound
#define bs binary_search
typedef long long LL;
typedef unsigned long long ULL;
typedef pair< int,int > ii;
typedef pair< int,ii > pii;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;
/*
// <----------------------FAST I/O---------------------->
#define MAXX 10000000
char *ipos,*opos,InpFile[MAXX],OutFile[MAXX],DIP[30];
inline int input_int(int flag=0){while(*ipos<=32)++ipos;if(flag)return(*ipos++-'0');int x=0,neg=0;char c;while(true){c=*ipos++;if(c=='-')neg=1;else{if(c<=32)return neg?-x:x;x=(x<<1)+(x<<3)+c-'0';}}}
inline LL input_LL(int flag=0){while(*ipos<=32)++ipos;if(flag)return(*ipos++-'0');LL x=0,neg=0;char c;while(true){c=*ipos++;if(c=='-')neg=1;else{if(c<=32)return neg?-x:x;x=(x<<1)+(x<<3)+c-'0';}}}
inline void input_st(char *s){while(*ipos<=32)++ipos;int pos=0;char c;while(true){c=*ipos++;if(c<=32){s[pos]='\0';break;}else s[pos++]=c;}}
inline char input_ch(){while(*ipos<=32)++ipos;char c=*ipos++;return c;}
inline void output(int x){int y;int dig=0;while(x||!dig){y=x/10;DIP[dig++]=x-((y<<3)+(y<<1))+'0';x=y;}while(dig--)*opos++=DIP[dig];}
inline void InitFASTIO(){ipos=InpFile;opos=OutFile;fread_unlocked(InpFile,MAXX,1,stdin);}
inline void FlushFASTIO(){fwrite_unlocked(OutFile,opos-OutFile,1,stdout);}
// <----------------------END OF FAST I/O---------------------->
*/
// <----------------------END OF TEMPLATE---------------------->

// <---------------------MAIN CODE STARTS HERE--------------------->

#define MAXN 100+5

int n, m;

LL a[MAXN];
LL b[MAXN];

int A[MAXN];
int B[MAXN];
int f[MAXN];
int nxtA[MAXN];
int nxtB[MAXN];

int seenid;
int seen[MAXN][MAXN];
LL dp[MAXN][MAXN];

LL go(int i, int j){
	if(i == n || j == m)	return 0;
	if(seen[i][j] == seenid)	return dp[i][j];
	seen[i][j] = seenid;
	LL ret = 0;
	if(A[i] == B[j] && A[i] != 101){
		LL sum1 = 0, k1 = i;
		while(k1 != n){
			sum1 += a[k1];
			LL sum2 = 0, k2 = j;
			while(k2 != m){
				sum2 += b[k2];
				ret = max(ret, min(sum1, sum2) + go(k1+1, k2+1));
				k2 = nxtB[k2];
			}
			k1 = nxtA[k1];
		}
	}
	else ret = max(go(i+1, j), go(i, j+1));
	return dp[i][j] = ret;
}

int main(){
	ifstream fin("Ain.txt");
	ofstream fout("Aout.txt");
	int t, kase = 0;
	seenid = 0;
	fin >> t;
	while(t--){
		kase++, seenid++;
		fin >> n >> m;
		REP(i, n)	fin >> a[i] >> A[i];
		REP(j, m)	fin >> b[j] >> B[j];
		int i = 0, j = 0;
		LL sum = 0;
		while(j < n){
			if(A[i] == A[j]){
				sum += a[j];
				if(j != i)	A[j] = 101;
				j++;
			}
			else{
				a[i] = sum;
				i = j;
				sum = 0;
			}
		}
		a[i] = sum;
		
		i = 0, j = 0;
		sum = 0;
		while(j < m){
			if(B[i] == B[j]){
				sum += b[j];
				if(j != i)	B[j] = 101;
				j++;
			}
			else{
				b[i] = sum;
				i = j;
				sum = 0;
			}
		}
		b[i] = sum;
		
		REP(i, 102)	f[i] = n;
		ROF(i, n-1, -1){
			nxtA[i] = f[ A[i] ];
			f[ A[i] ] = i;
		}
		
		REP(i, 102)	f[i] = m;
		ROF(i, m-1, -1){
			nxtB[i] = f[ B[i] ];
			f[ B[i] ] = i;
		}
		fout << "Case #" << kase << ": " << go(0, 0) << endl;
	}
	fin.close();
	fout.close();
    return 0;
}
