#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
#define MAXI(a,b) ((a>b)?(a):(b))
#define MINI(a,b) ((a<b)?(a):(b))

#define MAX 1005
bool prime[MAX];


int gcd(int x,int y)
    {
    if(y==0) return x;
    else return gcd(y,x%y);
    }
    
int gpf(int x)
    {
        int g=1;
    for(int i=1;i<=(x/2);i++)
           if((x%i)==0) g=i; 
    return g;
    }
    
bool isprime(int c)
    {
    for(int i=2;i<=(c/2);i++)
            if((c%i)==0) return 0;
    return 1;
    }

bool ss(int a,int b,int p)
    {
        for(int i=p;i<=MINI(a,b);i++)
            {
            if( prime[i] && ((a%i)==0 ) &&((b%i)==0 )) return 1;    
            }
    return false;
    }
    
#define MAX1 110
    
int main()
{
   long long cas , n, m, X, Y , Z ; 
    cin>>cas;
    int A[MAX1];
    int lt[MAX];
    long long dp[MAX];
    
 for(int i=1;i<=cas;i++)   
    {
    cin>>n >> m >> X >> Y >> Z ;    
    for(int j=0;j<m;j++) cin>>A[j];    

  //  for(int j=0;j<m;j++) cout<<A[j]<<" ";    
  //  cout<<endl;
    
    int val=A[0];
    
    for(int k=0;k<n;k++) 
            {
        //    cout<<A[k%m]<<" ::-> "<<k%m<<" ";
            lt[k]=A[k%m];
            A[k%m]=(X *A[k%m] + Y * (k + 1) )  %Z ;
            }
//    cout<<endl;
    
    //   for(int k=0;k<n;k++)  cout<<lt[k]<<" ";
    //   cout<<endl;
//    cout<<"There are "<< n<<" elements "<<endl;
    
    for(int k=0;k<n;k++) dp[k]=1;
    
        for(int k=0;k<n;k++)
            for(int h=k+1;h<n;h++)
                {
                 if(lt[h]>lt[k]) dp[h]+=dp[k];   
                dp[h]%=1000000007;
                 dp[k]%=1000000007;
                }

    long long ans=0;
    
        for(int k=0;k<n;k++) { //cout<<dp[k]<<" ";
                            ans+=dp[k];
                             ans%=1000000007;
                            }
  //      cout<<endl;
    cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    
return 0;
}
