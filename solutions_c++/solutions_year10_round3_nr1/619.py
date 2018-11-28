#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
using namespace std;
pair <int, int > ar[1001];
int n,_N;
int main()
{
   scanf("%d",&_N);
   for(int _r=0;_r<_N;_r++)
    {
        int n,res=0;
        scanf("%d",&n);
        for(int r=0;r<n;r++)
         scanf("%d %d",&ar[r].first,&ar[r].second);
        for(int r=0;r<n;r++)
         for(int c=r+1;c<n;c++)
         if(  (ar[r].first>ar[c].first && ar[r].second<ar[c].second)  ||
             (ar[r].first<ar[c].first && ar[r].second>ar[c].second) )
           res++;
        printf("Case #%d: %d\n",_r+1,res);
    }
}
