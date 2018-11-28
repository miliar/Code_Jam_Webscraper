/* Enter your code here. Read input from STDIN. Print output to STDOUT */

#include<iostream>
#include<algorithm>
#include<math.h>
#include<map>
#include<algorithm>
#include<set>
#include<vector>
using namespace std;

#define fr(i,a,b) for(i=(a);i<(b);++i)
struct triplet
{
int i;
int j;
int k;       
       
};

vector<triplet> get_triplet_set(int x);
bool  ispossible_surprising_with_current_max(int ak,int y);
bool ispossible_at_least(int x,int y);
bool no_surprising_possible_with_at_least_p(int x,int p)
{int i,j,k;
    for(i=p;i<=10;i++)
    for(j=p;j<=10;j++)
    for(k=p;k<=10;k++)
      if(i+j+k==x && (abs(i-j)==2 ||abs(j-k)==2 || abs(k-i)==2))
         return false;
   return true;            
     
     
}

bool ispossible_with_max_y(int x,int y)
{int i,j,k;
 for(i=0;i<=10;i++)
 for(j=0;j<=10;j++)
    if(i+j+y==x && abs(i-j)<=1 && abs(j-y)<=1 && abs(y-i)<=1     )
      return true;
 return false;
 
    
     
}

bool is_surprising(triplet t);
int getmax(triplet t)
 {
   return(max(max(t.i,t.j),t.k));               
                
 }


int main()
    
    
{
int i,j,tt,surprising,ncount,N,S,p,tc,ss;
vector<triplet> st1,st2,st3;
vector<triplet>::iterator iter1,iter2,iter3;
map<char ,char > m;
map<char , char >:: iterator mitr;
	freopen( "C:\\code_jam_io_files\\input.txt", "r", stdin );
	freopen( "C:\\code_jam_io_files\\output.txt", "w", stdout );

scanf("%d",&tt);

for(i=0;i<tt;i++)

  {int max_count=0;
   scanf("%d",&N);
   int *a=new int[5];
    
   
   int *max=new int[N];
   int *tmp=new int[N];
   scanf("%d",&S);
   scanf("%d",&p);
   int max_size=0;
   for(j=0;j<N;j++)
     scanf("%d",&a[j]);               
             
         
 
 
  /* if(S==0)
     {   
         int count=0;
          for(int r=0;r<N;r++)
             {
                  
                  if   ( ispossible_with_max_y(a[r],p) &&(no_surprising_possible_with_at_least_p(a[r],p)) )
                    count++;
                    
            
             }         
            printf( "Case #%d: ", i+1 );   
       	  printf( "%d\n",count); 
           
           
     }
   else
   {
       */
       
       int count;
   triplet temp1,temp2,temp3;
        
           if(N==3)
           {
                   
             
                 st1 = get_triplet_set(a[0]);
                 st2=  get_triplet_set(a[1]);
                 st3=  get_triplet_set(a[2]);
                 for(iter1=st1.begin();iter1!=st1.end();iter1++)
                   for(iter2=st2.begin();iter2!=st2.end();iter2++)
                     for(iter3=st3.begin();iter3!=st3.end();iter3++)
                        {count=0,ss=S;
                             temp1=*iter1;
                             
                             temp2=*iter2;
                             temp3=*iter3;
                            
                                if(is_surprising(temp1))
                                   ss--;                                                                        
                                 if(is_surprising(temp2))
                                 ss--;
                                 
                                 if(is_surprising(temp3))
                                 ss--;                                       
                              if(ss!=0)
                                   continue;
                              else
                                {
                                  int k=getmax(temp1);
                                  if(k>=p)
                                  count++;            
                                    k=getmax(temp2);
                                  if(k>=p)
                                  count++;  
                                    k=getmax(temp3);
                                  if(k>=p)
                                  count++;            
                                if(count>max_count)
                                  max_count=count;
                                }     
                         
                      }                 
           }                    //N==3
         else
            
         if(N==2)
         
           {
                   
          
                 st1 = get_triplet_set(a[0]);
                 st2=  get_triplet_set(a[1]);
              for(iter1=st1.begin();iter1!=st1.end();iter1++)
                   for(iter2=st2.begin();iter2!=st2.end();iter2++)
                     
                        {   count=0,ss=S;
                             temp1=*iter1;
                             
                             temp2=*iter2;
                          
                            
                                if(is_surprising(temp1))
                                   ss--;                                                                        
                                 if(is_surprising(temp2))
                                 ss--;
                                 
                                                       
                              if(ss!=0)
                                   continue;
                              else
                                {
                                  int k=getmax(temp1);
                                  if(k>=p)
                                  count++;            
                                    k=getmax(temp2);
                                  if(k>=p)
                                  count++;  
                                          
                                if(count>max_count)
                                  max_count=count;
                                }     
                         
                      }                 
           }          
         else
           {
                
             st1 = get_triplet_set(a[0]);
                 
               
                  for(iter1=st1.begin();iter1!=st1.end();iter1++)      
                      {   count=0,ss=S;   
                                   temp1=*iter1;                                
                              if(is_surprising(temp1))
                                   ss--;
                                  if(ss!=0)
                                   continue;
                              else
                                {
                                  int k=getmax(temp1);
                                  if(k>=p)
                                  count++;            
                                  
                                          
                                if(count>max_count)
                                  max_count=count;
                                }                                                
                      }     
                      
                      
               }         
         
        printf( "Case #%d: ", i+1);   
        printf( "%d\n", max_count);
                 
                   
        
       
     	 
    
     
      
  
 
  
}
return 0;
}

bool is_surprising(triplet t)
  {
   if(abs(t.i-t.j)==2|| abs(t.j-t.k)==2||abs(t.k-t.i)==2)
     return true;
   return false;                           
                           
  }

vector<triplet> get_triplet_set(int x)
 {
 int i,j,k;
         vector<triplet> st;    
 
         
         for(i=0;i<=10;i++)
         for(j=0;j<=10;j++)
         for(k=0;k<=10;k++)
         if(i+j+k==x && abs(i-j)<=2 && abs(j-k)<=2 && abs(k-i)<=2 )
                      {  triplet temp;
                         temp.i=i;
                         temp.j=j;
                         temp.k=k;
                       st.push_back(temp);
                      }
      return st;         
 }

/*vector<triplet> getpossible_triplets(int x)
{
                vector<triplet> v;
                int i,j,k;
                
fr(i,0,11)
fr(j,0,11)
fr(k,0,11)
    {
       if(i+j+k==x && abs(i-j)<=2 && abs(j-k)<=2 && abs(k-i)<=2 )
                      {  triplet temp;
                         temp.i=i;
                         temp.j=j;
                         temp.k=k;
         v.push_back(temp);
                      }
          
    }                
return v;
}
*/



bool ispossible_at_least(int x,int y)
{int i,j,k;
 for(i=0;i<=10;i++)
 for(j=0;j<=10;j++)
 for(k=0;k<=10;k++)
    if(i+j+k==x && i>=y && j>=y && k>=y &&abs(i-j)<=2 && abs(j-k)<=2 && abs(k-i)<=2 )
      return true;
 return false;
 
   
     
}



bool  ispossible_surprising_with_current_max(int ak,int y)
 {   int j,k;                               
     for(j=0;j<=y;j++)                                
     for(k=0;k<=y;k++)                                                                            
          {
             if(j+k+y==ak && abs(y-j)<=2 && abs(j-k)<=2 && abs(k-y)<=2 &&( abs(j-y)==2 || abs(k-y)==2 || abs(j-k)==2))
               return true;
                                                                                                        
                                                                                                   
         }
  return false; 
 
 }
 




