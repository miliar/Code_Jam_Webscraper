# include <stdio.h>
# include <iostream>
# include <sstream>
# include <string>
# include <stdio.h>
# include <vector>
# include <algorithm>
# include <map>

using namespace std;
map<vector<long long>,long long>mp;

int main()
{
   long long test,i,j,k,l,m,n,rem,r,s,t,dif,tot,sum,rp,u,v,la,fa,mul,rs;
   freopen("C.in","r",stdin);
   freopen("C.out","w",stdout);
   cin >> test;

   for(l=1;l<=test;l++)
   {
       cin >> r >> k >> n;
       vector<long long>a(n),b(n);
       vector<long long>st,c(n);
       a.clear();b.clear();c.clear();st.clear();
       mp.clear();

       for(i=0;i<n;i++)
       {
           cin >> m;
           a.push_back(m);
       }

       sum = 0;
       for(i=0;i<r;i++)
       {
           rp = 0;

           if(mp[a] == 0)
           {
               mp[a] = i;

               for(j=0;j<n;j++)
               {
                   if(rp + a[j] <= k)
                   {
                       rp = a[j] + rp;

                   }
                   else
                   {
                       u = j;
                       for(s = u;s<n;s++)
                       c.push_back(a[s]);
                       for(s=0;s<u;s++)
                       c.push_back(a[s]);
                       a.clear();
                       a = c;
                       c.clear();

                       break;
                   }
               }
           }

           else
           break;
           st.push_back(rp);
           sum += rp;
       }

       rs = tot = 0;
       la = i;
       fa = mp[a];
       dif = la - fa;
       mul = (r - i)/dif;
       rem = (r - i)%dif;

       for(i = fa;i<la;i++)
       rs += st[i];

       sum += (rs * mul);



       for(i=fa;i<fa+rem;i++)
       sum += st[i];
       cout <<"Case #"<<l<<": "<<sum << endl;

   }
  return 0;
}
