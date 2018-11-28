#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

long long  GCD[10000];
long long  LCA[10000];
long long gcd(long long a, long long b) {
  if (a<b) return gcd(b,a); 
  //a>=b;
  if (b==0) return a;
  return gcd(b,a % b);
}
int cp(long long a, long long b , long long c) // a*b > c;
{
   //ax*2^31 + ay
   //bx*2^31+ by;
   long long ax = a >> 30;
   long long ay = a - ( ax << 30);
   long long bx = b >> 30;
   long long by = b - (bx << 30);
   //tm = ax*bx*2^60 + (ax*by+bx*ay)*2^30 + ay*by
   if (ax*bx) return true;
   long long tx = ax*by + bx * ay + (ay*by >> 30);
   long long ty = ay*by - (ay*by >> 30 << 30);
   long long cx = c >> 30;
   long long cy = c -(cx << 30);
   return (tx>cx || (cx==tx && ty>cy));
   
   
}

long long limlca( long long a, long long b, long long lim) {
  if (a>lim || b>lim) return lim+1;
  long long G = gcd(a,b);
  a = a/G;
  if (cp(a,b,lim)) return lim+1;
  return a * b;
  // a * b > lim return lim+1 // 10^16 
  
}
long long check(long long low, long long high, long long a, long long b) {
 // cout <<"Checking"<< low<<","<<high<<","<<a<<","<<b<<","<<endl;
  if (b % a) return 0;
  for (long long t = low; t <=high; t++) {
    if (b % t ==0 && t % a ==0) return t;
  }
  return 0;
}
long long  work(vector<long long > V, int l, int h) {
  sort(V.begin(),V.end());
  int n = V.size();
  LCA[0] = (long long ) V[0];
  for (int i = 1; i< n; i++) 
    LCA[i] = limlca(LCA[i-1],V[i], h);
  GCD[n-1] = (long long )V[n-1];
  for (int i = n-2; i>=0; i--)
    GCD[i] = gcd(GCD[i+1],V[i]);
  //  cout << n << endl;
 // for (int i = 0 ; i < n ; i++)
 //   cout << LCA[i] <<" ";
 // cout << endl;
  
 //   for (int i = 0 ; i < n ; i++)
 //   cout << GCD[i] <<" ";
 // cout << endl;
  int t;
  if (t = check(l,h,1,GCD[0])) return t;
  for (int i = 0; i<n-1; i++)
    if (t= check(l,h,LCA[i],GCD[i+1])) return t;
  for (t= l; t<=h; t++)
     if (t % LCA[n-1] ==0) return t;
  cout <<"NO"<< endl;
  return 0;
}
int main()
{
  int tt;
  cin >> tt;
  for (int i = 1; i<= tt; i++) {
    cout <<"Case #"<<i<<": ";
    int n,l,h;
    cin >> n>>l>>h;
    vector<long long > VV;
    VV.clear();
    //cout << "Got n "<<n <<endl;
    for (int k =0;k<n;k++) {
      long long  t;
      cin >> t ; //cout <<"T"<<t<<endl;
      VV.push_back(t);
    }
    long long tmp = work(VV,l,h);
    if (tmp) cout << tmp << endl;
  }
}
