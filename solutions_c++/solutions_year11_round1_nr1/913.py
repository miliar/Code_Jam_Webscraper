# include <stdio.h>
# include <sstream>
# include <iostream>
# include <string.h>
# include <vector>
# include <string>
# include <algorithm>
# include <map>
# include <math.h>
# include <stdlib.h>

using namespace std;

int main()
{
   freopen("A-large.in","r",stdin);
   freopen("a-out.txt","w",stdout);

   long long i,j,k,l,m,n,r,s,per,t,rp,sp;
   int pd,pg;
   cin >> n;

   for(k=1;k<=n;k++)
   {
       l = 0;
       cin >> t >> pd >> pg;

       rp = __gcd(pd,100);
       sp = 100/rp;

       if(t < sp)
       l = 1;
       else if(pd < 100 && pg == 100)
       l = 1;
       else if(pd > 0 && pg == 0)
       l = 1;
       else l = 0;

       if(l == 1)
       cout <<"Case #"<<k<<": Broken"<<endl;
       else
       cout <<"Case #"<<k<<": Possible"<<endl;
   }


  return 0;
}
