#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int t, x;
int P, K, L;
int letter[1005];

void solve()
{
     scanf("%d %d %d", &P, &K, &L);
     for (int i = 0; i < L; i++)
     {
         scanf("%d",&letter[i]);
         letter[i] = -letter[i];
     }  
     sort(letter, letter + L);  
  
     int z = 1, ans = 0;
     for (int i = 0; i < L; )
     {
         int y = 0;
         while (y < K && i < L) {y++; ans += -letter[i] * z; i++;}   
         z++;
     }    
     cout << "Case #" << ++x << ": " << ans << endl;
}  

   

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    while (t--)
    {
        solve();
    }  
}    
