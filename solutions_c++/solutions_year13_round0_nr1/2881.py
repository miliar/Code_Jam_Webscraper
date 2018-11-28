/*
 * =====================================================================================
 *
 *       Filename:  A.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2013年04月13日 09时22分32秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Wang Shengyu (nbuacm09), 
 *        Company:  
 *
 * =====================================================================================
 */
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define ll long long
using namespace std;
template<class T> T gcd(T x,T y){while(T t=x%y)x=y,y=t;return y;}
const double eps = 1e-10;
const double PI = acos(-1.);
const int INF = 1000000000;
const int MOD = 1000000007;
const double E = 2.7182818284590452353602874713527;

#define pmul(x1,y1,x2,y2) ((x1)*(x2)+(y1)*(y2))
#define xmul(x1,y1,x2,y2) ((x1)*(y2)-(x2)*(y1))
#define sqr(x) ((x)*(x))

#define FR(i,N) for(int i=0;i<N;i++)
#define _FR(i,N) for(i=0;i<N;i++)
#define FRS(i,S,E) for(int i=S;i<=E;i++)
#define _FRS(i,S,E) for(i=S;i<=E;i++)
#define FRD(i,S,E) for(int i=S;i>=E;i--)
#define _FRD(i,S,E) for(i=S;i>=E;i--)
#define SZ(x) ((int)(x).size())
#define fill(a,b) memset(a,b,sizeof(a));
#define MP(a,b) make_pair(a,b)
#define PII pair<int,int>
#define PLL pair<ll,ll>
#define fi first
#define se second
#define all(x) (x).begin(),(x).end()
#define PB push_back
#define lowbit(x) ((x)&(-(x)))

bool isdig(char x){return x>='0'&&x<='9';}
bool isup(char x){return x>='A'&&x<='Z';}
bool islow(char x){return x>='a'&&x<='z';}
bool islet(char x){return isup(x)||islow(x);}

//--------CODE----------
char mp[5][5];
void get_data(){
	FR(i,4)scanf("%s",mp[i]);	
}
int cnt(){
	int r = 0;
	FR(i,4)FR(j,4)r += mp[i][j] == '.';
	return 16-r;
}
int cal(char x){
	int t;
	FR(i,4){
		t = 0;
		FR(j,4)t += mp[i][j] == x || mp[i][j] == 'T';
		if(t == 4)return 1;
	}
	FR(j,4){
		t = 0;
		FR(i,4)t += mp[i][j] == x || mp[i][j] == 'T';
		if(t == 4)return 1;
	}
	t = 0;
	FR(i,4)t += mp[i][i] == x || mp[i][i] == 'T';
	if(t == 4)return 1;
	t = 0;
	FR(i,4)t += mp[i][3-i] == x || mp[i][3-i] == 'T';
	if(t == 4)return 1;
	return 0;
}
void run(){
	int o = cal('O'), x = cal('X');
	int tot = cnt();
	if(!o && !x){
		if(tot == 16)cout<<"Draw"<<endl;
		else cout<<"Game has not completed"<<endl;
	}else{
		if(o && x)while(true);
		else{
			if(o)cout<<"O won"<<endl;
			else cout<<"X won"<<endl;
		}
	}
}

int main ( int argc, char *argv[] ){
	//	get_prime();
		freopen("A-large.in","r",stdin);
		freopen("output.out","w",stdout);
	int t,i=0;
	cin>>t;
	while(t--)
	{
		get_data();
		printf("Case #%d: ",++i);
		run();
	}
	return EXIT_SUCCESS;
}

