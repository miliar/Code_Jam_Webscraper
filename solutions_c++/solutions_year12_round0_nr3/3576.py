#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
         
using namespace std;


string transform(string x)
{int l, n = x.size(); 
 string ns = "";
 
 for (l=1; l<n; l++)
     ns+=x[l];
 ns+=(x[0]);
 
 return ns;    
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t, cnt = 0, l, a, o, b;
    string cur;
    scanf("%d",&t);
    while (t--)
    {
          cnt++;
          int ans = 0;
          scanf("%d%d",&a,&b);
          for (l=a; l<=b; l++)
          {
              stringstream ss;
              ss<<l;
              ss>>cur;   
              do
              {
                  cur = transform(cur);
                  istringstream ( cur ) >> o;
                  if (o>=a && o<=b && o!=l) ans++;
              }
              while (o!=l);
          }
          
          
          
          printf("Case #%d: %d\n",cnt,ans/2);
    }
}
