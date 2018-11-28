#include <vector>
#include <iostream>
#include <cstdlib>

std::vector<char> robots;
std::vector<int> buttons;

int simulation()
{
  int posO = 1, posB = 1;
  int tmO = 0, tmB = 0;
  int tm = 0;
  for ( size_t i=0; i<robots.size(); ++i )
  {
    if ( robots[i] == 'O' )
    {
      int needed = std::abs(buttons[i] - posO) + 1 - tm + tmO;
      if ( needed < 1 )
        needed = 1;
      tm += needed;
      tmO = tm;
      posO = buttons[i];
    }
    else
    {
      int needed = std::abs(buttons[i] - posB) + 1 - tm + tmB;
      if ( needed < 1 )
        needed = 1;
      tm += needed;
      tmB = tm;
      posB = buttons[i];
    }
  }
  return tm;
}


void read_data()
{
  robots.clear();
  buttons.clear();
  int N;
  std::cin >> N;
  for ( int i=0; i<N; ++i )
  {
    std::string r;
    std::cin >> r;
    int b;
    std::cin >> b;
    robots.push_back(r[0]);
    buttons.push_back(b);
  }
}


int main()
{
  int T;
  std::cin >> T;
  for ( int t=1; t<=T; ++t )
  {
    read_data();
    int v = simulation();
    std::cout << "Case #" << t << ": " << v << '\n';
  }
  return 0;
}
