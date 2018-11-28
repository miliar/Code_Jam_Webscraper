#include <stdio.h>
#include <algorithm>
#include <string>
#include <set>
#include <bitset>
#include <vector> 
using namespace std;
vector < string > pals;
vector < set < char> > temp;
set < char > se;
bitset< 60000 > bit;
char pal[1000];
int main()
{
     int n,k,m;
       scanf("%d%d%d",&k,&n,&m);
    for(int r=0;r<n;r++)
     {            
        scanf("%s",pal);       
        pals.push_back(pal);
     }
     for(int r=0;r<m;r++)
     {
      //       printf("sad\n" );
      temp.clear();
        scanf("%s",pal);       
        string s=pal;
        int flag=0;
        for(int c=0;c<s.size();c++)
         {
            if(  s[c]=='(' )       
                flag=1,se.clear();
            else
             if(  s[c]==')' )    
               temp.push_back(se),flag=0,se.clear();
             else
             {
                se.insert(  s[c] );
                 if( !flag )                     
                  temp.push_back( se ),se.clear();
             }
         }
          //   printf("sad2 %d\n",temp.size() );         
            int res=0;         
       for(int c=0;c<pals.size();c++)
         {
            bool FLAG=0;
            for(int j=0;j<pals[c].size();j++)      
             if(  !temp[j].count( pals[c][j]  ) )
               FLAG=1;
            if(  !FLAG )
            res++;
         }
            printf("Case #%d: %d\n",r+1,res);         
     }
     //system("pause");
    return 0;
}
