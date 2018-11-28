#include<iostream>
#include<set>
#include<vector>
using namespace std;
int dig;
int pow;
int total;
int rotate(int &m, int &n)
{
  set<int> myset;
  set<int>::iterator it;
  pair<set<int>::iterator,bool> ret;
  int m1 = m,pricti;
  for (int i = 1; i < dig; ++i)
  {
    pricti = (m1%10)*pow;
    pricti += m1/10;
    m1 = pricti;
    ret = myset.insert(m1);
    if ((m1 > m) && (m1 <= n) && ret.second)
      ++total;
  }
}
int main()
{
  int T,A,B;
  cin >> T;
  for (int i = 1; i <= T ; ++i)
  {
    total = 0;
    cin >> A >> B;
    if (A < 10){dig = 1;pow = 1;}
    else if (A < 100){dig = 2;pow = 10;}
    else if (A < 1000) {dig = 3; pow = 100;}
    else if (A < 10000) {dig = 4; pow = 1000;}
    else if (A < 100000) {dig = 5; pow = 10000;}
    else if (A < 1000000) {dig = 6; pow = 100000;}
    else {dig = 7; pow = 1000000;}
    for (int j = A; j < B; ++j)
      rotate(j,B);
    cout << "Case #" << i << ": " << total << endl;
  }
  return 0;
}
