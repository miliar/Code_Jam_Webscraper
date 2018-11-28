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

int main()
{
  freopen("B-large.in.txt","r",stdin);
  freopen("B-large.out","w",stdout);
  int l,t,n,k,x,i,d,c;
  // char c;
  char dump;
    //  scanf("%d",&t);
  cin >> t;
  for (l=0;l<t;l++)
  {
      // scanf("%d", &n);
    cin >> c;
    string s1, s2, s3, temp;
    for (int i = 0; i < c; i++)
    {  
      cin >> temp;
      s1 += temp;
    }
    cin >> d;
    for (int i = 0; i < d; i++)
    {
      cin >> temp;
      s2 += temp;
    }
    cin >> n;
    cin >> s3;
    // cout << s1 << " " << s2 << " " << s3 << endl;
    for (int i = 0; i < s3.size(); i++)
    {
      if (i > 0)
      {
        for (int j = 0; j < 3*c; j++)
        {
          if (j%3 == 0 && s1[j] == s3[i] && s1[j+1] == s3[i-1])
          {
            s3[i] = s1[j+2];
            s3.erase(i-1, 1);
            i--;
            break;
          }
          else if (j%3 == 1 && s1[j] == s3[i] && s1[j-1] == s3[i-1])
          {
            s3[i] = s1[j+1];
            s3.erase(i-1,1);
            i--;
            break;
          }
        }
        for (int j = 0; j < 2*d; j++)
        {
          bool flag = false;
          if (j%2 == 0 && s2[j] == s3[i])
          {
            for (int k = 0; k < i; k++)
            {
              if (s3[k] == s2[j+1])
              {
                // s3.erase(k, i-k+1);
                // i -= i-k+1;
                s3.erase(0, i+1);
                i = -1;
                flag = true;
                break;
              }
            }
          }
          else if (j%2 == 1 && s2[j] == s3[i])
          {
            for (int k = 0; k < i; k++)
            {
              if (s3[k] == s2[j-1])
              {
                // s3.erase(k, i-k+1);
                // i -= i-k+1;
                s3.erase(0,i+1);
                i = -1;
                flag = true;
                break;
              }
            }
          }
          if (flag)
          {
            break;
          }
        }
      }
    }
    cout << "Case #" << l+1 << ": [";
    for (int i = 0; i < s3.size(); i++)
    {
      cout << s3[i];
      if (i < s3.size() - 1)
      {
        cout << ", ";
      }
    }
    cout << "]" << endl;
  }
	return 0;
}

