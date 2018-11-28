#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int s[40];
char buf[41];
long long total,L, cuenta;
bool isUgly(long long x)
   {
      if(x<0)
	     x=-x;
      return ((x%2)==0) || ((x%3)==0) || ((x%5)==0) || ((x%7)==0);
   }
void getCount(int ini, long long actual)
   {
      if(ini==L)
	     {
		    cuenta++;
		    if(isUgly(actual))
			   {
		          total++;
			   }
			return;
		 }
	   for(int fin=ini;fin<L;fin++)
	      {
		     long long a=0;
			 for(int i=ini;i<=fin;i++)
			    a=a*10+buf[i]-'0';
		    if(ini>0)
			   {
		          getCount(fin+1, actual+a);
			      getCount(fin+1, actual-a);
			   }
			else
			   getCount(fin+1, actual+a);
		  }
   }



int main()
   {
      int N;
	  scanf("%d", &N);
	  for(int caso=1;caso<=N;caso++)
	    {
		   scanf("%s", buf);
		   L=0;
		   while(buf[L])
		      L++;
		   
		   total=0;
		   cuenta=0;
		   getCount(0,0);
		   printf("Case #%d: %lld", caso, total);
		   if(caso<N)
		      printf("\n");
		}
      
      return 0;
   }
