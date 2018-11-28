#include <array>
#include <iostream>
#include <string>

using namespace std;

int main (int argc, char* argv[])
{
  array<string, 3> encoded = {
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"
  };

  array<string, 3> decoded = {
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"
  };

  array<char, 26> map;

  for (int a=0, b=encoded.size(); a<b; a++) {
    for (int i=0, j=encoded[a].size(); i<j; i++) {
      map[(int)(encoded[a][i]-'a')] = decoded[a][i];
    }
  }

  map['q'-'a'] = 'z';
  map['z'-'a'] = 'q';
  
  string encoded_message; string decoded_message;
  int k = 1;
  getline(cin, encoded_message);

  while (getline(cin, encoded_message)) {
    decoded_message = "";

    for (int i=0, j=encoded_message.length(); i<j; i++) {
      if (encoded_message[i] == ' ') {
        decoded_message.push_back(' ');
      } else {
        decoded_message.push_back(map[(int)(encoded_message[i] - 'a')]);
      }
    }

    cout << "Case #" << k++ << ": " << decoded_message << endl;
  }

  return 0;
}
