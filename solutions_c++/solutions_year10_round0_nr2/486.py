#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

long long gcd(long a, long b){
     
    if(a == 0 || b == 0)return a + b; 
    while( (a%=b) && (b%=a) );
    return a+b;
}

int main()
{
   //freopen("B-small-attempt1.in","r",stdin);
   //freopen("out.txt","w",stdout);
   int cs , N ;
   long long a[3] , GCD , maxv;
    
   scanf("%d",&cs);
   for(int c=1;c<=cs;c++)
   {
        scanf("%d",&N);
        for(int i=0;i<N;i++)cin >> a[i];
        sort(a , a+N);
        
        if(N == 3)//0,1,2
        {
             GCD = gcd( a[2] - a[0] , gcd( a[2] - a[1] , a[1] - a[0]) );
             maxv = GCD * ( a[2] / GCD ); 
             if(maxv < a[2])maxv += GCD;
             maxv -= a[2]; 
        }
        else if(N == 2)
        {
             GCD = a[1] - a[0];
             maxv = GCD * ( a[1] / GCD ); 
             if(maxv < a[1])maxv += GCD;
             maxv -= a[1]; 
        }   
        END: 
        cout << "Case #" << c << ": " << maxv << endl;   
   }
   return 0;
}
