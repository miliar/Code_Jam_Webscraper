/*
TASK: A
LANG: C++
*/
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>

int main()
{
	freopen("A.in","rt",stdin);
	freopen("c.out","wt",stdout);
	int T;
	scanf("%d",&T);
	
	for(int i=0 ; i < T ; i++)
	{  int n=0,s=0,p=0,count=0;
       scanf("%d %d %d",&n,&s,&p);
       for(int j=0 ; j<n ; j++)
       {       int num=0,temp=0,prob=0;
               scanf("%d",&num);
               temp=num-p;
               prob=temp-(2*p);
               if(temp >= 0)
               {if (prob>=0)
                {count++;
                }
                if ((prob>=-4) && (prob<-2) && (s>0))
                {count++;
                s--;
                }
                 if ((prob>=-2) && (prob<0) )
                {count++;
                
                }
               }
               }
               printf("Case #%d: %d\n",i+1,count);
             
    }
            
	
    return 0;
}

