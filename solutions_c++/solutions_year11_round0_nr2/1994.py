# include <stdio.h>
# include <stdlib.h>
# include <sstream>
# include <iostream>
# include <string>
# include <string.h>
# include <math.h>
# include <algorithm>


using namespace std;


int main()
{
   int i,j,k,g,d,l,m,n,r,s,t,u,o,flag[1000],com[300][300],del[300][300],ln;
   char a,b,c;
   char st[300];

   freopen("B-large.in","r",stdin);
   freopen("B.txt","w",stdout);

   cin >> t;

   for(g=1;g<=t;g++)
   {


       memset(del,0,sizeof(del));
       memset(flag,0,sizeof(flag));
       memset(com,0,sizeof(com));

       cin >> d;
       for(i=1;i<=d;i++)
       {
           cin >>a>>b>>c;
           com[a][b] = com[b][a] = c;
       }
       cin >> l;
       for(i=1;i<=l;i++)
       {
           cin >> a >> b;
           del[a][b] = del[b][a] = 1;
       }

       cin >> ln;
       cin >>st;
       --ln;

       string rt="";

       for(i=0;i<=ln;i++)
       {
           l = rt.size();
           if(l != 0 && com[rt[l-1]][st[i]] != 0)
           {
               rt[l-1] = com[rt[l-1]][st[i]];
           }
           else
           {
               u = 0;
               for(j=l-1;j>=0;j--)
               {
                   if(del[st[i]][rt[j]] == 1)
                   {
                      u = 1;
                      rt = "";
                      break;
                   }
               }
               if(u == 0)rt += st[i];

           }

       }
      // cout << rt<<endl;

      l = rt.size();
      cout <<"Case #"<<g<<": [";
      for(i=0;i<l;i++)
      {
          cout << rt[i];
          if(i != l-1)
          cout <<", ";
      }
      cout << "]"<<endl;
   }
  return 0;
}
