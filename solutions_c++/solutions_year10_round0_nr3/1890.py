#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
pair<int,long long> pre[1001];
int ar[1001];
void calc(int n,int R)
{
   for(int r=0;r<n;r++)   
    {
      int long long cont=0,pos=0;
      for(int c=0;c<n;c++)   
       {
           int a=(c+r)%n;
           if(  cont+ar[a]<=R )     
            cont+=ar[a],pos++;
           else
            break;
       }
       pre[r]=make_pair(pos,cont);
    }
}
int main()
{
    int T;
    scanf("%d",&T);
    for(int r=0;r<T;r++)   
     {
        int R,k,n,pos=0;
        long long res=0;
        scanf("%d%d%d",&R,&k,&n);
        for(int c=0;c<n;c++)     
         scanf("%d",&ar[c]);
        calc(n,k);
        for(int c=0;c<R;c++)         
        {
         res+=pre[pos].second;
         pos=(pos+pre[pos].first)%n;
        }
        printf("Case #%d: ",r+1);
        cout <<res<<endl;
     }
}
