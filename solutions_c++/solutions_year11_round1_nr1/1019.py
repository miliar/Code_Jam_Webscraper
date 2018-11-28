#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <string>
#include <math.h>

using namespace std;

#define fori(i,j,k) for(int i=j;i<k;i++)
#define ford(i,j,k) for(int i=j-1;i>=k;i--)
#define i64 __int64
#define ld long double
#define mp make_pair


int main()
{
    int t;
    scanf("%d\n",&t);
    //printf("%d",t);
    fori(i,0,t){
        int a,b,c;
        scanf("%d %d %d\n",&a,&b,&c);
        //printf("%d %d %d ",a,b,c);
        if((c==0)&&(b==0)) {printf("Case #%d: Possible\n",i+1); continue;}
        if((c==100)&&(b==100)) {printf("Case #%d: Possible\n",i+1); continue;}
        if((c==0)||(c==100)) { printf("Case #%d: Broken\n",i+1); continue;}
        int d=100;
        if(b%5==0) {b/=5; d/=5;}
        if(b%5==0) {b/=5; d/=5;}
        if(b%2==0) {b/=2; d/=2;}
        if(b%2==0) {b/=2; d/=2;}
        if(a<d){printf("Case #%d: Broken\n",i+1); continue;}
        printf("Case #%d: Possible\n",i+1);
    }
    
    return 0;
}
