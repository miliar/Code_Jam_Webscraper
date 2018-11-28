#include <iostream>
#include <map>
#include <string>
#include <boost/foreach.hpp>

using namespace std;

class CharMap : public map<char , char> // google / english
{
};

static int matchCount = 0;
bool make(string goo, string eng, CharMap& charMap)
{
  int i = 0;
  BOOST_FOREACH(char gooChar, goo)
  {
    if (gooChar == ' ')
    {
      i++;
      continue;
    }
    char engChar = eng[i++];
    if (charMap[gooChar] != '\0')
    {
      if (charMap[gooChar] != engChar)
      {
        cout << " match fail " << gooChar << " " << engChar << endl;
        return false;
      }
      continue;
    }
    charMap[gooChar] = engChar;
    matchCount++;
    // cout << gooChar << " " << engChar << " " << matchCount << endl; // gilgil temp
  }
  return true;
}

bool debug(CharMap& charMap)
{
  bool res = true;
  for (char gooChar = 'a'; gooChar <= 'z'; gooChar++)
  {
    char engChar = charMap[gooChar];
    if (engChar == '\0')
    {
      cout << "no match " << gooChar << endl; // gilgil temp
      res = false;
    }
    // cout << gooChar << " " << engChar << endl; // gilgil temp
  }
  return res;
}

string translate(string goo, CharMap& charMap)
{
  string res;
  BOOST_FOREACH(char gooChar, goo)
  {
    if (gooChar == ' ')
    {
      res += ' ';
      continue;
    }
    char engChar = charMap[gooChar];

    res += engChar;
  }
  return res;
}

int main()
{
  CharMap charMap;

  charMap['y'] = 'a';
  charMap['e'] = 'o';
  charMap['z'] = 'q';

  {
    string goo = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string eng = "our language is impossible to understand";
    if (!make(goo, eng, charMap)) return -1;
  }

  {
    string goo = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    string eng = "there are twenty six factorial possibilities";
    if (!make(goo, eng, charMap)) return -1;
  }

  {
    string goo = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string eng = "so it is okay if you want to just give up";
    if (!make(goo, eng, charMap)) return -1;
  }

  charMap['q'] = 'z'; // unregistered char

  if (!debug(charMap)) return -1;

  int T; cin >> T;
  string dummy; getline(cin, dummy);
  for (int t = 1; t <= T; t++)
  {
    string goo;
    getline(cin, goo);
    // cout << "goo=" << goo << endl; // gilgil temp
    string eng = translate(goo, charMap);
    cout << "Case #" << t << ": " << eng << endl;
  }
}