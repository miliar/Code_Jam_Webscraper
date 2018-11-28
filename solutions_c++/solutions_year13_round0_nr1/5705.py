/*
*********************************************
Author:     neo0057
Institute:  IIIT Allahabad
*********************************************
*/

#include <vector>
#include <list>
#include <map>
#include <set>
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
 
#define debug(x) cout<<#x<<" = "<<x<<"\n"
#define print(x) cout<<x<<endl
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,a,n) for(int (i)=a;(i)<(n);(i)++)  
#define INF (1<<29) 
#define pb push_back 
#define sz size() 
#define ln length() 
#define mp make_pair 
#define all(a) a.begin(),a.end() 
#define fill(ar,val) memset(ar,val,sizeof ar) 
#define sqr(x) ((x)*(x)) 
#define min(a,b) ((a)<(b)?(a):(b)) 
#define max(a,b) ((a)>(b)?(a):(b)) 
 
using namespace std;
 
 
typedef int I;
typedef string STR;
typedef long long LL;
typedef map<I,I> MII;
typedef vector<I> VI;
typedef long double LD;
typedef vector<LL> VLL;
typedef vector<STR> VS;
typedef vector<VI> VVI;
typedef map<STR,I> MSI;
typedef map<I,MII> MMI;
typedef stringstream SS;
typedef map<char,I> MCI;
typedef map<STR,STR> MSS;

string s[4];

int check_row(int id){
	int i,cx=0,co=0;
	for(i=0;i<4;i++){
		if(s[id][i]=='X') cx++;
		else if(s[id][i]=='O') co++;
	}
	if(cx==4 || (cx == 3 && co ==0)) return 1;
	if(co==4 || (co == 3 && cx ==0)) return 2;
	return 0;
}
int check_col(int id){
	int i,cx=0,co=0;
	for(i=0;i<4;i++){
		if(s[i][id]=='X') cx++;
		else if(s[i][id]=='O') co++;
	}
	if(cx==4 || (cx == 3 && co ==0)) return 1;
	if(co==4 || (co == 3 && cx ==0)) return 2;
	return 0;
}
int check_diag1(){
	int i,cx=0,co=0;
	for(i=0;i<4;i++){
		if(s[i][i]=='X') cx++;
		else if(s[i][i]=='O') co++;
	}
	if(cx==4 || (cx == 3 && co ==0)) return 1;
	if(co==4 || (co == 3 && cx ==0)) return 2;
	return 0;
}
int check_diag2(){
	int i,j,cx=0,co=0;
	for(i=0,j=3;i<4&&j>=0;i++,j--){
		if(s[i][j]=='X') cx++;
		else if(s[i][j]=='O') co++;
	}
	if(cx==4 || (cx == 3 && co ==0)) return 1;
	if(co==4 || (co == 3 && cx ==0)) return 2;
	return 0;
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	int t,tc=1;
	int res;
	
	cin>>t;
	while(tc<=t){
		REP(i,4) cin>>s[i];
		int f = 0;
		cout<<"Case #"<<tc<<": ";
		REP(i,4){
			res = check_row(i);
			if(res == 1){ cout<<"X won\n"; f=1; break; }
			else if(res == 2){ cout<<"O won\n";	f=1; break; }
		}
		if(!f){
		REP(i,4){
			res = check_col(i);
			if(res == 1){ cout<<"X won\n"; f=1; break; }
			else if(res == 2){ cout<<"O won\n";	f=1; break; }
		}
		}
		if(!f){
			res = check_diag1();
			if(res==1){	cout<<"X won\n"; f=1; }
			else if(res == 2){ cout<<"O won\n";	f=1; }
		}
		if(!f){
			res = check_diag2();
			if(res==1){	cout<<"X won\n"; f=1;}
			else if(res == 2){ cout<<"O won\n";	f=1;}
		}
		int c=0;
		REP(i,4) REP(j,4){ if(s[i][j] != '.') c++; }
		if(!f && c < 16){ cout<<"Game has not completed\n";	f=1; }
		if(!f) cout<<"Draw\n";
		tc++;
	}
	return 0;
}


