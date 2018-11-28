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
    fori(h,0,t){
        int n;
        scanf("%d",&n);
        int *a=new int [n];
        fori(i,0,n) scanf("%d ",&a[i]);
        int min=1100000;
        int sum=0;
        fori(i,0,n)
            if(a[i]<min) min=a[i];
        int p=0;
        fori(i,0,n){
            p^=a[i];
            sum+=a[i];
        }
        if (p!=0){
            printf("Case #%d: NO\n",h+1);
        }
        else{
            printf("Case #%d: %d\n",h+1,sum-min);
        }
    }    
    
    return 0;
}
