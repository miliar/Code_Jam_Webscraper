#include <ctype.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdio.h>
#include <time.h>
#include <vector>
#include <string>

int check(int,int);
void solve(int,int);

int arr[1000][3];
int main()
{
    int n,k;
    FILE *in=fopen("A.in","r");
    FILE *out=fopen("A.out","w");
    int case_no=1,T;
	fscanf(in,"%d",&T);
    while(T--)
    {
            
              
        n=0;
        k=0;
       
		    fscanf(in,"%d",&n);
            fscanf(in,"%d",&k);
		
		if(check(n,k)==1)
		{
		    fprintf(out,"Case #%d: ON\n",case_no);
		}
    	else
		{
		    fprintf(out,"Case #%d: OFF\n",case_no);
		}
		case_no++;
	}
   
    return 0;
}


int check(int n,int k)
{ 
  solve(n,k);
  if(arr[n-1][2]==1)
  return 1;
  else 
  return 0;   
}


void solve(int n,int k)
{    int i,j;
     
     for(int x=0;x<=n;x++)
     {
       arr[x][0]=0;
       arr[x][1]=0;
       arr[x][2]=0;
     }
     
     
     arr[0][0]=1;
                    
        for(j=0;j<k;j++)
          {  
             for(i=0;i<n;i++)
               {
                    if(arr[i][0]==1)
                     { if(arr[i][1]==0)
                       arr[i][1]=1;   
                       else
                       arr[i][1]=0;
                     }        
                    
               }          
               
                for(i=0;i<n;i++)
               { 
                   
                   if(arr[i][0]==1 && arr[i][1]==1)
                      arr[i][2]=1;
                   else   
                      arr[i][2]=0;
                      
                    if(arr[i][1]==1 && arr[i][2]==1)
                      arr[i+1][0]=1;  
                    else
                      arr[i+1][0]=0;  
                   
                   }  
                   
          }               
     
     
 }
















