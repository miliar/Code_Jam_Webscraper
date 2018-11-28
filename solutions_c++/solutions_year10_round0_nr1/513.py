#include<iostream>
using namespace std;
int main()
{    int N,ca=0;
    long n,k;
    scanf("%d",&N);
    for(int i=0;i<N;i++)
    {cin>>n>>k;
    ca++;
     k++;
     n=1<<n;         
     printf("Case #%d: ",ca);
     if(k%n==0)
      printf("ON\n");
      else
      printf("OFF\n");                      
    }
return 0;
}
