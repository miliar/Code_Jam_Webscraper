#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <cassert>

std::vector<int> va;
std::vector<int> res;
void solve()
{
    if(va.size()==1 ) 
    {
         res.push_back(va[0]);
         res.push_back(0);
         return;                           
    }  
    bool asc = true; 
    int m=0; 
    for(int i=0;i<va.size()-1;i++)
    {
      if(va[i+1]!=0) m = i+1;
      if(va[i]<va[i+1]) {asc =false; break;}
    }
    if(asc==true)
    {
           res.push_back(va[m]);
           res.push_back(0);
           for(int i=va.size()-1; i>=0; i--)
           {
                   if(i==m) continue;
                   res.push_back(va[i]);        
           }
           return;                   
    }
    for(int i=va.size()-2; i>=0; i--)
    {
           if( va[i]<va[i+1] ) { m = i; break;}         
    }
    for(int i=0;i<m;i++)
    {
            res.push_back(va[i]);        
    }
    int first = va[m] ;
    std::vector<int> temp;
    for(int i=m;i<va.size();i++)
    {
            temp.push_back(va[i]);        
    }
    sort(temp.begin(),temp.end());
    
    for(int i=0;i<temp.size();i++)
    {
            if(temp[i]>first) { m = i; res.push_back(temp[i]); break;}        
    }
    for(int i=0;i<temp.size();i++)
    {
            if(i==m) continue;
            res.push_back(temp[i]);        
    }
    return;
}

int main(int argc, char *argv[])
{
   freopen("B-large.in","r",stdin);
 //    freopen("B-large-practice (1).in","r",stdin);
    freopen("out.txt","w",stdout);
      
    int N;

    scanf("%d",&N);

    int CASE = 1;
    while(N--)
    {
          char buf[30];
          memset(buf,'\0',sizeof(buf));    
          va.clear(); 
          res.clear();   
         
          scanf("%s",buf);

          int j = 0;

          while(1)
          {
                 if( buf[j]=='\0' ) break; 
                 
                 int i = buf[j] - '0';                    
                 va.push_back(i);
                 j++ ;                          
          } 
    //      for(int i=0;i<va.size();i++)
      //        printf("%d",va[i]);  
          solve();
          
          printf("Case #%d: ",CASE);
          for(int i=0;i<res.size();i++)
               printf("%d",res[i]);
          printf("\n");
          CASE++;     
    }

    return 0;
}
