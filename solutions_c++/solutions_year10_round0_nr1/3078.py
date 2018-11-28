#include<iostream>
#include<algorithm>
#include<vector>
#include<stdio.h>
#include<cmath>
#include<math.h>

using namespace std;

typedef long double ll;

ll n,N,K;
long int val,chk;
int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("A-large-output.out","wt",stdout);
    cin>>n;
    for(int i=0;i<n;i++)
    {
              cin>>N>>K;
              printf("Case #%d: ",(i+1));
              val=(long int)pow(2,N);
              chk=val-1;
              if((long int)K%val==chk)
              cout<<"ON"<<endl;
              else
              cout<<"OFF"<<endl;
    }              
}

    
