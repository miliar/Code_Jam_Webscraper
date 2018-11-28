#include <iostream>
#include <cmath>
#include <cassert>
using namespace std;


int t,c,p,l;

int pow(int x,int y)
{
int ans=1;
for(int i=1;i<=y;i++)
  ans*=x;
return ans;    
}

int main()

{
cin >>t;    
for(int tt=1;tt<=t;tt++)
  {
  cin >> l >> p >> c;
        long long tmp(1),x(0),ans(0);
        while(l * tmp * c < p){
            tmp *= c;
            ++x;
        }
        tmp = 1;
        while(tmp <= x){
            tmp *= 2;
            ++ans;
        }
        cout << "Case #" << tt << ": " << ans << endl;

  }
return 0;    
}
