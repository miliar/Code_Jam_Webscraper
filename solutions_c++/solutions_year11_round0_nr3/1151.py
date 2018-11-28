#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<utility>
#include<set>
#include<sstream>
#define fr(a,b,c) for (a=b;a<=c;a++)
#define frr(a,b,c) for (a=b;a>=c;a--)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define oo 1000111222
using namespace std;
typedef long long ll;

vector <int> a;

int main()
{
   int test,it,i,n,x;
   cin >> test;
   fr(it,1,test)
   {
      cin >> n;
      int s=0,sum=0,m=1000000;
      fr(i,1,n) 
      {
         scanf("%d",&x); 
         sum+=x;
         m=min(m,x);
         s^=x;
      } 
      cout << "Case #" << it << ": ";
      if (s) cout << "NO" << endl;
      else cout << sum-m << endl;
   }  
   return 0;
}
