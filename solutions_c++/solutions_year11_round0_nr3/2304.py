#include<iostream>
using namespace std;

void solve(int t)
{
int i, N;
long c;
cin >> N;

long min = 1000000, sum =0, psum =0;
for(i=0;i<N;i++)
{
cin >> c;
if(c<min) min = c;
sum += c;
psum ^= c;
}
cout << "Case #" << t << ": ";
if (psum) cout << "NO" << endl;
else
cout << (sum - min) << endl;
}

int main()
{
int i, T;
cin >> T;
for(i=1;i<=T;i++)solve(i);
}
