#include <string>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <math.h>
#include <utility>
#include <sstream>
#include <queue>
#include <stack>
#include <iomanip>
#include <limits.h>
#ifndef ONLINE_JUDGE
#include <conio.h>
#endif
using namespace std;

#define max(a,b) (a>=b?a:b)
#define min(a,b) (a<=b?a:b)
#define pb push_back
#define mp make_pair
#define all(X) (X).begin(),(X).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

int N,i,j,T,decode[256],yes[256],op[256];
char input[1000];

int main()
{
    freopen("a.out","w",stdout);
   decode['y']='a';
   decode['e']='o';
   decode['q']='z';
   yes['y']=1;
   yes['e']=1;
   yes['q']=1;
   op['a']=1;
   op['o']=1;
   op['z']=1;
   char str[]="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
   char dc[]="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
   N=strlen(str);
   for(i=0;i<N;i++)
   {
       if(str[i]!=' ')
       {
         decode[str[i]]=dc[i];
         yes[str[i]]=1;
         op[dc[i]]=1;
       }
   }  
   /*
   for(i='a';i<='z';i++)
   {
       if(yes[i]==0)cout<<"dec "<<char(i)<<endl;
       if(op[i]==0)cout<<"op "<<char(i)<<endl;       
   }
   */
   decode['z']='q';
   yes['z']=1;
   op['q']=1;
   decode[' ']=' ';
   scanf("%d%*c",&T);
   for(j=1;j<=T;j++)
   {
       gets(input);
       N=strlen(input);
       printf("Case #%d: ",j);
       for(i=0;i<N;i++) printf("%c",char(decode[input[i]]));
       printf("\n");
   }                  
   
#ifndef ONLINE_JUDGE
    getch();
#endif
    return 0;
}
