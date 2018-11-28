/* 
 * File:   main.cpp
 * Author: tanaeem
 *
 * Created on May 8, 2010, 6:38 AM
 */

#include <stdlib.h>
#include <stdio.h>

/*
 * 
 */
int main()
{
  freopen("A1.in","r",stdin);
  freopen("A1.op","w",stdout);

  int t;
  scanf("%d",&t);
  int cs=0;
  while (t--)
  {
    int n,k,p;
    scanf("%d%d",&n,&k);
    p=1;
    while (n--)
    {
      if(k&1)k/=2;
      else p=0;
    }
    printf("Case #%d: %s\n",++cs,p?"ON":"OFF");
  }


  return 0;
}

