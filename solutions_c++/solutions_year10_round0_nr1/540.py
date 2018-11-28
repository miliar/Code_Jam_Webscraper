
#include <iostream>

using namespace std;

int ar[32];
int n,tc,k;

int main()
{
 ar[0] = 1;
 int i;
 for(i=1;i<32;i++) ar[i] = ar[i-1]*2;
 
 cin >> tc;
 for(i=0;i<tc;i++)
  {
   cin >> n >> k;
   cout << "Case #" << i+1 << ": ";
   k = k%ar[n];
   if(ar[n]-1==k) cout << "ON" << endl; else cout << "OFF" << endl;
  }
}
