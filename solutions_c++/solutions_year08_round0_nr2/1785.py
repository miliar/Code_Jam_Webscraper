#include<stdio.h>
#include<cstdlib>
#include<algorithm>
#include<functional>
#include<vector>
#include<stdlib.h>
using namespace std;
struct NODE
{
 int st,end;       
};
NODE n1[110],n2[110];
vector<int> v1,v2;
FILE *fout;
bool cmp(const NODE &a,const NODE &b)
{return a.st<b.st;}
int main()
{
  int t,index,i,j;
  fout=fopen("a.out","w");
  scanf("%d",&t);
  for(index=1;index<=t;index++)
  {
      int T,na,nb;                             
      scanf("%d%d%d",&T,&na,&nb);
      int e,f,g,h;                         
      for(i=0;i<na;i++)
      {
      scanf("%d:%d %d:%d",&e,&f,&g,&h);
      n1[i].st=e*60+f;n1[i].end=g*60+h;
      
      }                         
      for(i=0;i<nb;i++)
      {
      scanf("%d:%d %d:%d",&e,&f,&g,&h);
      n2[i].st=e*60+f;n2[i].end=g*60+h;
      }
      sort(n1,n1+na,cmp);
      sort(n2,n2+nb,cmp);
      v1.clear();v2.clear();
      
      int id1,id2;
      id1=id2=0;
      int ans1,ans2;
      ans1=ans2=0;
      while(1)
      {
            if(id1==na&&id2==nb)
            break;       
            if(id1==na||id2==nb)
            {
               if(id1==na)
               {
                  if(v2.size()==0)                         
                  {
                  ans2++;                                         
                  v1.push_back(n2[id2++].end+T);                                      
                  }  
                  else
                  {      
                     if(v2[0]<=n2[id2].st)     
                     {
                     v2.erase(v2.begin());                          
                     v1.push_back(n2[id2++].end+T);                        
                     }  
                     else
                     {
                     ans2++;    
                     v1.push_back(n2[id2++].end+T); 
                     }            
                  }               
               }          
               else
               {
               if(v1.size()==0)                         
               {
                  ans1++;                                         
                  v2.push_back(n1[id1++].end+T);                                      
               }                      
               else 
               {
                  if(v1[0]<=n1[id1].st)     
                  {
                    v1.erase(v1.begin());                         
                    v2.push_back(n1[id1++].end+T);                        
                  }  
                  else
                  {
                     ans1++;    
                     v2.push_back(n1[id1++].end+T); 
                  } 
               }       
               }          
               continue;                 
            } 
            if(n1[id1].st<n2[id2].st)
            {
               if(v1.size()==0)                         
               {
                  ans1++;                                         
                  v2.push_back(n1[id1++].end+T);                                      
               }                      
               else 
               {
                  if(v1[0]<=n1[id1].st)     
                  {
                    v1.erase(v1.begin());                         
                    v2.push_back(n1[id1++].end+T);                        
                  }  
                  else
                  {
                     ans1++;    
                     v2.push_back(n1[id1++].end+T); 
                  } 
               }
                                     
            }
            else 
            {
                     
               if(v2.size()==0)                         
               {
                  ans2++;                                         
                  v1.push_back(n2[id2++].end+T);                                      
               }                      
               else 
               {
                  if(v2[0]<=n2[id2].st)     
                  {
                    v2.erase(v2.begin());                          
                    v1.push_back(n2[id2++].end+T);                        
                  }  
                  else
                  {
                     ans2++;    
                     v1.push_back(n2[id2++].end+T); 
                  } 
               }
                 
            }
           
           
            sort(v1.begin(),v1.end());
            sort(v2.begin(),v2.end());  
      }
      fprintf(fout,"Case #%d: %d %d\n",index,ans1,ans2);
   }
      
system("pause");
return 0;    
}
