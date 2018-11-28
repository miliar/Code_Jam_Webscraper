#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int T;
  cin>>T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #"<<t<<": ";
    int N, L, H;
    cin>>N;
    cin>>L;
    cin>>H;
    int* a = new int[N];
    for (int i = 0; i < N;i++)
    {
      cin >>a[i];
    }
    bool found = false;
    for (int j = L; j <= H; j++)
    {
      int good = 0;
      for (int i = 0; i < N; i++)
      {
        if ((a[i] > j && (a[i] % j == 0))||(j >= a[i] && (j % a[i] == 0)))
          good++;
      }

      if (good == N) 
      {
        cout<<j<<endl;
        found = true;
        break;
      }
    }
    if (!found) cout<<"NO"<<endl;
  }

  return 0;
}