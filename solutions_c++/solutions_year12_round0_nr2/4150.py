#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <map>
#include <set>
using namespace std;
//BEGINTEMPLATE_BY_TOKENS
typedef long long       LL;
typedef long double     LD;
typedef unsigned long long       UL;
typedef pair<long,long> PL;

//FUN_ _
#define SIZE(X) ((int)(X.size()))          //NOTES:SIZE(
#define L(X) ((int)(X.length()))      //NOTES:LENGTH(
#define MAX(i,j) (i)>(j)?(i):(j)
#define MIN(i,j) (i)<(j)?(i):(j)
#define FOR(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define REP(i,a) for((i)=0;(i)<(a);(i)++)
#define MEM(m,i) memset((m),(i),SZ(m))
#define PB(x,y) (x).push_back(y)
#define MP(x,y) make_pair(x,y)
#define INF 1000000000000
#define EPI 1e-7
const int MaxMatrixSize=40;
using namespace std;
template<class T> inline T checkMod(T n,T m) {return (n%m+m)%m;}          //NOTES:checkMod(
template<class T> inline T gcd(T a,T b)        //NOTES:gcd(
  {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)             //NOTES:lcm(
  {if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline void showMatrix(int n,T A[MaxMatrixSize][MaxMatrixSize])//NOTES:showMatrix(
  {for (int i=0;i<n;i++){for (int j=0;j<n;j++)cout<<A[i][j];cout<<endl;}}

//@niteshvishnoi.................//
int main()
{
    int test,cse=1;
   	freopen("input.txt","r",stdin);
				freopen("output2.txt","w",stdout);
    scanf("%d",&test);
    while(cse<=test)
    {
					  int n,s,p,i,j;
					  scanf("%d%d%d",&n,&s,&p);
					  int a,tot;
					//  sort(tot,tot+n);
					  int rem=s,cnt=0;
					  REP(i,n)
					  {
			        scanf("%d",&tot);
											a = tot/3;
           if(a>=p || tot>27 || p==0)
              ++cnt;
           else if(tot==1)
											{
												  if(p<=1)
														  ++cnt;
											}		  
           else if(tot>1)
           {
											     if(tot%3==0)
                {
															    if( (a + 1)== p && rem>0)
															    {
																 		   ++cnt;
																	     rem--;
															    }
											     }
											     else 
											     {
												       if(a>= (p - 1))
										            ++cnt;
										         else if(tot%3==2 && (a + 2) >=p && rem>0)   
										         {
																			   ++cnt;
																			   rem--;
																			}
											     }
							     }
							}
							printf("Case #%d: %d\n",cse++,cnt);
				}
   // system("pause");
    return 0;
}
