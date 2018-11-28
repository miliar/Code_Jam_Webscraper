#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

long long  n,l,h;
long long  G[10000];
long long  L[10000];
   vector<long long > VV;

long long gcd(long long a, long long b) {
  if (a<b) return gcd(b,a);
  if (b==0) return a;
  return gcd(b,a % b);
}
int cp(long long a, long long b , long long c) // a*b > c;
{
   long long ax = a >> 30;
   long long ay = a - ( ax << 30);
   long long bx = b >> 30;
   long long by = b - (bx << 30);
   if (ax*bx) return true;

   long long tx = ax*by + bx * ay + (ay*by >> 30);
   long long ty = ay*by - (ay*by >> 30 << 30);
   long long cx = c >> 30;
   long long cy = c -(cx << 30);
   return (tx>cx || (cx==tx && ty>cy));


}

long long limlca( long long a, long long b, long long lim) {
  if (a>lim || b>lim) return lim+1;
  long long e = gcd(a,b);
  a = a/e;
  if (cp(a,b,lim)) return lim+1;
  return a * b;

}
vector<pair<long long ,int> > getfactor(long long a) {
  long long  pri = 2;
  vector< pair<long long,int> > WW; WW.clear();
  while (a>1) {
    if (a % pri ==0) {
      int p =0;
      while (a % pri ==0) {
        p++; a /= pri;
      }
      WW.push_back(make_pair(pri,p));
    }
    pri++;
    if (pri*pri>a) break;
  }
  if (a>1) {
    WW.push_back(make_pair((long long )a, 1));
  }
 // for (int i = 0 ; i < WW.size(); i++)
 //   cout << (WW[i].first) <<" "<<(WW[i].second) << endl;
  return WW;
}

    long long best;
  vector< pair<long long , int> > VPA ;
  long long low, high;
  void work(long long now, int id) {
     if (id == VPA.size()) {
       if (low <= now && now <=high && now <= best)
         best = now;
       return ;
     }
     long long nxt = now;
     for (int i = 0 ; i <=  VPA[id].second; i++) {
        work(nxt,id+1);
        nxt *= VPA[id].first;
     }
  }
long long check(long long t_low, long long t_high, long long a, long long b) {
  if (a>t_high) return 0;
  if (b % a) return 0;
  // cout <<"Checking"<< low<<","<<high<<","<<a<<","<<b<<","<<endl;
  long long k = b/a;
  if (b==a) {
    if (t_low<=a && a<=t_high) return a; else return 0;
  }
  VPA = getfactor(k);
best = b+ 1;
  low = t_low; high = t_high;
  work(a,0);
  if (best<=b) return best; else
     return 0;
}
long long  work(vector<long long > V, long long  l, long long  h) {
  sort(V.begin(),V.end());
  int n = V.size();
  L[0] = (long long ) V[0];
  for (int i = 1; i< n; i++)
    L[i] = limlca(L[i-1],V[i], h);
  G[n-1] = (long long )V[n-1];
  for (int i = n-2; i>=0; i--)
    G[i] = gcd(G[i+1],V[i]);
  int t;
  if (t = check(l,h,1,G[0])) return t;
  for (int i = 0; i<n-1; i++)
    if (t= check(l,h,L[i],G[i+1])) return t;
  for (t= l; t<=h; t++)
     if (t % L[n-1] ==0) return t;
  return 0;
}

void init()
{

    VV.clear();
    scanf("%d%d%d",&n,&l,&h);
    for (int k =0;k<n;k++) {
        long long  t;
        scanf("%lld",&t);
        VV.push_back(t);
    }
}

int main()
{
    FILE *tin=freopen("C-small-attempt1.in", "r", stdin);
    FILE *cin=freopen("c.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    for (int tnum = 1; tnum<= T; tnum++) {
        init();
        long long tmp = work(VV,l,h);
        if (tmp)
            printf("Case #%d: %lld\n",tnum,tmp);
        else
            printf("Case #%d: NO\n",tnum);
    }
}
