/* Author       :        Arpit Sood
 * Algorithm    :        
 * */
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <cmath>
#include <climits>

using namespace std;

#define FOR(i,a,b) for(int i = (a) ; i < (b) ; i ++ ) 
#define FOR0(i,a) for(int i = 0 ; i < (a) ; i ++ ) 
#define FOR1(i,a) for(int i = 1 ; i < (a) ; i ++ )
#define REP(i,a,b,c) for(int i = (a) ; i < (b) ; i+= (c) ) 
#define PRINT printf 
#define PB push_back
#define MP make_pair
#define all(c) (c).begin(),(c).end()
#define present(c,x) (find(all(c),x) != (c).end())
#define SQ(x) (x)*(x)
#define INF 0xffffff00
#define ESP 1e-6
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define MININ(a) *min_element(a.begin(), a.end())
#define MININ_A(a,n) *min_element(a, a+n)
#define MAXIN(a) *max_element(a.begin(), a.end())
#define MAXIN_A(a,n) *max_element(a, a+n)

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef vector<int> vi;

// Unlike lower_bound, upper_bound function does not return an 
// iterator to the element if it compares equivalent to value,
// but only if it compares strictly greater.

bool comparator(const ii& left, const ii& right)
{
    if(left.second == right.second)
        return left.first < left.second;
    
    return left.second < right.second;
}

int main()
{
       int n, k, c, t, cnt = 0;
       int s, p;
       int arr[101];
       cin >> t;
       while(t--)
       {
           cnt ++;
           int ans = 0;
           cin >> n >> s >> p; //n = number of googlers, s = surprising, p = best result
           FOR0(i, n)
               cin >> arr[i];

           sort(arr, arr+n);

           FOR0(i, n)
           {
               if(arr[i] == 0 || arr[i] == 1)
               {
                   if(arr[i] >= p)
                       ans++;
                   continue;
               }
               if(s > 0)
               {
                   if(arr[i]%3 == 0)
                   {
                       c = arr[i]/3 + 1;
                       if(c >= p)
                       {
                           ans++;
                           s--;
                       }
//                       cout << "arr[i] " << arr[i] << " c " << c << endl;
                   }
                   else if((arr[i] - 1)%3 == 0)
                   {
                       c = (arr[i] + 2) / 3;
                       if(c >= p)
                       {
                           ans++;
                           s--;
                       }
  //                     cout << "arr[i] " << arr[i] << " c " << c << endl;
                   }
                   else if((arr[i] - 2)%3 == 0)
                   {
                       c = (arr[i] + 4) / 3;
                       if(c >= p)
                       {
                           ans++;
                           s--;
                       }
    //                   cout << "arr[i] " << arr[i] << " c " << c << endl;
                   }
               }
               else
               {
                   if(arr[i]%3 == 0)
                   {
                       c = arr[i] / 3;
                       if(c >= p)
                           ans++;
                   }
                   else if((arr[i] - 1)%3 == 0)
                   {
                       c = (arr[i] + 2) / 3;
                       if(c >= p)
                           ans++;
                   }
                   else if((arr[i] - 2)%3 == 0)
                   {
                       c = (arr[i] + 1) / 3;
                       if(c >= p)
                           ans++;
                   }
               }
           }
           cout << "Case #" << cnt << ": " <<  ans << endl;
       }

       return 0;
}
