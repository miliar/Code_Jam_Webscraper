#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <numeric> 
#include <ctime>
#include <algorithm>
using namespace std;  
  
typedef vector<int> vi;  
typedef vector<vi> vvi;  
typedef vector<string> vs;  
typedef vector<vs> vvs; 
#define pb push_back  
#define sz(v) ((int)(v).size()) 


int main()
{
  int i,j,k,n,N;
  scanf("%d",&N);
  for(n=1;n<=N;n++)
  {
    printf("Case #%d: ",n);
    int s; scanf("%d",&s);
    vector<long long> A(s),B(s);
    for(j=0;j<s;j++) scanf("%lld",&A[j]);
    for(j=0;j<s;j++) scanf("%lld",&B[j]);
    sort(A.begin(),A.end());
    sort(B.begin(),B.end());
    reverse(B.begin(),B.end());
    long long som=0;
    for(j=0;j<s;j++)
      som+=A[j]*B[j];

    printf("%lld\n",som);
  }

  return 0;
}

