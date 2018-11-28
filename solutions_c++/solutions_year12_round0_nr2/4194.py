#include <iostream>
using namespace std;
int main() {
int t, n, s, p, m, c=0;
cin >> t;
for (int i=1; i<=t;i++)
{cin >> n >> s >> p;
for (int j=0; j<n; j++)
{cin >>m; if (m>=(3*p-2)) {c++;} else if (m>=(3*p-4)&&p!=1) {if (s>0) {s--;c++;}}}
cout << "Case #" << i << ": " << c << endl; c=0;}}
