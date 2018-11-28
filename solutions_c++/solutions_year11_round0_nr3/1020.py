#include <cstdlib>
#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

long mas[21];
int s[100];
int main()
{ 
    long temp;
    long min = 9999999;
    long sum = 0;
    
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);  
    int t,n,r,c,h;
    bool res = true;
    cin>>t;
    for(int i=0;i <t;i++)
    {
     for(int j=0;j<21;j++)
       mas[j] = 0;
     cin>>s[i];
     min = 9999999;
     sum = 0;
     for(int j=0; j < s[i]; j++)
     {
      cin>>temp;
      h = 0;
      sum+=temp;
      if(min> temp)min = temp;
      while(temp>0)
      {
       mas[h] = (temp%2+mas[h])%2;
       temp = temp/2;
       h++;
      } 
     }
     res = true;
     for(int j=0; j < 21; j++)
      if(mas[j] != 0)res = false;
     if(res == true)
      printf("Case #%d: %ld\n",i+1,sum - min);
     else
      printf("Case #%d: NO\n",i+1);
    }
    return 0;
}
