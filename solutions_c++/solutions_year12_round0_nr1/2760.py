#include <iostream>
using namespace std;
int main()
{
  //char reps[] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','g','r','j','g','t','h','a','q'};
  //char reps[] =   {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
  char reps[] =   {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
  int n;
  cin >> n;
  char tmp[1];
  cin.getline(tmp, 1);
  for (int i = 1; i<=n; i++)
  {
    cout << "Case #" << i << ": ";
    char chars[1000];
    cin.getline(chars, 1000);
    for (int j=0; j < 1000; j++)
    {
      if (chars[j] >= 97 && chars[j]<=122) cout << reps[chars[j]-97];
      else if (chars[j] == 32) cout << " ";
      else break;
    }
    cout << endl;
  }
}