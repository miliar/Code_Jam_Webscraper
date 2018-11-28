#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define MST(a,b) (memset(a,b,sizeof(a)))
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;


#define MOD 10009

char S[131072];
int K, N, L;
char wd[32][1024];
int cnt[32][32];
int pick[32];
int sum;
int V[32];
void F()
{
     
     int i, j;
   /*  for(i = 0; i < 26; ++i)
         for(j = 0; j < N; ++j)
             V[i] += pick[j] * cnt[j][i];*/
             
     int tmp = 1;
     for(i = 0; S[i]; i++)
     {
         if(S[i] == '+')
         {
             sum += tmp;
             tmp = 1;
         }
         else
         {
             tmp = (tmp * V[S[i]-'a']) % MOD;
         }
     }
     sum = (sum + tmp) % MOD;

 }
void dfs(int p)
{
     int i, j;
     if(p == L)
     {
         F();
         return;
     }
     for(i = 0; i < N; ++i)
     {
         //pick[i]++;
         for(j = 0; j < 26; ++j)
             V[j] += cnt[i][j];
         dfs(p + 1);
         for(j = 0; j < 26; ++j)
             V[j] -= cnt[i][j];
     }
}
int main()
{
	freopen("B_S2.in","r", stdin);
	freopen("B_S2.out", "w", stdout);

    int t;
	scanf("%d", &t);
    int Case;
     
     
    int i, j, k;
     int res[32];
	for(int Case = 1; Case <= t; Case++)
	{
		scanf("%s", S);
		scanf("%d", &K);
		scanf("%d", &N);
		for(i = 0; i  < N; ++i) scanf("%s", wd[i]);
	    memset(cnt, 0, sizeof(cnt));
	    for(i = 0; i < N; ++i)
	      for(j = 0; wd[i][j]; ++j)
	          cnt[i][wd[i][j]-'a']++;
        for(L =  1; L <= K; ++L)
        {
            memset(pick, 0, sizeof(pick));
            sum = 0;
            memset(V, 0, sizeof(V));
            dfs(0);
            res[L] = sum;
        }
		printf("Case #%d:", Case);
		for(L = 1; L <= K; ++L) printf(" %d", res[L]);
		printf("\n");
        
        //fflush(stdout);

	}


	return 0;
}
