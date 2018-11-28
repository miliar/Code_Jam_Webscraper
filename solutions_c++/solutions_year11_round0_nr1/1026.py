#include <cstdlib>
#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;
struct E
{
       char c;
       int s;
};
vector<E> v[100];
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("out.txt","w",stdout); 
    int t,n,r,c;
    long pos_o = 1,pos_b = 1;
    unsigned long count = 0;
    E temp;
    cin>>t;
    //scanf("%d",&t);
    for(int i=0; i<t;i++)
    {
     cin>>n;
//         scanf("%d",&n);
         for(int j=0;j<n;j++)
         {
          cin>>temp.c>>temp.s;
//          scanf("%c %d",&temp.c,&temp.s);
          v[i].push_back(temp);
         }
    }
    for(int k=0; k<t; k++)
    {
      count = 0;
      pos_o = 1;
      pos_b = 1;      
      for(int i = 0; i< v[k].size(); i++)
      {
         if(v[k][i].c == 'B')
         {
             count += abs(v[k][i].s-pos_b) + 1;

             for(int j = i + 1; j< v[k].size(); j++)
             {
              if(v[k][j].c == 'O')
              {
               if(abs(v[k][j].s-pos_o) <= abs(v[k][i].s-pos_b) + 1)
                pos_o = v[k][j].s;
               else
                if(v[k][j].s > pos_o)
                 pos_o += abs(v[k][i].s-pos_b) + 1;
                else
                 pos_o -= abs(v[k][i].s-pos_b) + 1;
                 break;
              }        
             }
            pos_b = v[k][i].s;
         }
         else
         {   
             count += abs(v[k][i].s-pos_o) + 1;
             for(int j = i + 1; j< v[k].size(); j++)
             {
              if(v[k][j].c == 'B')
              {
               if(abs(v[k][j].s-pos_b) <= abs(v[k][i].s-pos_o) + 1)
                pos_b = v[k][j].s;
               else
                if(v[k][j].s > pos_b)
                 pos_b += abs(v[k][i].s-pos_o) + 1;
                else
                 pos_b -= abs(v[k][i].s-pos_o) + 1;
                 break;
              }        
             }
             pos_o = v[k][i].s;
         }
      }
      printf("Case #%d: %d\n",k+1,count);
    }
    return 0;
}
