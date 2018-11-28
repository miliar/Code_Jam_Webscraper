#include<iostream>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    int n;
    cin >> n;
    int a, b;
    for (int i = 1; i <= n; i++)
    {
          cin >> a >> b;
          if ((b+1) % (1<<a)) cout << "Case #" << i << ": OFF\n";
          else cout << "Case #" << i << ": ON\n";
    }
    return 0;
}
