#include <iostream>
#include <queue>

using namespace std;

int r,k,n,tc;
int ar[1010];
long long ar2[1010];
int ar3[1010];

long long ans;

int main()
{
 cin >> tc;
 int i;
 for(int i=0;i<tc;i++)
 {
  cout << "Case #" << i+1 <<": ";
  ans = 0;
  cin >> r >> k >> n;
  
//  if(n!=1000)
  for(int ii=0;ii<n;ii++)
  {
   cin >> ar[ii];
  }
//  else
//  for(int ii=0;ii<n;ii++) ar[ii] = 1000000000;
  
  for(int ii=0;ii<n;ii++)
  {
   ar2[ii] = (long long) ar[ii];
   ar3[ii] = (ii+1)%n;
   while(ar2[ii]+ar[ar3[ii]]<=k && ar3[ii] !=ii) 
   {
    ar2[ii] += (long long) ar[ar3[ii]];
    ar3[ii]++; if(ar3[ii]==n) ar3[ii] = 0;
   }
  }
  
  int nw = 0;
  for(int ii=0;ii<r;ii++)
  {
   ans += ar2[nw];
   nw = ar3[nw];
  }
  
  cout << ans << endl;
 }
}
