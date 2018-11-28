#include <iostream>
using namespace std;
bool power[32];
bool on[32];
unsigned long long pow[]={1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824};
int main ()
{
    unsigned long long temp;
         #ifndef ONLINE_JUDGE
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
#endif;
    unsigned long long  t,n,k;
    cin>>t;

for(int i=1;i<=t;i++)
    {

        cin>>n>>k;
        if(((k+1)%pow[n])==0){
              cout<<"Case #"<<i<<": ON\n";
            }
            else {
            cout<<"Case #"<<i<<": OFF\n";
                }

    }

    return 0;
}


