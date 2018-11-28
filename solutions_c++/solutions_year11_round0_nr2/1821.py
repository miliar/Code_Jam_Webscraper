#include <string>
#include <iostream>
#include <cstring>

char combine[26][26];
bool oppose[26][26];
int present[26];

std::string list;

std::string read_data()
{
  std::memset(combine, 0, sizeof(combine));
  std::memset(oppose, 0, sizeof(oppose));
  std::memset(present, 0, sizeof(present));
  list.clear();
  int C;
  std::cin >> C;
  std::string word;
  for ( int i=0; i<C; ++i )
  {
    std::cin >> word;
    combine[word[0] - 'A'][word[1] - 'A'] = word[2];
    combine[word[1] - 'A'][word[0] - 'A'] = word[2];
  }
  int D;
  std::cin >> D;
  for ( int i=0; i<D; ++i )
  {
    std::cin >> word;
    oppose[word[0] - 'A'][word[1] - 'A'] = true;
    oppose[word[1] - 'A'][word[0] - 'A'] = true;
  }
  std::cin >> D;
  std::cin >> word;
  return word;
}


void simulate(std::string const &word)
{
  for ( size_t i=0; i<word.length(); ++i )
  {
    if ( not list.empty() )
    {
      char last = list[list.length() - 1];
      char cmb = combine[last - 'A'][word[i] - 'A'];
      if ( cmb )
      {
        list[list.length() - 1] = cmb;
        present[cmb - 'A']++;
        present[last - 'A']--;
        continue;
      }
      bool opp = false;
      for ( int j='A'; j<='Z'; ++j )
      {
        if ( present[j - 'A'] > 0 and oppose[j - 'A'][word[i] - 'A'] )
        {
          opp = true;
          break;
        }
      }
      if ( opp )
      {
        list.clear();
        std::memset(present, 0, sizeof(present));
        continue;
      }
    }
    list.push_back(word[i]);
    present[word[i] - 'A']++;
  }
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t=1; t<=T; ++t )
  {
    std::string sim = read_data();
    simulate(sim);
    std::cout << "Case #" << t << ": [";
    for ( size_t i=0; i<list.length(); ++i )
    {
      if ( i > 0 )
        std::cout << ", ";
      std::cout << list[i];
    }
    std::cout << "]\n";
  }
  return 0;
}
