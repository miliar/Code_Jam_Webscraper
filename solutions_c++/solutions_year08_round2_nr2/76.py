#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <ctype.h>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>

#define for_to(i,j,k) for(i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)
#define wipe(a,x) memset(a,x,sizeof(a))
#define gcd __gcd
#define huge long long
#define MAX 1123456
#define id(x) (x-A)

using namespace std;

huge n_tests,test;
huge i,j,k;
huge p[MAX],rank[MAX];
huge primes[MAX];
huge n_primes=0;
huge A,B,P,q,ans;

huge find_set(huge i)
{
  if (p[i]!=i)
  {
    p[i]=find_set(p[i]);
  }
  return p[i];
}

void Union(huge i,huge j)
{
  huge x,y;
  x=find_set(i);
  y=find_set(j);
  if (x==y) return;
  //cout << x << " *** " << y << endl;
  if (rank[x]>rank[y])
  {
    p[y]=x;
  }
  else
  {
    p[x]=y;
  }
  if (rank[x]==rank[y]) ++rank[y];
}

int main()
{
  cin >> n_tests;
  for_to(i,0,MAX-1)
  {
    p[i]=1;
  }
  for_to(i,2,MAX-1)
  {
    if (p[i])
	{
	  primes[n_primes++]=i;
	  for (j=i*i; j<MAX; j+=i)
	  {
	    p[j]=0;
	  }
	}
  }
  //cout << n_primes << endl;
  //for_to(i,0,10)
   //cout << primes[i] << endl;
  for_to(test,1,n_tests)
  {
    //cout << "test " << test << endl;
    cin >> A >> B >> P;
    for_to(i,A,B)
	{
	  rank[id(i)]=0;
	  p[id(i)]=id(i);
	}
	//cout << "ok" << endl;
    for (i=0; i<n_primes; ++i)
	{
	  q=primes[i];
	  if (q>B-A) break;
	  if (q<P) continue;
	  if (A%q==0)
	  {
	    j=A;
	  } 
	  else
	  {
	    j=( (A+q)/q ) * q;
	  }
	  //cout << "A,j=" << A << " "  << j << endl;
	  for (k=j+q; k<=B; k+=q)
	  {
	    //cout << j << "--" << k << endl;
	    Union(id(j),id(k));
		//cout << "out" << endl;
	  }
	}
	//cout << "aa" << endl;
	ans=0;
	for_to(i,A,B)
	{
	  if (p[id(i)]==id(i))
	  {
	    ++ans; 
	  }
	}
	cout << "Case #" << test << ": "  << ans << endl;
	
  }
  return 0;
}

