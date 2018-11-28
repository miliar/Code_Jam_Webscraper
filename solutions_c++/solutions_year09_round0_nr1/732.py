#include <iostream>
#include <vector>

int L, D, N;

std::vector<std::string> words;
int Do(const std::string &pat)
{
  std::vector<std::vector<bool> > pattern;
  std::string::const_iterator it = pat.begin();
  for (int i = 0; i < L; ++i)
  {
    std::vector<bool> p(32, false);
    int ch = *it++;
    if (ch =='(')
    {
      while( (ch = *it++)!=')')
	p[ch-'a'] = true;
    }else
      p[ch-'a'] = true;
    pattern.push_back(p);
  }

  int res = 0;
  for (int i = 0; i < D; ++i)
  {
    bool t = true;
    for (int j = 0; j < L; ++j)
      if (!pattern[j][words[i][j]-'a'])
      {
	//	std::cerr << j << std::endl;
	t = false;
	break;
      }
    res += t;
  }
  return res;
  
}  
      

int main()
{
  std::cin >> L >> D >> N;
  for (int i = 0; i < D; ++i)
  {
    std::string w;
    std::cin >> w;
    words.push_back(w);
  }
  for (int i = 0; i < N; ++i)
  {
    std::string pat;
    std::cin >> pat;
    int res = Do(pat);
    std::cout << "Case #" << (i+1) << ": " << res << std::endl;
  }
}
      
