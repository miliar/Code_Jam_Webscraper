#include <list>
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <algorithm>

#define LEN 256

static std::list<std::pair<char, unsigned int>* > li;

static inline unsigned int
get_cycle(void);

static inline unsigned int
get_cycle(void)
{
  unsigned int cycle = 0;
  unsigned int tmp = 0;
  unsigned int pos[2] = {1, 1};
  bool go[2] = {false, false};
  char turn = 0;

  while (li.size() > 0)
    {
      std::pair<char, unsigned int> *p = li.front();
      if (!turn)
	{
	  turn = p->first;
	  tmp = abs(p->second - pos[turn - 'A']) + 1;
	}
      else if (turn == p->first)
	{
	  tmp += abs(p->second - pos[turn - 'A']) + 1;
	}
      else
	{
	  turn = p->first;
	  cycle += tmp;
	  tmp = 1 + std::max(abs(p->second - pos[turn - 'A']) - (int) tmp, 0);
	}
      go[turn - 'A'] = true;
      pos[turn - 'A'] = p->second;
      li.pop_front();
      delete p;
    }

  if (tmp)
    cycle += tmp;

  return cycle;
}

static void
parse_me(std::string filename)
{
  std::fstream file;
  char buf[LEN];
  unsigned int len;
  std::pair<char, unsigned int> *p;

  file.open(filename.c_str());

  file.getline(buf, LEN);
  len = atoi(buf);

  for (int i = 0; i < len; ++i)
    {
      file.getline(buf, LEN, ' ');
      int n = atoi(buf);
      for (int j = 1; j < n; ++j)
	{
	  p = new std::pair<char, unsigned int>;
	  file.getline(buf, LEN, ' ');
	  if (buf[0] == 'O')
	    p->first = 'A';
	  else
	    p->first = 'B';
	  file.getline(buf, LEN, ' ');
	  p->second = atoi(buf);
	  li.push_back(p);
	}
      p = new std::pair<char, unsigned int>;
      file.getline(buf, LEN, ' ');
      if (buf[0] == 'O')
	p->first = 'A';
      else
	p->first = 'B';
      file.getline(buf, LEN);
      p->second = atoi(buf);
      li.push_back(p);
      std::cout << "Case #" << i + 1 << ": " << get_cycle() << std::endl;
    }

  file.close();
}

int
main(int argc, char** argv)
{
  if (argc < 2)
    return 1;

  parse_me(argv[1]);

  return 0;
}
