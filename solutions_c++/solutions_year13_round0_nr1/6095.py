#include <algorithm> 
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctype.h>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector> 
using namespace std;

typedef long long             ll;
typedef vector<int>           vi;
typedef pair<int, int>        ii;
typedef vector<ii>            vii;
typedef map<int, int>         mii;
typedef set<int>              si;
typedef map<string, int>      msi;
typedef vector<bool>          vb;
typedef long double           ld;

#define rep(i, a, b)    for (int i = int(a); i <= int(b); i++)
#define repd(i, a, b)   for (int i = int(a); i >= int(b); i--)
//#define TR(c, it)       for (typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define pb              push_back
#define mp              make_pair
#define SIZE(c)         (int((c).size()))
#define LET(x, a)       __typeof(a) x = (a)
#define FOR(x, a, b)    for(LET(x,a); x!=(b); x++)
#define TR(cnt, it)     FOR(it, (cnt).begin(), (cnt).end())
 
#define vsort(v)        sort(v.begin(), v.end())
#define REDIRECT_INPUT  freopen("input_1.txt", "r", stdin)
#define REDIRECT_OUTPUT freopen("output_1.txt","w", stdout);
#define INF 2147483647  // 2^31-1

int arr[4][4],xcount,ocount,tcount; 
int case1 = 1;
int dotcount,flag;
string str;
int main()
{
 int T;
 REDIRECT_INPUT;
 REDIRECT_OUTPUT;
  cin>>T;
 while(T--)
 {
	flag = 1;
	dotcount =0 ;
	rep(i,0,3)
	{
	cin>>str;
	 rep(j,0,3)
	 {
	 arr[i][j] = str[j];
	if(arr[i][j]=='.')
	dotcount++;
    }
    }
	rep(i,0,3)
	{
		xcount = ocount = tcount = 0;
	rep(j,0,3)
	{
		if(arr[i][j] == 'X')
		xcount++;
		if(arr[i][j] == 'O')
		ocount++;
		if(arr[i][j] == 'T')
		tcount++;
	}	
	//printf("%d %d \n", xcount,tcount);
        if(xcount + tcount == 4)
        {
         printf("Case #%d: X won\n",case1);
         flag = 0;
         break;
	    }
        if(ocount + tcount == 4)
        {
        printf("Case #%d: O won\n",case1);
        flag =0; 
        break;
	    }
    }
    xcount = ocount = tcount = 0;
    if(flag){ 
    rep(j,0,3)
    {
		xcount = ocount = tcount = 0;
	rep(i,0,3)
	{
		if(arr[i][j] == 'X')
		xcount++;
		if(arr[i][j] == 'O')
		ocount++;
		if(arr[i][j] == 'T')
		tcount++;
	}	
        if(xcount + tcount == 4)
        {
         printf("Case #%d: X won\n",case1);
         flag = 0;
         break;
	    }
        if(ocount + tcount == 4)
        {
        printf("Case #%d: O won\n",case1);
        flag =0;
        break; 
	    }  
 }
}
     xcount = ocount = tcount = 0;
     if(flag){
     rep(i,0,3)
     {
     if(arr[i][i] == 'X')
		xcount++;
		if(arr[i][i] == 'O')
		ocount++;
		if(arr[i][i] == 'T')
		tcount++;
	}	
        if(xcount + tcount == 4)
        {
         printf("Case #%d: X won\n",case1);
         flag = 0;
	    }
        if(ocount + tcount == 4)
        {
        printf("Case #%d: O won\n",case1);
        flag =0; 
      } 
  }
     xcount = ocount = tcount = 0;
     if(flag)
     {
     rep(i,0,3)
     {
     if(arr[i][3-i] == 'X')
		xcount++;
		if(arr[i][3-i] == 'O')
		ocount++;
		if(arr[i][3-i] == 'T')
		tcount++;
	}	
        if(xcount + tcount == 4)
        {
         printf("Case #%d: X won\n",case1);
         flag = 0;
	    }
        if(ocount + tcount == 4)
        {
        printf("Case #%d: O won\n",case1);
        flag =0; 
	    } 
	  }  
      if(flag)
      {
		  if(dotcount)
		  printf("Case #%d: Game has not completed\n",case1);
		  else
		  printf("Case #%d: Draw\n",case1);
      }
      case1++; 
  }
}
