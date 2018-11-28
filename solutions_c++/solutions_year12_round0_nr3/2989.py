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


int numdigits(int n)
 {
 int count = 1; /* bound to be at least one digit! */
 while(n != 0)
 {
 n /= 10;
 ++count;
 }
 return count;
 }
 
 int power(int a, int b)
{
     int c=a;
     for (int n=b; n>1; n--) c*=a;
     return c;
}


int main()
{
	freopen("A.in","rt",stdin);
	freopen("c.out","wt",stdout);
	int N;
	scanf("%d",&N);
	
    for (int i = 0; i < N ; i++)
     {
             int a=0,b=0,count=0;
             scanf("%d %d",&a,&b);
             for (int x=a; x<=b;x++) 
             {  int digits=0,temp_num=0,temp1=0,temp2=0;
                 digits=numdigits(x)-1;
                 temp_num=x;
               for (int j = 1 ; j<=digits;j++)
               {
                   temp1=temp_num/10;
                   temp2=temp_num%10;
                   temp_num=temp2*power(10,digits-1) + temp1 ;
                   if (temp_num >= a && temp_num <=b && temp_num > x) 
                    {count ++ ;}
                 }
             } 
             printf("Case #%d: %d\n",i+1,count);
   	 }
	return 0;
}

