#include <cstdlib>
#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string.h>

using namespace std;
int main()
{
    string r[100][36],d[100][28],word[100],res = "";  
    int counter[100][3];  
    freopen("B-large (1).in","r",stdin);
    freopen("out.txt","w",stdout); 
    int t,n,rs,c;
    int count,pos_f;
    int temp;
    cin>>t;
    for(int i=0; i<t;i++)
    {
      cin>>counter[i][0];
      for(int j=0;j<counter[i][0];j++)
        cin>>r[i][j];
      cin>>counter[i][1];
      for(int j=0;j<counter[i][1];j++)
        cin>>d[i][j];
      cin>>counter[i][2];
      cin>>word[i];      
    }
    for(int i=0;i<t;i++)
    {
      res = word[i][0];
      bool crock;
      for(size_t k = 1; k<counter[i][2]; k++)
      {
       crock = false;
       for(int h =0; h<counter[i][0]; h++)
       {
        if((res[res.length()-1] == r[i][h][0] && word[i][k] == r[i][h][1]) || (res[res.length()-1] == r[i][h][1] && word[i][k] == r[i][h][0]))
         {res[res.length()-1] = r[i][h][2];crock = true;break;}
       }
       if(crock == false)
{       crock = true;
       res += word[i][k];
 }      for(int h = 0; h<counter[i][1]; h++)
       {
        count = 0;
        pos_f = -1;
        for(size_t l=0; l < res.size(); l++)
         if(res[l] == d[i][h][0])
         {
          count++;
          pos_f = l;
          break;
         }
        for(size_t l=0; l < res.size(); l++)
         if(res[l] == d[i][h][1] && l != pos_f)
         {
          count++;
          break;
         }
        if(count == 2){
         res = "";break;}
       }
       if(crock == false)
        res += word[i][k];
      }
      printf("Case #%d: [",i+1);
      for(int h = 0; h < res.length(); h++)
      {
       if(h > 0)
        cout<<", "<<res[h];
       else
        cout<<res[h];
      }
      printf("]\n");
    }
    return 0;
}
