#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
#define LL long long
vector<LL> v;
LL gcd (LL a, LL b){
    if (b == 0) return a;
    return gcd(b,a%b);
}
int tc,n;
LL temp;
int main(){
 scanf("%d",&tc);
 for (int ti = 1; ti <= tc; ti++){
     v.clear();
     scanf("%d",&n);
     for (int i = 1; i <= n; i++){
         scanf("%I64d",&temp);
         v.push_back(temp);
     }    
     sort(v.begin(),v.end());
     LL a;
     for (int i = 1; i < v.size(); i++){
         if (i == 1) a = v[i]-v[i-1];
         else a = gcd(a,v[i]-v[i-1]);    
     }
     if ((v[0]%a) == 0) printf("Case #%d: 0\n",ti);
     else printf("Case #%d: %I64d\n",ti,a-(v[0]%a));
 }   
}
