#include <iostream>
#include <math.h>

using namespace std;

double eps = 1e-7;
double pi = 3.1415296535897932;

double Abs(double x)
{
  if (x > 0)
    return x;
  else
    return -x;
}

double Abs(int x)
{
  if (x > 0)
    return x;
  else
    return -x;
}


int k, n;
int q[100000];

int mas[6000];
        
int main()
{
  long long i, j, t_count, test, n, m, tmp, col, pos, was, s;

  freopen("C-small.in", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> t_count;
  for (test = 0; test < t_count; test++)
  {
    cout << "Case #" << test + 1 << ": ";
       
    cin >> k >> n;
    for (i = 0; i < n; i++)
      cin >> q[i];


    memset(mas, 0, sizeof(mas));

//    for (i = 1; i <= k; i++)

    was = k;
    pos = 0;
    for (i = 0; i < k; i++)
    {
      col = 0;     
      
      if (i >= was)
        col += i - i % was;

      while (col <= i)
      {
        while (mas[pos] != 0)
        {
          pos = (pos + 1) % k;
        }

        col++;
        if (col <= i)
          pos++;
        pos = pos % k;
      }

      mas[pos] = i + 1;
//      cout << i << ' ' << pos << endl;
//      return 0;
      was--;
    }

    for (i = 0; i < n; i++)
      cout << mas[q[i] - 1] << ' ';
    cout << endl;
  }

  return 0;
}