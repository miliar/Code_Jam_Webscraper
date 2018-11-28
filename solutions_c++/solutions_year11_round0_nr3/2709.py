#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<fstream>
#include<stdio.h>
#include <stdlib.h>

#define INPUT "large.txt"
#define FOR(i,n) for(int i=0;i<n;i++)

FILE* ifp = fopen(INPUT,"r");
FILE* ofp = fopen("output.txt","w+");
//FILE* ifp = stdin;

#define MAXN 1000

using namespace std;

int main()
{
int t,n, a[MAXN], x,sum;

fscanf(ifp,"%d",&t);

    FOR(T,t)
    {
        fscanf(ifp,"%d",&n);
        x = sum = 0;
        
        FOR(i,n)
               {
                            fscanf(ifp,"%d",&a[i]);
                            x = x ^ a[i]; 
                            sum += a[i];
                            //cout<<x<<endl;                      
               }
        
        if(x==0)
                  sort(a,a+n);          
      
        fprintf(ofp,"Case #%d:",T+1);
        if(x==0) fprintf(ofp," %d\n",sum - a[0]);
        else fprintf(ofp," NO\n");
   }


system("Pause");
return 0;
}
