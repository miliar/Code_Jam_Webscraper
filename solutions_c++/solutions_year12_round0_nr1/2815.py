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
	int N;
	scanf("%d",&N);
	
	
    for (int i = 0; i <= N ; i++)
     {   char x=' ';
         if (i!=0)
         {printf("Case #%d: ",i);}
         scanf("%c",&x);
		 /*---*/
		 while(x!='\n'){
         
         switch (x)
		 {
		 case 'a':
              x='y';
              break;
		 case 'b':
              x='h';
              break;
         case 'c':
              x='e';
              break;
		 case 'd':
              x='s';
              break;
         case 'e':
              x='o';
              break;
         case 'f':
              x='c';
              break;     
         case 'g':
              x='v';
              break;
         case 'h':
              x='x';
              break;
         case 'i':
              x='d';
              break;
         case 'j':
              x='u';
              break;
         case 'k':
              x='i';
              break;
         case 'l':
              x='g';
              break;
         case 'm':
              x='l';
              break;
         case 'n':
              x='b';
              break;
         case 'o':
              x='k';
              break;
         case 'p':
              x='r';
              break;
         case 'q':
              x='z';
              break;
         case 'r':
              x='t';
              break;
         case 's':
              x='n';
              break;
         case 't':
              x='w';
              break;
         case 'u':
              x='j';
              break;
         case 'v':
              x='p';
              break;
         case 'w':
              x='f';
              break;
         case 'x':
              x='m';
              break;
         case 'y':
              x='a';
              break;
         case 'z':
              x='q';
              break;
              }
              printf("%c",x); 
              scanf("%c",&x);
                  }
         if (i!=0)
         {printf("\n");}
         
   	 }
	return 0;
}
