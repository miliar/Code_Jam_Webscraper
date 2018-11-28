#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int T, tc;
bool komp[1000002];
vector<long long> v;
void sieve() {
     for (int i=2;i<=1000000;i++) {
         if (komp[i] == 0) {
                     for (int j=i+i;j<=1000000;j+=i) komp[j] = 1;
                     }
         }
     }

int main() {
    sieve();
    freopen("res.out","w",stdout);
    freopen("res.txt","r",stdin);
long long lcm = 1;
int worst= 1;
int best = 0;
for (long long i=2 ; i<= 1000000;i++) {
    if (komp[i] == 0) {
                worst--;
                long long apa = i*i;
                while (1000000000000ll >= apa) {
                //      if (apa!=i)
                      v.push_back(apa);
                      apa*=i;
                      }
                }
    }
sort(v.begin(),v.end());
scanf("%d",&T);
for (int ii = 1;ii<=T;ii++) {
long long X;
cin>>X;
    printf("Case #%d: %d\n",ii,lower_bound(v.begin(),v.end(),X+1) - v.begin() + (bool) (X-1));
}

}
