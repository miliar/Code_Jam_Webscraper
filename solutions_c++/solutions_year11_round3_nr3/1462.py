#include<iostream>
using namespace std;

const int MAXN = 10 * 10 * 10 * 10 * 10;

int nums[MAXN];
int l,h,n;
 
int main()
{
    int t, test = 0;
    cin >> t;
    while(test < t)
    {
               test++;
               cout << "Case #" << test << ": ";
               
               cin >> n >> l >> h;
               for(int i = 0; i < n; i++)
                cin >> nums[i];
                
               bool flag = 0;
               for(int k = l; k <= h; k++)
               {
                flag = 0;
                for(int i = 0; i < n; i++)
                {
                  if(k % nums[i] == 0 || nums[i] % k == 0) continue;
                  else flag = 1;        
                }
                if(flag == 0)
                {
                        cout << k << endl;
                        break;
                }
               }
               
               if(flag == 1)
               {
                       cout << "NO\n";
               }
    }
    return 0;
}
