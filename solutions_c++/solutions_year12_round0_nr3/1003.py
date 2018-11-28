#include<iostream>

using namespace std;

int ll, ul;
int numbers[3000000];

int count_digits(int n)
{
  int _count_digits = 0;
  for(n; n; n/=10) _count_digits ++;
  return _count_digits;
}
int power(int base, int exp)
{
  int n = 1;
  while(exp)
    {
      n*=base;
      exp--;
    }
  return n;
}
int mark_all(int n)
{
  int i,j,k;
  int copy_n = n;
  int cd = count_digits(n);
  if (cd <=1) return 0;
  int count = 0;
  int remainder, divident, new_number, x=n;
  do {
    //    cout << "in this loop" << endl;
    remainder = x%10;
    divident = x/10;
    x = new_number = remainder * power(10,cd-1) + divident;
    if(count_digits(new_number) != cd) continue;
    if (ll <= new_number && new_number <=ul)
      numbers[new_number] = 1, count ++;
  } while (x!=n);

  //  cout << "For " << n << " marked = " << count << endl;

  return (count*(count-1))/2;

}
int solve()
{
  int i,j,k, count =0;
  count = 0;
  for(i=ll;i<=ul;i++)
    numbers[i] = 0;
  for(i=ll;i<=ul;i++)
    {
      if (numbers[i]) 
	continue;
      else 
	count += mark_all(i);
    }
  return count;
}


int main()
{
  int n;
  int i,j,k;
  cin >> n;
  for(i=0;i<n;i++)
    {
      cin >> ll >> ul;
      cout << "Case #" << i+1 << ": " << solve() << endl;;
    }

    
}
