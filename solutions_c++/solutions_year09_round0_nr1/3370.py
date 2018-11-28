#include <iostream>
#include <fstream>
#include <ext/hash_set>
#include <string>

namespace __gnu_cxx
{
  template <>
  struct hash<std::string>
  {
    size_t operator()(const std::string& s) const
    {
      return hash<const char*>()(s.c_str());
    }
  };


}

int resolv(const std::string& s, int pos, const std::string& to_test, const __gnu_cxx::hash_set<std::string>& words, const __gnu_cxx::hash_set<std::string>& swords)
{
  if (pos >= s.size())
    if (words.find(to_test) != words.end())
      return 1;

  if (s[pos] != '(')
  {
    std::string s_ = to_test + s[pos];
    if (swords.find(s_) != swords.end())
      return resolv(s, pos + 1, s_, words, swords);
  }

  int end;
  for (end = pos; end < s.size(); ++end)
    if (s[end] == ')')
      break;

  int sum = 0;
  for (int i = pos; i < end; ++i)
  {
    std::string s_ = to_test + s[i];
    if (swords.find(s_) != swords.end())
      sum += resolv(s, end + 1, s_, words, swords);
  }

  return sum;
}

void resolv(const std::string& s, const __gnu_cxx::hash_set<std::string>& words, const __gnu_cxx::hash_set<std::string>& swords, int test)
{
  int r = resolv(s, 0, "", words, swords);
  std::cout << "Case #" << test << ": " << r << std::endl;
}



int main(int argc, char** argv)
{
  std::ifstream f(argv[1]);
  if (!f.is_open())
    return -1;

  int L, D, N;
  __gnu_cxx::hash_set<std::string> words;
  __gnu_cxx::hash_set<std::string> swords;

  f >> L >> D >> N;

  for (int i = 0; i < D; ++i)
  {
    std::string s;
    f >> s;
    for (int i = 1; i < s.size() + 1; ++i)
    {
      swords.insert(s.substr(0, i));
    }
    words.insert(s);
  }

  for (int i = 0; i < N; ++i)
  {
    std::string s;
    f >> s;
    resolv(s, words, swords, i + 1);
  }
}
