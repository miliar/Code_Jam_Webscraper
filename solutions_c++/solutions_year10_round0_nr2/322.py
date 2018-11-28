#include <cstdio>
#include <cstring>

const int NMAX = 2000, BASE = 10, CntDigits = 150;
const char zero[] = "0", e[] = "1";

struct Long
{
 int digit[CntDigits];
 int size;

 void Init()
 {
  size = 0;
  memset(digit, 0, sizeof(digit));
 }

 int &operator [](int index)
 {
  return digit[index];
 }

 void Normalize()
 {
  while (size && !digit[size - 1])
   --size;
 }

 void FromStr(const char *s)
 {
  Init();

  int len = strlen(s);
  for (int i = 0; i < len; ++i)
   digit[i] = s[len - i - 1] - '0';
  size = len;

  Normalize();
 }

 Long()
 {
  Init();
 }

 Long(const char *s)
 {  
  FromStr(s);
 }

 void Print()
 {
  if (size == 0)
  {
   printf("0");
   return;
  }

  printf("%d", digit[size - 1]);
  for (int i = size - 2; i >= 0; --i)
   printf("%d", digit[i]);
 }
};

int Max(int a, int b)
{
 return a < b ? b : a;
}

int Min(int a, int b)
{
 return a < b ? a : b;
}

bool operator <(Long &x, Long &y)
{
 int ResOfCmp = x.size - y.size;
 if (ResOfCmp)
  return ResOfCmp < 0;

 for (int i = x.size - 1; i >= 0; --i)
 {
  ResOfCmp = x[i] - y[i];
  if (ResOfCmp)
   return ResOfCmp < 0;
 }

 return false;
}

bool operator ==(Long &x, Long &y)
{
 int ResOfCmp = x.size - y.size;
 if (ResOfCmp)
  return false;

 for (int i = x.size - 1; i >= 0; --i)
 {
  ResOfCmp = x[i] - y[i];
  if (ResOfCmp)
   return false;
 }

 return true;
}

Long operator +(Long x1, Long &x2)
{
 Long y;
 int carry = 0;

 for (int i = 0; i < Max(x1.size, x2.size) || carry; ++i)
 {
  carry += x1[i] + x2[i];
  y[y.size++] = carry % BASE;
  carry /= BASE;
 }

 return y;
}

Long operator -(Long &x1, Long &x2)
{
 Long y;
 int carry = 0;

 for (int i = 0; i < Max(x1.size, x2.size); ++i)
 {
  carry += x1[i] - x2[i];
  y[y.size++] = (carry + BASE) % BASE;
  carry = (carry - BASE + 1) / BASE;
 } 

 y.Normalize();
 return y;
}

Long operator /(Long &x, const int k)
{
 Long y;
 int carry = 0;

 for (int i = x.size - 1; i >= 0; --i)
 {
  carry = carry * BASE + x[i];
  y[i] = carry / k;
  carry %= k;
 }

 y.size = x.size;
 y.Normalize();

 return y;
}

int operator %(Long &x, const int k)
{
 int carry = 0;

 for (int i = x.size - 1; i >= 0; --i)
 {
  carry = carry * BASE + x[i];
  carry %= k;
 }

 return carry;
}

Long operator *(Long &x, const int k)
{
 Long y;
 int carry = 0;

 for (int i = 0; i < x.size || carry; ++i)
 {
  carry += x[i] * k;
  y[y.size++] = carry % BASE;
  carry /= BASE;
 }

 return y;
}

Long operator *(Long &x1, Long &x2)
{
 Long y;

 for (int i = 0; i < x1.size; ++i)
 {
  int carry = 0;
  for (int j = 0; j < x2.size || carry; ++j)
  {
   carry += x1[i] * x2[j] + y[i + j];
   y[i + j] = carry % BASE;
   carry /= BASE;
  }
 }

 y.size = x1.size + x2.size;
 y.Normalize();

 return y;
}

Long GCD(Long &x1, Long &x2)
{
 Long a = x1, b = x2, y(e), buff;

 while (true)
 {
  if (a == Long(zero))
   return y * b;
  if (b == Long(zero))
   return y * a;

  int r1 = a % 2, r2 = b % 2;

  if (!r1 && !r2)
  {
   y = y * 2;
   a = a / 2;
   b = b / 2;
   continue;
  }

  if (!r1 && r2)
  {
   a = a / 2;
   continue;
  }

  if (r1 && !r2)
  {
   b = b / 2;
   continue;
  }

  if (a < b)
   buff = b - a;
  else
   buff = a - b;

  a = b;
  b = buff;
 }
}

Long operator %(Long &x1, Long &x2)
{
 Long left = Long(zero), right = x1, middle, ed = Long(e), res;

 while (left < right)
 {
  middle = (left + right + ed) / 2;
  res = middle * x2;

  if (x1 < res)
   right = middle - ed;
  else
   left = middle;
 }

 return x1 - left * x2;
}

Long a[NMAX], b[NMAX];
char s[CntDigits];


int main()
{
 freopen("input.txt", "r", stdin);
 freopen("output.txt", "w", stdout);

 int CountTest;

 scanf("%d", &CountTest);
 for (int index = 0; index < CountTest; ++index)
 {
  int n;

  scanf("%d", &n);
  for (int i = 0; i < n; ++i)
  {
   scanf("%s", s);
   a[i].FromStr(s);
  }

  Long min = a[0];
  for (int i = 1; i < n; ++i)
   if (a[i] < min)
    min = a[i];

  for (int i = 0; i < n; ++i)
  {
   b[i].Init();
   b[i] = a[i] - min;
  }

  Long d = b[0];
  for (int i = 1; i < n; ++i)
   d = GCD(d, b[i]);

  Long res = (d - a[0] % d) % d;

  printf("Case #%d: ", index + 1);
  res.Print();
  printf("\n");
 }

 return 0;
}