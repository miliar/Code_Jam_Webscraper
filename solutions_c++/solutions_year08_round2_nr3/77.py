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

using namespace std;

#define MAX 5010

int n_tests,test;
int i,j,k;
int K,n;
int d[MAX],pos;
int card[MAX],next[MAX],prev[MAX];

int main()
{
  cin >> n_tests;
  for_to(test,1,n_tests)
  {
    cin >> K;    
    cin >> n;
	cout << "Case #" << test << ":";
    for_to(i,1,K)
	{
	  card[i]=0;
	  prev[i]=i-1;
	  next[i]=i+1;
	  if (i==1)
	  {
	    prev[i]=K;
	  }
	  if (i==K)
	  {
	    next[i]=1;
	  }
	}
	next[0]=1;
    pos=0;
	for_to(i,1,K)
	{
	  for_to(j,1,i)
	  {
	    pos=next[pos];
	  }
	  card[pos]=i;
	  next[prev[pos]]=next[pos];
	  prev[next[pos]]=prev[pos];
	}	 
    for_to(i,1,n)
	{
	  cin >> pos;
	  cout << " " << card[pos] ; 
	}
	cout << endl;
  }
  return 0;
}

