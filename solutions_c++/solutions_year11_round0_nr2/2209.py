/*
***************************************************************
Author           : Ishan Dutta
Email            : ishandutta2007@gmail.com
Facebook         : http://www.facebook.com/ishan.dutta
Blog             : tessellationsoftechnology.wordpress.com
Topcoder Handle  : Ishandutta2007
Codeforces Handle: ishandutta2007
Codechef Username: ishandutta2007
Spoj Username    : ishandutta2007
UVA Username     : ishandutta2007
***************************************************************
*/
/* ***************************************************************** */
// \_/\_/\_/\_/\_/\_/\_/\_/---Headers---\_/\_/\_/\_/\_/\_/\_/\_/
/* ***************************************************************** */

//C headers
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<ctime>
#include<cctype>
#include<cassert>
#include<climits>
#include<cerrno>
#include<cfloat>
#include<ciso646>
#include<clocale>
#include<csetjmp>
#include<csignal>
#include<cstdarg>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cwchar>
#include<cwctype>

//containers
#include<vector>
#include<list>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<complex>
#include<string>
#include<stack>
#include<bitset>
#include<istream>
#include<valarray>

//IOs
#include<iostream>
#include<sstream>
#include<iomanip>
#include<fstream>
#include<exception>
#include<ios>
#include<iosfwd>
#include<ostream>
#include<iterator>
#include<stdexcept>
#include<streambuf>

//algorithm & miscellaneous
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<limits>
#include<locale>
#include<memory>
#include<new>

/* ****************************************************************** */
// \_/\_/\_/\_/\_/\_/\_/---Frequently used macros---\_/\_/\_/\_/\_/\_/\_/
/* ****************************************************************** */

#define MOD 1000000007
#define INF 1000000000

/* ****************************************************************** */
// \_/\_/\_/\_/\_/\_/\_/\_/\_/---Shorthands---\_/\_/\_/\_/\_/\_/\_/\_/\_/
/* ****************************************************************** */

#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair

#define SZ(c) (c).size()
#define reset(x) memset((x),0,sizeof(x));
#define negset(x) memset((x),-1,sizeof(x));
#define set(x) memset((x),1,sizeof(x));

#define ALL(x) (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define REVERSE(c) reverse(ALL(c))

#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define REP(i,n) FOR(i,0,(n-1))

#define FORD(i,a,b) for(int i=(int)(a);i>=(int)(b);i--)
#define REPD(i,n) FOR(i,(n-1),0)


#define tst int t;scanf("%d",&t);while(t--)
#define s(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)

#define p(x) printf("%d",x)
#define pl(x) printf("%lld",x)
#define ps(x) printf("%s",x)

#define pn(x) printf("%d\n",x)
#define pln(x) printf("%lld\n",x)
#define psn(x) printf("%s\n",x)

#define sp system("PAUSE")

/* ****************************************************************** */
// \_/\_/\_/\_/\_/---Fast IO using getchar_unlocked---\_/\_/\_/\_/\_/
/* ****************************************************************** */

using namespace std;
/* ****************************************************************** */
// \_/\_/\_/\_/\_/\_/---Actual Code Starts Here---\_/\_/\_/\_/\_/\_/
/* ****************************************************************** */
char adjopp[500][500];
char adjcom[500][500];
int main(){  
    freopen ("B-large.in", "r", stdin);
    freopen ("file.out", "w", stdout);
    int T;s(T);REP(t,T){
      int C;s(C);
      REP(i,500)REP(j,500)adjopp[i][j]=adjcom[i][j]=0;
      
      char scom[C][5];
      memset(scom,0,sizeof(scom));
      REP(i,C){ss(scom[i]);adjcom[scom[i][0]][scom[i][1]]=adjcom[scom[i][1]][scom[i][0]]=scom[i][2];}
      
      int D;s(D);
      char sopp[D][4];
      memset(sopp,0,sizeof(sopp));
      REP(i,D){ss(sopp[i]);adjopp[sopp[i][0]][sopp[i][1]]=adjopp[sopp[i][1]][sopp[i][0]]=1;}
      
      int N;s(N);
      char text[1010];ss(text);
      
      vector< char >stak;
      stak.clear();
      int l=strlen(text);
      FOR(i,0,l-1){
        if(stak.size()==0){stak.PB(text[i]);continue;}
        int u=stak[stak.size()-1];
        if(adjcom[u][text[i]]!=0){
            stak.pop_back();
            stak.PB(adjcom[u][text[i]]);
        }
        else{
          bool flag=false;
          for(int j=0;j<stak.size();j++){
            if(adjopp[stak[j]][text[i]]==1){flag=true;break;}
          }
          if(flag){
            do{
              stak.pop_back();
            }while(stak.size());
          }
          else stak.PB(text[i]);
        }
      }
      char ans1[1010];
      ans1[0]='[';
      int j=1;
      REP(i,stak.size()){
         ans1[j]=stak[i];j++;
         ans1[j]=',';j++;
         ans1[j]=' ';j++;
      }
      if(stak.size()>0)j-=2;
      ans1[j]=']';
      ans1[j+1]='\0';
      printf("Case #%d: %s\n",t+1,ans1);
    }
  return 0;
}

