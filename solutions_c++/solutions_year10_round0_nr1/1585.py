#include <iostream>
using namespace std;
int main(void)
{
freopen("A-large2.in","r",stdin);
freopen("A-large2.out","w",stdout);

  int T,n,k;
  cin >> T;
  for (int t = 1;t <= T;t++)
  {
    cin >> n >> k;
    bool flag = true;
    for (int i = 0;i < n;i++)
      if ((k & (1<<i)) == 0)
        flag = false;
    printf("Case #%d: ",t);
    if (flag)
      puts("ON");
    else
      puts("OFF");
  }
}
