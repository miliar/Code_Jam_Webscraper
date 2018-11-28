/************************************************************************************************************

	AUTHOR : coderhead_42

	FILE NAME : tictactoe.cpp

	CREATION DATE : Sat 13 Apr 2013 07:09:32 PM IST

	LAST MODIFIED : Sat 13 Apr 2013 08:32:38 PM IST
			
*************************************************************************************************************/


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
#include<typeinfo>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<int>::iterator VII;
typedef vector<vector <int> > VVI;
typedef vector<vector <int> >::iterator VVII;
typedef vector<string> VSTR;
typedef vector<string>::iterator VSTRI;
typedef string STR;
typedef string::iterator STRI;
typedef pair<int,int> PII;
typedef list<int> LI;
typedef list<int>::iterator LII;


#define INF (int)1e9
#define LINF (long long)1e18
#define EPS 1e-9
#define MP make_pair
#define PB push_back
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int) (x).size())
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORi(i,a,b) for (i=a;i<b;i++)
#define ROF(i,a,b) for(int i=a-1;i>=b;i--)
#define ROFi(i,a,b) for (i=a-1;i>=0;i--)
#define DIS(a)	sort(all(a)); a.erase(unique(all(a)),a.end())
#define SI ({int x;scanf("%d",&x);x;})
#define SC ({char c;scanf("%c",&c);c;})
#define SIC ({scanf("%*c");})
#define SMP(a,b,c) printf("%d%s",a,b==c-1?"":"\n");
#define IATOV(a) ({vector<int> v(a,a+sizeof(a)/sizeof(int));v;})
#define CATOV(a) ({vector<char> v(a,a+sizeof(a)/sizeof(char));v;})
#define BS(a,x) ({int z=(lower_bound(ALL(a),x)-(a).begin());(z==0&&a[0]!=x)?-1:z;})
#define CASE ({printf("Case #%d: ",testcase+1);})
#define DEBUG 1

/****************************************************************************************************************************/

int main(){

#ifdef DEBUG
  double tmp_start = clock();
  fprintf(stderr, "Start\n");
#endif

int n=SI;
FOR(testcase,0,n){
	bool dots=false;
	bool flag=false;
	VSTR a(4);
	FOR(i,0,4)
		cin>>a[i];

	int xcnt_r[4]={0},ocnt_r[4]={0},tcnt_r[4]={0},dcnt=0,xcnt_c[4]={0},ocnt_c[4]={0},tcnt_c[4]={0},xcnt_d=0,ocnt_d=0,tcnt_d=0,xcnt_rd=0,ocnt_rd=0,tcnt_rd=0;
	FOR(i,0,4){
		FOR(j,0,4){
			if(a[i][j]=='.')
				dcnt++;
			if(i==j&&a[i][j]=='O')
				ocnt_d++;
			if(i==j&&a[i][j]=='T')
				tcnt_d++;
			if(i==j&&a[i][j]=='X')
				xcnt_d++;
			if(i+j==3&&a[i][j]=='O')
				ocnt_rd++;
			if(i+j==3&&a[i][j]=='T')
				tcnt_rd++;
			if(i+j==3&&a[i][j]=='X')
				xcnt_rd++;
			if(a[i][j]=='O'){
				ocnt_r[i]++;
				ocnt_c[j]++;
			}
			if(a[i][j]=='T'){
				tcnt_r[i]++;
				tcnt_c[j]++;
			}
			if(a[i][j]=='X'){
				xcnt_r[i]++;
				xcnt_c[j]++;
			}
		}
	}
	bool win_flag=false,draw=true;
	
	if(xcnt_d==4||(xcnt_d==3&&tcnt_d==1)){
		CASE;
		cout<<"X won\n";
		continue;
	}
	if(xcnt_rd==4||(xcnt_rd==3&&tcnt_rd==1)){
		CASE;
		cout<<"X won\n";
		continue;
	}
	if(ocnt_d==4||(ocnt_d==3&&tcnt_d==1)){
		CASE;
		cout<<"O won\n";
		continue;
	}
	if(ocnt_rd==4||(ocnt_rd==3&&tcnt_rd==1)){
		CASE;
		cout<<"O won\n";
		continue;
	}
	if(dcnt>0)
		draw=false;
	FOR(i,0,4){
		if(xcnt_r[i]==4||(xcnt_r[i]==3&&tcnt_r[i]==1)){
			CASE;
			cout<<"X won\n";
			win_flag=true;
			break;
		}
		if(xcnt_c[i]==4||(xcnt_c[i]==3&&tcnt_c[i]==1)){
			CASE;
			cout<<"X won\n";
			win_flag=true;
			break;
		}
		if(ocnt_r[i]==4||(ocnt_r[i]==3&&tcnt_r[i]==1)){
			CASE;
			cout<<"O won\n";
			win_flag=true;
			break;
		}
		if(ocnt_c[i]==4||(ocnt_c[i]==3&&tcnt_c[i]==1)){
			CASE;
			cout<<"O won\n";
			win_flag=true;
			break;
		}
	}
	if(win_flag)
		continue;
	if(draw){
		CASE;
		cout<<"Draw\n";
		continue;
	}
	CASE;
	cout<<"Game has not completed\n";
}

#ifdef DEBUG
  fprintf(stderr, "Total time = %.2lf sec\n", (double)(clock() - tmp_start) / CLOCKS_PER_SEC);
#endif

return 0;
}
