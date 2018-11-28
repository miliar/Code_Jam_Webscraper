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
    	//freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int c,cse,a,b,num,mul,j,res;
    cin>>c;cse=0;
    while(c-->0)
    {
         cse++;res=0;
         cin>>a>>b;
         num=a;mul=1;
         while(num) {num/=10;mul*=10;}
         mul/=10;
         
         for(j=a;j<=b;j++)
         {
              num=j;
              do
              {
                    num=(num%10)*mul+(num/10);
                    if(num>j && num<=b) res++;
              }while(j!=num);
         }
         printf("Case #%d: %d\n",cse,res);
    }
    return 0;
}
              
         
