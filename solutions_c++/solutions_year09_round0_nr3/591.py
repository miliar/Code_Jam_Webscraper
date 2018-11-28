#include <iostream>
#include <cstring>
using namespace std;
int mod = 10000;
int DP[520][21];
char o[] = "welcome to code jam"; // 19 
char s[600]; int L;
int rec (int pos, int left)
{
    if (left == 0) return 1;
    if (pos == L) return 0;
   if (DP[pos][left] != -1) return DP[pos][left];
   
      int k = 0;
     
    if (s[pos] == o[19 - left]) k+= rec (pos+1, left-1);
    if (k >= mod) k -= mod;
    
    
    k += rec (pos+1, left);
    if (k >= mod) k -= mod;
    
    return DP[pos][left] = k;
    
}
void solve (int pos)
{
    memset (DP, -1, sizeof (DP));
    gets(s);
    L = strlen(s);
   printf ("Case #%d: %04d\n", pos, rec (0, 19)); 
}
int main ()
{
    int q;
    scanf ("%d\n", &q);
    int i;
    for (i =1; i<=q; i++) solve (i);
    
    return 0;
}
