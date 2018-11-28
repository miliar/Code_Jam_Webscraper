#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;
typedef long long LL;

int main()
{
  freopen("C-large.in.txt","r",stdin);
  freopen("C-large.out","w",stdout);
  LL l,t,n,k,x,i,d,c;
    // char c;
  char dump;
    //  scanf("%d",&t);
  cin >> t;
  
  for (l=0;l<t;l++)
  {
    cin >> n;
    vector<LL> v(n);
    for (int i = 0; i < n; i++)
    {
      cin >> v[i];
    }
    sort(v.begin(), v.end());
    LL xorSum, sum, min;
    min = v[0];
    xorSum = min;
    sum = 0;
    for (int i = 1; i < n; i++)
    {
      xorSum ^= v[i];
      sum += v[i];
    }
    cout << "Case #" << l+1 << ": ";
    if (xorSum != 0)
    {
      cout << "NO" << endl;
    }
    else
    {
      cout << sum << endl;
    }
  }  
	return 0;
}


