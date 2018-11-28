#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <set>
#include <cmath>
#include <cstring>
#include <stdio.h>
#include <string.h>
#include <sstream>
#include <stdlib.h>
#include <vector>
#include <iomanip>
using namespace std;

int Googlers,A,B;

int cal(int cas)
{
    vector<int>V;
    int l=log10(cas)+1,rem=0,AA=cas,counter=0;
    for(int i=0;i<(l-1);i++)
    {
        rem=AA%10;
        AA=AA/10;
        AA=(rem*(int)pow(10.0,l-1))+AA;
        if(AA>=A && AA<=B && AA>cas) V.push_back(AA);
    }
     sort(V.begin(),V.end());
     if(V.size())
     {
          counter++;
          for(int i=1;i<V.size();i++)
          if(V[i]!=V[i-1]) counter++;
     }
     return counter;
}
int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int i,j,k,len,N,P,S,t=1,mx,res;
    scanf("%d",&k);
    while(k--)
    {
        scanf("%d %d",&A,&B);
        res=0;
        for(i=A;i<=B;i++)
        {
           res+=cal(i);
        }
        printf("Case #%d: %d\n",t++,res);
    }
    return 0;
}
