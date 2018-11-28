#include <iostream>
#include<math.h>
using namespace std;
bool power[32];
bool on[32];

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
        if(((k+1)%(long long )pow(2,n))==0){
              cout<<"Case #"<<i<<": ON\n";
            }
            else {
            cout<<"Case #"<<i<<": OFF\n";
                }

    }

    return 0;
}


