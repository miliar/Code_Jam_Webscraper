// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <string>
#include <iostream>

using namespace std;

const char c[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
const char m[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

int mapping[26];
int reverse_mapping[26];

void add_mapping(char from, char to) {
  mapping[from - 'a'] = to;
  reverse_mapping[to - 'a'] = from;
}

int _tmain(int argc, _TCHAR* argv[])
{
  for (int i = 0; i < 26; ++i) {
    mapping[i] = -1;
    reverse_mapping[i] = -1;
  }

  for (int i = 0; i < strlen(c); ++i) {
    if (c[i] != ' ')
      add_mapping(c[i], m[i]);
  }

  add_mapping('y', 'a');
  add_mapping('e', 'o');
  add_mapping('q', 'z');

  int unknown = 0;
  for (int i = 0; i < 26; ++i) {
    if (mapping[i] == -1) {
      unknown++;
    }
  }

  if (unknown == 1) {
    for (int i = 0; i < 26; ++i) {
      if (mapping[i] == -1) {
        for (int j = 0; j < 26; ++j) {
          if (reverse_mapping[j] == -1) {
            mapping[i] = 'a' + j;
            reverse_mapping[j] = 'a' + i;
            goto DONE;
          }
        }
      }
    }
  }
  DONE:;

  for (int i = 0; i < 26; ++i) {
    if (mapping[i] == -1) {
      printf("unknown mapping: %c\n", 'a' + i);
    }
  }

  int num_tests;
  cin >> num_tests;
  string s;
  getline(cin, s);
  for (int i = 0; i < num_tests; ++i) {
    getline(cin, s);
    printf("Case #%d: ", i+1);
    for (int j = 0; j < s.size(); ++j) {
      printf("%c", s[j] == ' ' ? ' ' : mapping[s[j] - 'a']);
    }
    printf("\n");
  }

	return 0;
}

