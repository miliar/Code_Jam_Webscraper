#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
int dig;
int getDigit(int a)
{
    int c = 0;
    while ( a ){
        c++;
        a/=10;   
    }   
    return c;
}

int exp(int a,int b)
{
    int ans = 1;
    for(int i=0;i<b;i++)
        ans*=a;
       return ans;   
}

void turn(int& n)
{
    int ten = 10;
    int p = exp(10,dig)/10;
    while ( n%ten == 0 ){
        ten *= 10;
        p /= 10;   
    }
    n = (n%ten)*p + ( n/ten );
    
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("Clarge.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int I=1;I<=T;++I){
        int a,b;
        scanf("%d%d",&a,&b);
        long long int ans = 0;
        dig = getDigit(a);
        for ( int i=a;i<=b;i++){
            
            int tmp = i;
            while ( turn(tmp),tmp != i ){
                if ( tmp > i && tmp <= b){
                    ans++;   
                    
                }
            }
        }
        printf("Case #%d: %lld\n",I,ans); 
    }
    return 0;   
}
