#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
    
int L,D;
int N;

char w[5000];
char dic[5010][20];
char word[20];
long long res;
int num;
//(ab)c(de) 3
bool verify(int a)
{
     for(int i=0;i<D;i++)
     {
            int flag = 1; 
            for(int j=0;j<=a;j++)
            {
                    if(word[j]!=dic[i][j])
                    { flag=0; break;}        
            }         
            if(flag==1) return true; 
     }     
     return false;
}

void search(int a,int b)
{
         if( a == L ) 
         {
//             printf("%d: %s\n",num,word);
             num++;
             for(int i=0;i<D;i++)
             {
                     if(strcmp(dic[i],word)==0)
                               res++;                        
             }
             return ;    
         }
         if(w[b]>='a' && w[b]<='z')
         {  
              word[a] = w[b];
              if(!verify(a)) return;
              int flag = -1;
              int j = b; 
              for( ;j>=0;j--)
              {
                  if(w[j]==')'){ flag=0;break;}
                  else if(w[j]=='('){ flag=1;break;}
              }
              if( flag==-1 || flag==0 )
              {   search(a+1,b+1);  }
              else
              {
                  int i = b;
                  while( w[i]!=')' ) i++;
                  search(a+1,i+1);
              }
         }
         else if(w[b]=='(')
         {
             for(int i=b+1; w[i]!=')'; i++)
             {
                     search(a,i);        
             }    
         }
         else
         {
             printf("Err..(\n");    
         }
          
}


int main(int argc, char *argv[])
{
  //  freopen("in.txt","r",stdin);
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d%d%d",&L,&D,&N);
    memset(dic,'\0',sizeof(dic));
    for(int i=0;i<D;i++)
    {
           scanf("%s",dic[i]);
    }
    int CASE = 1;
    while(N--)
    {
          num = 0;
          res = 0;
          memset(word,'\0',sizeof(word));
          memset(w,'\0',sizeof(w));
          scanf("%s",w);
          search(0,0); 
          printf("Case #%d: %lld\n",CASE,res);    
          CASE++;     
    }

    return 0;
}
