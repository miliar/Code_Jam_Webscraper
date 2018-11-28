#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <vector>
#include <list>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <numeric>
#include <bitset>
#include <complex>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
using namespace std;

#define lp for(;;)
#define repf(i,a,b) for (int i=(a);i<(b);++i)
#define rep(i,n) repf(i,0,n)
#define ft(i,a,b) for (int i=(a);i<=(b);++i)
#define fdt(i,a,b) for (int i=(a);i>=b;--i)
#define feach(e,s) for (typeof((s).begin()) e=(s).begin();e!=(s).end();++e)
#define fsubset(subset,set) for (int subset=set&(set-1);subset;subset=(subset-1)&set)
#define forin(i,charset) for (cstr i=charset;*i;i++)
#define whl while
#define rtn return
#define fl(x,y) memset((x),sizeof(x),char(y))
#define clr(x) fl(x,char(0))
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define sz(x) (int((x).size()))
#define all(x) (x).begin(),(x).end()
#define srt(x) sort(all(x))
#define uniq(x) srt(x),(x).erase(unique(all(x)),x.end());
#define pr pair
#define que queue
#define prq priority_queue
#define itr iterator
#define sf scanf
#define pf printf
#define pdb(prcs,x) printf("%."#prcs"f",(abs(x)<1e-##prcs)?0.0:x)
#define input(in) freopen(in,"r",stdin)
#define output(out) freopen(out,"w",stdout)

typedef long long int LL;
typedef pr<int,int> pii;
typedef pr<LL,LL> pll;
typedef pr<double,double> pdd;
typedef pr<string,int> psi;
typedef map<int,int> mii;
typedef map<string,int> msi;
typedef map<char,int> mci;
typedef set<int> si;
typedef set<string> ss;
typedef que<int> qi;
typedef prq<int> pqi;
typedef vector<int> veci;
typedef vector<bool> vecb;
typedef vector<string> vecs;
typedef vector<double> vecdb;

const int oo=(~0u)>>1;
const LL lloo=(~0ull)>>1;
const double dboo=1e+20;
const double eps=1e-8;
const double pi=acos(-1.0);
const int MOD=1000000007;

char maps[5][5];
int T;
int checkdia()
{
	 int j=1;
	 int dia=maps[1][1];
	 if(dia=='T')
		  dia=maps[2][2];
	 if(dia=='.')
		  return 0;
	 ft(i,2,4)
	 {
		  j++;
		  if(maps[i][j]==dia||maps[i][j]=='T')
			   continue;
		  return 0;
	 }
	 return dia;
}
int checkinvdia()
{
	 int j=4;
	 int dia=maps[1][4];
	 if(dia=='T')
		  dia=maps[2][3];
	 if(dia=='.')
		  return 0;
	 ft(i,2,4)
	 {
		  j--;
		  if(maps[i][j]==dia||maps[i][j]=='T')
			   continue;
		  return 0;
	 }
	 return dia;
}
void solve()
{
	 int emt=0;
	 int flag=-1;
	 ft(i,1,4)
	 {
		  flag=maps[i][1];
		  while(flag=='T')
			   flag=maps[i][2];
		  if(flag == '.')
		  {			   
			   emt=1,flag=-1;
			   continue;
		  }
		  ft(j,2,4)
		  {
			   if(maps[i][j]==flag||maps[i][j]=='T')
					continue;
			   if(maps[i][j]=='.')
					emt=1;
			   flag=-1;
			   break;
		  }
		  if(flag!=-1)
		  {	   pf("%c won\n",flag);return;}
		
	 }

	 ft(i,1,4)
	 {
		  flag=maps[1][i];
		  while(flag=='T')
			   flag=maps[2][i];
		  if(flag == '.')
		  {			   
			   emt=1,flag=-1;
			   continue;
		  }
		  ft(j,2,4)
		  {
			   if(maps[j][i]==flag||maps[j][i]=='T')
					continue;
			   if(maps[j][i]=='.')
					emt=1;
			   flag=-1;
			   break;
		  }
		  if(flag!=-1)
		  {	   pf("%c won\n",flag);return;}
	 }
	 
	 if(flag!=-1)
		  return ;
	 if(checkdia())
	 {	  pf("%c won\n",checkdia());return;}
	 else if(checkinvdia())
	 {		  pf("%c won\n",checkinvdia());return;};
	 if(emt)
		  pf("Game has not completed\n");
	 else
		  pf("Draw\n");
}
int main(int argc, char *argv[])
{
	 sf("%d",&T);
	 ft(tt,1,T)
	 {
		  ft(i,1,4)
			   sf("%s",&maps[i][1]);
		  pf("Case #%d: ",tt);
		  solve();
	 }
	 return 0;
}
