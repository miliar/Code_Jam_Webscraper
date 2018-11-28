#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
  const string  in("ejp mysljylc kd kxveddknmc re jsicpdrysi"
                   "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
                   "de kr kd eoya kw aej tysr re ujdr lkgc jvzq");
  const string out("our language is impossible to understand"
                   "there are twenty six factorial possibilities"
                   "so it is okay if you want to just give upqz");

  string sn;
  getline(cin, sn);
  const int n = stoi(sn);
  for(int i=0; i<n; ++i)
  {
    string sq;
    getline(cin, sq);
    cout << "Case #" << i+1 << ": ";
    for(auto c: sq)
    {
      cout << out[in.find_first_of(c)];
    }
    cout << endl;
  }

  return 0;
}

