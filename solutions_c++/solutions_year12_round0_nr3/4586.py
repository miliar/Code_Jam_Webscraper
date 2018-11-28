using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>

int main()
{
    int te,t,cs=1,len,a,b,temp,i,r,q,res;
    scanf("%d",&te);
    while(te--)
    {
       scanf("%d%d",&a,&b);
       temp=b,len=0,res=0;
       while(temp!=0)
       {
          temp/=10;
          len++;
       }
       t=1;
       for(i=1;i<len;i++)
          t=t*10;
          
       for(i=a;i<=b;i++)
       {
                  temp=i;
                  while(1)
                  {
                           r=temp%10;
                           q=temp/10;
                           temp=r*t+q;
                           if(temp>=a && temp<=b && temp>i) res++;
                           if(temp==i) break;
                  }
       }
         
       printf("Case #%d: %d\n",cs,res);
       cs++;
    }
    return 0;
}
