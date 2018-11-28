#include <stdio.h>
#include <math.h>
int check(int,int);
void solve(int,int);

int arr[30][3];
int main()
{
    int n,k;
    FILE *in=fopen("A.in","r");
    FILE *out=fopen("A.out","w");
    short int case_no=1,T;
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
  if(k%8==0)return 0;
  else if((k-2)%8==0)return 0;
  else if((k-4)%8==0)return 0;  
  else if((k-6)%8==0)return 0;
  else
  
  { if((k-1)%8==0)
     { if(n==1)return 1; 
       else 
       return 0;
      }   
      else  if((k-3)%8==0)
     { if((n==1)||(n==2))return 1; 
       else 
       return 0;
      }   
       else  if((k-5)%8==0)
     { if(n==1)return 1; 
       else 
       return 0;
      }   
               
    else  
      {  
      solve(n,k);
      if(arr[n-1][2]==1)
      return 1;
      else 
      return 0;   
      } 
       }
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
















