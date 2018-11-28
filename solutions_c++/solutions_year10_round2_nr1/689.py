#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <list>

using namespace std;

typedef struct node{
        string name;
        node *next[110];
        int son;
        };
        
bool is(char x)
{
   return((x >= 'a' && x <= 'z') || (x >= '0' && x <= '9'));
}

int n,m;
char path[110];
node *root;

void build_tree()
{
      root = new node; 
      root -> son = 0;
      root -> name = ""; 
      memset(root -> next,NULL,sizeof(root -> next));      
      for(int i = 1; i <= n; i++)
      {  
         scanf("%s",&path); //cout<<path<<endl;
         string a[110];
         int l = strlen(path);
         int tmp = 0;
         string tmp1 = ""; 
         for(int j = 1; j < l; j++)
         {
            if(is(path[j]))
            {
               tmp1 += path[j];
            }
            if(!is(path[j]) || j == l-1)
            {
               tmp ++;
               a[tmp] = tmp1;
               tmp1 = "";
            }
         }
         //cout<<tmp<<endl;
         //for(int i = 1; i <= tmp; i++) cout<<a[i]<<' ';cout<<endl;
         node *tmp2 = root;
         for(int j = 1; j <= tmp; j++)
         {
            bool flag = 0;
            for(int k = 1; k <= tmp2 -> son; k++)
            {
               if(tmp2 -> next[k] != NULL && tmp2 -> next[k] -> name == a[j])
               {
                  tmp2 = tmp2 -> next[k];
                  flag = 1;
                  break;
               }
            }
            if(!flag)
            {
               tmp2 -> son++;
               node *tmp3 = new node;
               tmp3 -> name = a[j];
               tmp3 -> son = 0;
               memset(tmp3 -> next,NULL,sizeof(tmp3 -> next));
               tmp2 -> next[tmp2 -> son] = tmp3;
               tmp2 = tmp3; 
            }
         }            
      } 
}

int cal()
{
    
      int ans = 0;
      for(int i = 1; i <= m; i++)
      {
         scanf("%s",&path);
         string a[110];
         int l = strlen(path);
         int tmp = 0;
         string tmp1 = "";
         for(int j = 1; j < l; j++)
         {
            if(is(path[j]))
            {
               tmp1 += path[j];
            }
            if(!is(path[j]) || j == l-1)
            {
               tmp ++;
               a[tmp] = tmp1;
               tmp1 = "";
            }
         }
         node *tmp2 = root;
         for(int j = 1; j <= tmp; j++)
         {
            bool flag = 0;
            for(int k = 1; k <= tmp2 -> son; k++)
            {
               if(tmp2 -> next[k] != NULL && tmp2 -> next[k] -> name == a[j])
               {
                  tmp2 = tmp2 -> next[k];
                  flag = 1;
                  break;
               }
            }
            if(!flag)
            {
               tmp2 -> son++;
               node *tmp3 = new node;
               tmp3 -> name = a[j];
               tmp3 -> son = 0;
               memset(tmp3 -> next,NULL,sizeof(tmp3 -> next));
               tmp2 -> next[tmp2 -> son] = tmp3;
               tmp2 = tmp3;
               ans ++;
            }
         }             
      } 
      return(ans); 
}

int main()
{
freopen("A-large.in","r",stdin);
freopen("E:/out.txt","w",stdout);
   int t,test = 0;
   scanf("%d",&t);
   while(t--)
   {
      scanf("%d%d",&n,&m);
      build_tree();      
      printf("Case #%d: %d\n",++test,cal());
   }
      return(0);
}         
