#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <stack>
using namespace std;
int main()
{
    int n;
    char pal[1000];
    scanf("%d",&n);
    for(int j=0;j<n;j++)
     {
       scanf("%s",pal);
       vector < string > v;
       string s=pal;
       string s2=pal;
       //sort(s.begin(),s.end());
       int flag=0;
       do
       {
          if(s[0]=='0')               
          continue;
           if(  s2<s )
           {
                flag=1;
             break;
           }
       }while(  next_permutation(s.begin(),s.end()) );
       if(  !flag )
        {
          sort(s.begin(),s.end()); 
          s="0"+s;
          for(int r=0;r<s.size();r++)  
           {
              if(  s[r]!='0' )    
              {   
               s[0]=s[r],s[r]='0';
               break;
              }
           }
        }
       printf("Case #%d: %s\n",j+1,s.c_str());
     }
     return 0;
}
