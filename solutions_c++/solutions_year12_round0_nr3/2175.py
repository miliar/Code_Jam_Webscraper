#include <iostream>
#include <algorithm>
using namespace std;

string itos(int n)
{
  string r = "";
  while(n)
  {
    r+= (char) (n%10  + '0');
    n/=10;
  }
  int l = r.length();
  reverse(r.begin(), r.end());
  return r;
}

int pairs(int n, int b, int e)
{
  string s = itos(n);
  int len = s.length();
  const char* arr = s.c_str();
  int pairs = 0;
  int array[len];
  for(int i = 0; i<len; i++)
  {
    int num = 0;
    for(int j = 0; j<len; j++)
    {
      num = num*10 + (arr[(j+i)%len] - '0');
    }
    bool flag = true;
    if(num>=b && num <=e && num>n)
    {
      
      for(int b = 0; b<pairs; b++)
      {
	if (array[b] == num) flag = false;
      }
      if(flag)
      {
	array[pairs++] = num;
      }
    }
  } 
  return pairs;
}

int calculate(int from, int to)
{
  int c = 0;
  for(int i = from; i<=to; i++)
    c+=pairs(i,from,to);
  return c;
}


int main()
{
  int cases;
  cin >> cases;
  for(int i = 0; i<cases; i++)
  {
    int a,b;
    cin >> a >> b;
    cout << "Case #" << i+1 << ": " << calculate(a,b)<<endl;
  }
  return 0;
}