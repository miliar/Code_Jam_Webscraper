#include <algorithm>
#include<iostream>
#include <cstdio>

using namespace std;
typedef long long ll;


int main()
{
   int t,n,p;
   char r;
   cin >> t;
   for(int i=1;i<=t;++i)
   {
      cin >> n;
      int lbp=1,lop=1;
      int bs=0,os=0;
      int w=0;
      for(int j=0;j<n;++j)
      {
         cin >>r>>p;
         if(r=='O')
         {
            w=max(os+abs(p-lop)+1,w+1);
            lop=p;
            os=w;
         }
         else
         {
            w=max(bs+abs(p-lbp)+1,w+1);
            lbp=p;
            bs=w;
         }
      }
      cout << "Case #" << i << ": " << w << endl;
   }


    return 0;
}
