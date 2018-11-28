#include <iostream>
#include <vector>
#include <cassert>

typedef char Map[26];

char translate(const Map& m, char c) {
  return c == ' ' ? ' ' : m[c - 'a'];
}

std::string translate(const Map& m, const std::string& a) {
  std::string b = a;
  for(std::size_t i=0;i<a.size();i++)
	b[i] = translate(m, a[i]);
  return b;
}

void add(Map& m, char a, char b) {
  if(a == ' ')
	return;

  assert(b != ' ');
  if(char b2 = m[a - 'a']) {
	assert(b == b2);
  }
  m[a - 'a'] = b;
}

void add(Map& m, const std::string& a, const std::string& b) {
  assert(a.size() == b.size());
  for(std::size_t i=0;i<a.size();i++)
	add(m, a[i], b[i]);
}

int main()
{
  Map m;
  std::memset(m, 0, 26);
  add(m, 'y', 'a');
  add(m, 'e', 'o');
  add(m, 'q', 'z');
  add(m, 'z', 'q');
  add(m, "ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
  add(m, "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
  add(m, "de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");

  //

  int T;
  std::cin >> T;
  std::cin.get();
  for(int C=1;C<=T;C++) {
	std::string G;
	std::getline(std::cin, G);
	std::string S = translate(m, G);
	std::cout << "Case #" << C << ": " << S << "\n";
  }
  return 0;
}
