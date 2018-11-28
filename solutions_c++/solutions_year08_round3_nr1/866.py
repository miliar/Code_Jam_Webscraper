#include <iostream>
#include <math.h>

using namespace std;

const double eps = 1e-08;
const double pi = 3.1415926535897932;

long long Abs(long long x)
{
  if (x > 0)
    return x;
  else
    return -x;
}

double Abs(double x)
{
  if (x > 0)
    return x;
  else
    return -x;
}   

int main()
{
  long long i, j, ans, t_count, test, p, k, l, a[101], d, b [101], f, max, s[20], S;
  
  //freopen("input.txt", "r", stdin);
  freopen("A-small-attempt0.in", "r", stdin);  
  freopen("output.txt", "w", stdout);

  cin >> t_count;
    for (test = 0; test < t_count; test++)
  {
    cin >> p >> k >> l;
      for (j = 0; j < l; j++)
        {
          cin >> a[j];
          b[j] = -1;
        }
      for (j = 0; j < p; j++)
       s[j] = 0;
    if ((p*k)<l)
      {
        cout << "Case #" << test + 1 << ": " << "Impossible" << endl;
        break;
      }
    else
    {
      //d = p * k - l;
      for (f = 0; f < l; f++)
        {
          for (j = 0; j < l; j++)
            if (a[j] > b[f])
               {
                 max = j;
                 b[f] = a[j];
               }  
             a[max] = 0;
             //cout << b[f] << " ";
        }
      for (j = l; j < p*k; j++)
        b[j] = 0;
      d = l / p;
      //cout << d << " ";
      for (f = 0; f < p; f++)
        {
          for (j = (k*f); j < (k*(f+1)); j++)
            s[f] = s[f] + b[j];
          //cout << s[f] << " ";
        }    
      S = 0;
      for (j = 0; j < p; j++)
        S = S + s[j]*(j+1);
          
      cout << "Case #" << test + 1 << ": " << S;

      cout << endl;
    }
  }

  return 0;
}
