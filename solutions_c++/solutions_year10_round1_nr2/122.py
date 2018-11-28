#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std; typedef unsigned long ul; typedef long long ll;
typedef unsigned long long ull;

int D,I,M,n;

int smooth(vector<int>&a) { for(int i=1;i<a.size();i++) if(abs(a[i]-a[i-1])>M) return 0; return 1;}

int dist(int x, int y)
{
  int m=abs(x-y);
  if (m <= M) return 0; if (M==0) return m;
  int r=m%M;
  return D <? ( m-M ) <? ( m/M*I - I + r) <? ( (m-1)/M*I ) ;
}

int main()
{
int cases;

cin >> cases; getchar();

for(int loop=1;loop<=cases;loop++)
{
  cin >> D>>I>>M>>n;
  vector<int> a(n);
for(int i=0;i<n;i++) cin >> a[i];

  printf("Case #%d: ",loop);
  int opt = 10000000;

  if (smooth(a)) {puts("0"); continue;}
  if (n==2) { printf("%d\n", dist(a[0],a[1])); continue; }
  // n==3
  opt = D+dist(a[0],a[2]);

  for(int i=0;i<256;i++)
  {
    opt <?= abs(i-a[1]) + dist(a[0],i) + dist(a[2],i);
  }

  printf("%d",opt);
  puts("");
  fflush(stdout);
}

}
