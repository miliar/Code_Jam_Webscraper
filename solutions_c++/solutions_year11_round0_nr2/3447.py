#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

void		magicka(void);

int		main(void)
{
  int		T, Ti;

  scanf("%d", &T);
  for (Ti = 1; Ti <= T; ++Ti)
  {
    printf("Case #%d: ", Ti);
    magicka();
  }
  return 0;
}

int		index(char c)
{
  /*char foo[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
  int i = 0;

  for (i = 0; i < 8; ++i)
  {
    if (foo[i] == c) break;
  }
  return i;*/
  return (int) (c-'A');
}

void		print_list(vector<char>& list)
{
  cout << "[";
  for (vector<char>::iterator it = list.begin(); it != list.end(); ++it)
  {
    cout << (*it);
    if (it != list.end()-1) cout << ", ";
  }
  cout << "]" << endl;
}

void		magicka(void)
{
  char		combine[26][26];
  bool		opposed[26][26];
  int		present[26] = {0};
  int		T, Ti, Tj, Ilast, Icur;
  char		foo[5], cur, last = '#';
  vector<char>	list(0);
  string	res = "";

  for (int x = 0; x < 26; ++x)
  {
    for(int y = 0; y < 26; ++y)
    {
      combine[x][y] = '#';
      opposed[x][y] = false;
    }
  }
  // Combine parsing.
  scanf("%d ", &T);
  while (T --> 0)
  {
    scanf("%s ", foo);
    combine[index(foo[0])][index(foo[1])] = foo[2];
    combine[index(foo[1])][index(foo[0])] = foo[2];
  }

  // Opposed parsing.
  scanf("%d ", &T);
  while (T --> 0)
  {
    scanf("%s ", foo);
    opposed[index(foo[0])][index(foo[1])] = true;
    opposed[index(foo[1])][index(foo[0])] = true;
  }

  scanf("%d ", &T);
  while (T --> 0)
  {
    scanf("%c", &cur);
    Ilast = index(last);
    Icur = index(cur);
    if (last != '#' && combine[Icur][Ilast] != '#')
    {
      present[Ilast]--;
      list[list.size()-1] = combine[Icur][Ilast];
      present[index(combine[Icur][Ilast])]++;
    }
    else
    {
      for (Ti = 0; Ti < 26; ++Ti)
      {
	if (present[Ti] > 0 && opposed[Icur][Ti])
	{
	  for (Tj = 0; Tj < 26; ++Tj) present[Tj] = 0;
	  list.clear();
	  Ti = 42;
	  break;
	}
      }
      if (Ti != 42)
      {
	list.push_back(cur);
	present[Icur]++;
      }
    }
    if (list.size() != 0) last = list.back();
    else last = '#';
  }
  print_list(list);
}
