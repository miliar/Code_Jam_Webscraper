#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

typedef unsigned int uint;

string X = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz";
string Y = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq";

int main()
{
  int ilz;
  scanf("%i\n", &ilz);
  for(int xz=1; xz<=ilz; xz++)
  {
    char s[ 1000 ];
    fgets( s, 1000, stdin );
    for(uint i=0, ssize=strlen(s); i<ssize; i++)
      for(uint j=0; j<X.size(); j++)
        if(X[j] == s[i])
        {
          s[i] = Y[j];
          break;
        }
    printf("Case #%i: %s", xz, s);
  }
  return 0;
}

