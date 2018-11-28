#include <iostream>
#include <vector>

using namespace std;

vector<int> a;

inline void solve(int testnum)
{
int n;
int totalxor = 0;
int me = 1 << 30;
long long sum = 0;
   cin >> n;
   a.resize(n);
for (int i = 0; i < n; i++)
{
cin >> a[i];
sum += a[i];
totalxor = totalxor ^ a[i];
me = min(me, a[i]);
}

if (totalxor)
{
cout << "Case #" << testnum + 1 << ": NO" << endl;
return;
}

cout << "Case #" << testnum + 1 << ": "<< sum - me << endl;
}

int num;

int main()
{
cin >> num;
for (int i = 0; i < num; i++)
{
solve(i);
}
}
