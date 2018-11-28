#include <iostream>

using namespace std;

int main()
{
  int T,N,K;
  cin >> T;
  for (int t=0; t<T; t++)
    {
      cin >> N >> K;

      cout << "Case #" << t+1 << ": ";

      bool ok=true;
      for (int n=0; n<N; n++)
	if (!(K&(1<<n)))
	  ok=false;

      if (ok)
	cout << "ON";
      else
	cout << "OFF";

      cout << endl;
    }

  return 0;
}
