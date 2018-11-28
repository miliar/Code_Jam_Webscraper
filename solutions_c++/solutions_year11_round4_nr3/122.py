#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#define N 1300000

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long ul;
typedef unsigned short us;
typedef unsigned char uc;

int P[100000], NP=0;
char siv[N];

bool enuf(int p,int k,ull n) { for(int i=0;i<k;i++) n/=p; return n; }

main()
{
  memset(siv,1,sizeof(siv));
  for(int i=2;i<N;i++) { if (siv[i]) { P[NP++]=i; for(int j=i+i;j<N;j+=i) siv[j]=0; } }

  int cases;
  cin >> cases;
  for(int loop=1; loop<=cases; loop++)
  {
    ull n; cin >> n;
    printf("Case #%d: ",loop);

    ull t=(n>1);
    for(int k=2;(1ULL<<k)<=n;k++)
    {
      int a=0, b=NP;
      while(b-a>1) { int c=(b+a)/2; if (enuf(P[c],k,n)) a=c; else b=c; }
      t += b;
    }
    printf("%llu\n",t);
  }
}
