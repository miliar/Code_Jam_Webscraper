#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
int a[1100000];
long long getmaxl(map<int,int> M, int l) {
   long long tmp = 0;
   for (map<int,int>::reverse_iterator iM = M.rbegin(); iM !=M.rend() && l; iM++) {
     while (l && iM->second) {
       l--;       tmp+= iM->first;
       (iM->second)--;
     }
     
   }
   return tmp;
}
int main()
{
   int tt; cin >>tt; for (int cc = 1; cc<= tt; cc++) {
     cout <<"Case #"<<cc<<": ";
     long long L,T,N,C;
     cin >> L>>T>>N>>C; T/=2;
     long long tot = 0;
     for (int i = 0 ; i < C; i++)
       cin >> a[i];
     map<int,int> MAP; int QQQ;
     for (int i = 0 , p = 0 ; i<N; i++) {
       if (p<T && p+a[i %C ]>T) {
         MAP[QQQ = p+a[i%C]-T]++;
       }
       if (p>=T) 
         MAP[a[i%C]]++;
       p+=a[i%C];
       tot+=a[i%C];
     }
     long long ans1 = getmaxl(MAP,L);
     MAP[QQQ]--;
     long long ans2 = getmaxl(MAP,L),ans;
   //  cout << ans1<<endl;
   //  cout << ans2 << endl;
     if (ans1< ans2) 
       ans = tot*2-ans2;
     else ans = tot*2-ans1;
     cout <<ans << endl;
}
}

