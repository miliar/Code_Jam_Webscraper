#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <utility>
#include <set>
#include <queue>
#include <sstream>
#define fr(a,b,c) for (a=b;a<=c;a++)
#define frr(a,b,c) for (a=b;a>=c;a--)
#define mp make_pair
#define pii pair<int,int>
#define pb push_back
#define F first
#define S second
#define oo 1000111222
#define lloo 1LL << 60
using namespace std;

int p[80000],P,d[80000],b[1000100];
long long n;

void prime()
{
    int i,j;
    fr(i,2,997)
      if (!b[i])
      {
         j=i*i;
         while (j<=1000000)
         {
            b[j]=1;
            j+=i;   
         }
      }
    fr(i,2,1000000)
      if (!b[i]) p[++P]=i;
}

int main()
{
    freopen("clarge.in","r",stdin); freopen("clarge.out","w",stdout);
    int test,it,i,re;
    cin >> test;
    prime();
    fr(it,1,test)
    {
       cout << "Case #" << it << ": ";
       cin >> n;
       re=0;
       fr(i,1,P)
       {
          if (p[i]>n) break;
          int cnt=0;
          long long nn=n;
          while (nn>=p[i]) nn/=p[i], ++cnt;
          re+=cnt-1;
       }
       if (n>1) re++;
       cout << re << endl;
       //cerr << it << endl;
    }
    //while (1);
    return 0;
}
