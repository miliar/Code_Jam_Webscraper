#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> A;
int p;
int M[147][147];

int rataj(int kde, int kolko)
{
  //printf("@%d %d\n",kde,kolko);
  if(kde==A.size() && kolko==0) return 0;
  else if(kde==A.size()) return -10000;
  else if(kolko<0) return -1000;
  if(M[kde][kolko]!=-1000000000) return M[kde][kolko]; 
  int x=A[kde];
  int pom=x/3;
  if(x%3!=0) pom+=1;
  int vys=-10000;
  if(pom>=p) vys=max(vys,rataj(kde+1,kolko)+1);
  pom=x/3;
  if(x%3==2) pom+=2;
  if(x%3==1) pom+=1;
  if(x%3==0) pom+=1;
  if(x>=2 && x<=28 && pom>=p) vys=max(vys,rataj(kde+1,kolko-1)+1);
  vys=max(vys,rataj(kde+1,kolko));
  if(x>=2 && x<=28) vys=max(vys,rataj(kde+1,kolko-1));
  M[kde][kolko]=vys;
  return vys;
}

int main()
{
  int t;
  scanf("%d ",&t);
  for(int i1=1; i1<=t; i1++)
  {
    int n,s;
    scanf("%d %d %d ",&n,&s,&p);
    A.clear(); A.resize(n);
    for(int i=0; i<n; i++) scanf("%d ",&A[i]);
    for(int i=0; i<n+42; i++)
      for(int j=0; j<n+42; j++) M[i][j]=-1000000000;
    int rek=rataj(0,s);
    printf("Case #%d: %d\n",i1,rek);
  }
return 0;
}