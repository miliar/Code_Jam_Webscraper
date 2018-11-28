#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <sstream>

std::vector<std::string> se, qu;


std::map<std::string, bool> working;

template<class T>
void Read(T &a)
{
  std::string s;
  std::getline(std::cin, s);
  std::istringstream i(s);
  i >> a;
}
  

std::vector<bool> searched;
template<class T>
void Fill(T &cont)
{
  cont.clear();
  int n;
  Read(n);
  while(n--)
  {
    std::string s;
    getline(std::cin, s);
    cont.push_back(s);
  }
}

void ClearSearch()
{
    working.clear();
    for(int i = 0; i < se.size(); i++)
    {
      working[se[i]] = false;
    }
}
void Solve()
{
  int N;
  Read(N);
  for (int i = 1; i <=N; ++i)
  {
    Fill(se);
    Fill(qu);
    ClearSearch();
    std::vector<std::string>::iterator it;
    std::map<std::string, bool>::iterator mit;
    int ns=0; // number of switches
    it = qu.begin();
    int enleft = se.size();
    while(it != qu.end())
    {
      mit = working.find(*it);
      if (mit != working.end())
      {
	if (!mit->second)
	{
	  mit->second = true;
	  --enleft;
	  if (enleft==0)
	  {
	    ClearSearch();
	    ++ns;
	    working[*it] = true;
	    enleft = se.size()-1;
	  }
	}
      }
      ++it;
    }
    std::cout << "Case #" <<i << ": " << ns <<std::endl;
  }
}

int main()
{
  Solve();
}
    
  
    
