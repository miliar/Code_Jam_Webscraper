#include <iostream>
#include <cstring>

using namespace std;

char *text1="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";

char *text2="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char mapping[30];
char line[3000];

int main()
{
  mapping['q'-'a'] = 'z';
  mapping['z'-'a'] = 'q';
  for (int i=0; i<strlen(text1); i++)
    {
      mapping[text1[i]-'a'] = text2[i];
    }

  // for (char c='a'; c<='z'; c++)
  //   cout << c << " --> " << mapping[c-'a'] << endl;

  int N;
  cin >> N;
  cin.getline(line, 3000);
  for (int n=0; n<N; n++)
    {
      cin.getline(line, 3000);
      cout << "Case #" << n+1 << ": ";
      for (int i=0; i<strlen(line); i++)
	if (line[i] >= 'a' && line[i] <= 'z')
	  cout << mapping[line[i]-'a'];
	else
	  cout << line[i];
      cout << endl;
    }

  return 0;
}
