/* 
 * File:   newJam.cc
 * Author: Tanaeem
 *
 * Created on August 2, 2008, 11:08 PM
 */

#include <stdio.h>


#include <stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
int k,s;
char inp[1100];
char op[1100];
int arr[10];
int mincost()
{
  for (int i = 0; i < s; i+=k)
    {
      for (int j = 0; j < k; j++)
        {
          op[i+j]=inp[arr[j]+i];
        }
    }
  int cost=1;
  for (int i = 1; i < s; i++)
    {
      if(op[i]!=op[i-1])
        cost++;
    }
  return cost;
  
}
int main ()
{
  freopen ("D.in","r",stdin);
  freopen ("small.op","w",stdout);
  
//  freopen ("C-large.in.enc.txt","r",stdin);
//  freopen ("large.op","w",stdout);
  int t,c=0;
  scanf ("%d",&t);
  while (t--)
    {
      scanf("%d%s",&k,inp);
      s=strlen (inp);
      for (int i = 0; i < k; i++)
        {
          arr[i]=i;
        }
      int mc=s;
      do
        {
          int cost=mincost();
          if(mc>cost)
            mc=cost;
        }while(next_permutation (arr,arr+k));


      
      printf ("Case #%d: %d\n",++c,mc);
      

    }


  return 0;
}

