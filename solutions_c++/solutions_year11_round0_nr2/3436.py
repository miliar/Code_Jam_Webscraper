#include <list>
#include <iostream>
#include <map>
#include <string>
#include <fstream>
#include <stdlib.h>

#define LEN 256

static unsigned int letter[26];
static std::map<std::pair<char, char>, char> fusion;
static std::map<std::pair<char, char>, char> boom;
static std::list<char> list;

static inline void
parse_me(std::string filename);

static inline void
print_list(std::list<char> &li, int n);

static inline bool
check_boom(char c);



static inline bool
check_boom(char c)
{
  for (int i = 0; i < 26; ++i)
    {
      if (letter[i] > 0 && boom.count(std::pair<char,char>((i + 'A'), c)) > 0)
	{
	  list.clear();
	  for (int j = 0; j < 26; ++j)
	    letter[j] = 0;
	  return true;
	}
    }

  return false;
}

static inline void
print_list(std::list<char> &li, int n)
{
  std::cout << "Case #" << n << ": " ;
  std::cout << "[";

  if (li.size() > 0)
    {
      std::cout << li.front();
      li.pop_front();
    }

  while (li.size() > 0)
    {
      std::cout << ", " << li.front();
      li.pop_front();
    }

  std::cout << "]" << std::endl;
}

static inline void
parse_me(std::string filename)
{
  std::fstream file;
  char buf[LEN];
  int len;
  char old = 0;
  char c;

  file.open(filename.c_str());

  file.getline(buf, LEN);
  len = atoi(buf);

  for (int i = 0; i < len; ++i)
    {
      file.getline(buf, LEN, ' ');
      int n = atoi(buf);
      for (int j = 0; j < n; ++j)
	{
	  file.getline(buf, LEN, ' ');
	  std::pair<char, char> *d = new std::pair<char, char>(buf[0], buf[1]);
	  fusion.insert(std::pair<std::pair<char,char>,char>(*d, buf[2]));
	  d = new std::pair<char, char>(buf[1], buf[0]);
	  fusion.insert(std::pair<std::pair<char,char>,char>(*d, buf[2]));
	}
      file.getline(buf, LEN, ' ');
      n = atoi(buf);
      for (int j = 0; j < n; ++j)
	{
	  file.getline(buf, LEN, ' ');
	  std::pair<char, char> *d = new std::pair<char, char>(buf[0], buf[1]);
	  boom.insert(std::pair<std::pair<char,char>,char>(*d, ' '));
	  d = new std::pair<char, char>(buf[1], buf[0]);
	  boom.insert(std::pair<std::pair<char,char>,char>(*d, ' '));
	}
      file.getline(buf, LEN, ' ');
      n = atoi(buf);
      for (int j = 0; j < n; ++j)
	{
	  file.get(c);
	  if (old && fusion.count(std::pair<char, char>(old, c)) > 0)
	    {
	      char new_c = fusion.find(std::pair<char, char>(old, c))->second;
	      list.pop_back();
	      list.push_back(new_c);
	      letter[old - 'A'] -= 1;
	      letter[new_c - 'A'] += 1;
	      old = 0;
	    }
	  else if (check_boom(c))
	    {
	      old = 0;
	      continue;
	    }
	  else
	    {
	      letter[c - 'A'] += 1;
	      list.push_back(c);
	      old = c;
	    }
	}
      print_list(list, i + 1);
      for (int j = 0; j < 26; j++)
	letter[j] = 0;
      list.clear();
      boom.clear();
      fusion.clear();
      old = 0;
      file.getline(buf, LEN);
    }
  file.close();
}

int
main(int argc, char** argv)
{
  if (argc < 2)
    return 1;

  for (int i = 0; i < 26; ++i)
    letter[i] = 0;

  parse_me(argv[1]);

  return 0;
}
