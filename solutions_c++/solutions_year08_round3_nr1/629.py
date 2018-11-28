#include <iostream>
using namespace std;

int n, p , k , l;

int let[1000+1];
void readIn()
{
   cin >> p >> k >> l;
   for(int i = 1; i <=l ; i++)
      cin >> let[i];
}
bool cmp(const int& a, const int & b)
{
   return a > b;
}
void work(int cases)
{
   sort(let+1, let + l + 1, cmp);
   int t = 0;
   int ans = 0;
   for(int i = 1; i <= l; i++)
   {
       if(i%k == 1) t++; 
       ans += t*let[i];
   }
   cout << "Case #" << cases << ": " << ans << endl;
}
int main()
{
      freopen("A-small-attempt0.in","r", stdin);
      freopen("A-small-attempt0.out","w",stdout);
   cin >> n;
   for(int i = 1; i <= n; i++)
   {
      readIn();
      work(i);
   }
   return 0;
}
