#include <iostream>
#include <math.h>

using namespace std;

double eps = 1e-7;
double pi = 3.1415296535897932;

int mas[1000];

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

int isprime(int n)
{
  int i;

  for (i = 2; i <= n / 2; i++)
    if (n % i == 0)
      return 0;

  return 1;
}

int findp(int n)
{
  int i;
  int ans = 0;

  for (i = 2; i <= n; i++)
    if (isprime(i))
      ans++;

  return ans;
}

int isgood(int n, int p)
{
  int i;

  for (i = 2; i <= p; i++)
    if (n % i == 0)
      return 0;

  return 1;
}

int getgroup(int n, int p)
{
  int i, d;

  d = sqrt(n + 1) + 1;

  for (i = p; i <= n; i++)
    if (n % i == 0 && isprime(i))
      return i;

  return n;
}

int color[100000], a, b, p;

int parse(int a, int b)
{
  int i;

  for (i = p; i <= a; i++)
    if (a % i == 0 && b % i == 0)
      if (isprime(i))
        return 1;

  return 0;
}

void paint(int v, int c)
{
  int i;

  color[v] = c;

  for (i = a; i <= b; i++)
    if (color[i] == 0)
      if (parse(v, i))
        paint(i, c);
}
     
int main()
{
  long long i, j, t_count, test, n, m, tmp, ans;
  int c;

  freopen("B-small.in", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> t_count;
  for (test = 0; test < t_count; test++)
  {
    cout << "Case #" << test + 1 << ": ";

    cin >> a >> b >> p;

/*
//    ans = findp(p);
    ans = 0;
    memset(mas, 0, sizeof(mas));

    for (i = a; i <= b; i++)
    {
      cout << i << " : " <<  getgroup(i, p) << endl;
      mas[getgroup(i, p)]++;
    }

    for (i = 0; i <= b; i++)
      if (mas[i] > 0)
      {
//        cout << i << endl;
        ans++;
      }*/

    c = 1;
    memset(color, 0, sizeof(color));
//    color[a] = 1;

    for (i = a; i <= b; i++)
    {
      if (color[i] == 0)
      {
        paint(i, c);
        c++;
      }

//      cout << i << ' ' << color[i] << endl;
    }


    ans = c - 1;
    cout << ans << endl;

  }

  return 0;
}