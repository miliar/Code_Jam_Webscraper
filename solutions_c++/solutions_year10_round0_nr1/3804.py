#include <iostream>
#include <stdio.h>
using namespace std;

long long int k;
int t,n;
long long int vec[31] = {};
long long int pot[50];
int main() {
    scanf("%d",&t);
    
    long long int val = 1;
    for (int j=1;j<=30;j++,val*=2)
        vec[j] = vec[j-1] + val , pot[j] = val;
    pot[31] = pot[30] * 2;
    for (int l=1;l<=t;l++) {
        scanf("%d %lld",&n,&k);
        
        string s = "ON";
        if (k >= vec[n]) {
           long long int valor = k - vec[n];
           if ((valor % (pot[n+1])) != 0)
              s = "OFF";
        }
        else
            s = "OFF";
        
        printf("Case #%d: %s\n",l,s.c_str());
    }
    return 0;
}
