#include <cstdlib>
#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

int mas[100][1001];
int main()
{    
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);  
    int t,n,temp;
    int count_i,count;
    cin>>t;
    for(int i = 0; i < t; i++)
    {
     cin>>n;
     for( int j = 1; j <= n; j++)
     {
      cin>>mas[i][j];
     }
     count = 0;
     count_i = 0;
     if(n > 1)
     {
     for( int j = 1; j <= n; j++)
     {
      if( mas[i][j] == j)
       count_i++;
      else
       if( mas[i][mas[i][j]] == j)
        count++;
     }
     n-=count_i;
     cout<<"Case #"<<i+1<<": "<<n<<".000000"<<endl;
     }
     else
     {
      cout<<"Case #"<<i+1<<": "<<0<<".000000"<<endl;
     }
    }
    return 0;
}
