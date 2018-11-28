#include<iostream>
#include<string>
#include<algorithm>
#include<sstream>

using namespace std;
bool con[10005][10005];
char ans[10005]; 
int h,w;

bool visited[10005];

void dfs(int pos,char c)
{
// cout<<"d- "<<pos<<endl;
 for(int i=0;i<h*w;i++) 
   if(pos!=i && (con[pos][i] || con[i][pos]) && (visited[i]==false))
    {
     ans[i]=c;
     visited[i]=true;
     dfs(i,c);     
    }
}

int main()
{
  int t;
  
  int dw[]={0,-1,1,0};
  int dh[]={-1,0,0,1};

   
    freopen("water.out","w",stdout);
    freopen("water.in","r",stdin);

   scanf("%d",&t);

  for(int tt=0;tt<t;tt++)
   {
//     int h,w;
           
      scanf("%d %d",&h,&w);


     int ques[h][w];
     
       for(int i=0;i<h*w;i++)
       {
          visited[i]=false;
        for(int j=0;j<h*w;j++)
          con[i][j]=false;
       }

      for(int i=0;i<h;i++)
       for(int j=0;j<w;j++)   
        {
          scanf("%d",&ques[i][j]);
          ans[i*w+j]='X';
        }

     for(int i=0;i<h;i++) 
       for(int j=0;j<w;j++)
        {
         int pos=-1;
         int mn=ques[i][j];
        
             for(int k=0;k<4;k++)
              {
                if((i+dh[k]>-1) && (j+dw[k]>-1) && (i+dh[k]<h) && (j+dw[k]<w))
                 {
                    if(ques[i+dh[k]][j+dw[k]]<mn)
                     {
                       pos=k;
                       mn=ques[i+dh[k]][j+dw[k]];
                     }
                 }
              }
          if(pos>=0)
           {
             con[i*w+j][(i+dh[pos])*w+(j+dw[pos])]=true;
           }
        }

    int charac='a';
    
    for(int i=0;i<h*w;i++)  
     {  
      if(ans[i]=='X')
      {
       ans[i]=charac;
       visited[i]=true;
       dfs(i,charac);
       charac++;
      }
     }

      printf("Case #%d:\n",tt+1);
       for(int i=0;i<h;i++)
        {
         for(int j=0;j<w;j++)
          {
           if(j)
             printf(" ");
           printf("%c",ans[i*w+j]);
          }
         printf("\n");
        }
 /*       for(int j=0;j<h*w;j++)
         {
           if(con[i][j]==true)
            {
              printf("%d %d\n",i,j);
            }
         }*/

      
   }

 return 0;
}
