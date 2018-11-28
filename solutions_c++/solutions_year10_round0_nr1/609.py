#include<cstdio>
#include<iostream>
#include<string.h>
#include<algorithm>

using namespace std;

int n,K;

int bit[33];
int main()
{
    int ncase;
    int i,J,k;
    
    for(i = 0;i < 32;i++) bit[i] = 1<<i;
    
    freopen("A-large.in.txt","r",stdin);
    freopen("a.txt","w",stdout);
    int casenum = 1;
    cin>>ncase;
    while(ncase--)
    {
          cin>>n>>K;
          K++;
          printf("Case #%d: ",casenum++);
          K = K % bit[n];
          if( K == 0 )
          printf("ON\n");
          else
          printf("OFF\n");
    }
   // system("pause");
    return 0;
}
