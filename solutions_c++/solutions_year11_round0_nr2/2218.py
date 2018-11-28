#include <iostream>
#include <algorithm>
#include <cstddef>
#include <list>
#include <cassert>
#include <map>
#include <set>
#include <string>
#include <sstream>
using namespace std;

char bases[] = { 'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F' };
set<char> base_set(bases, bases + sizeof(bases) / sizeof(bases[0]));

bool is_base(char c)
{
  return base_set.count(c) == 1;
}

string sorted_concat(char a, char b)
{
  if (a > b)
    swap(a, b);
  char buf[3] = { a, b, 0 };
  return string(buf);
}

class element_list
{
public:
  element_list()
  {
    clear();
  }

  void append(char c)
  {
    if (_list.size())
    {
      char back = _list.back();
      if (is_base(c) && is_base(back) && is_combination(c, back))
      {
        pop();
        append(_combinations[sorted_concat(c, back)]); 
      }
      else if (is_base(c) && contains_opposition(c))
      {
        clear();
      }
      else
      {
        _list.push_back(c);
        ++_count[c - 'A'];
      }
    }
    else
    {
      _list.push_back(c);
      ++_count[c - 'A'];
    }
  }

  void pop()
  {
    --_count[_list.back() - 'A']; 
    _list.pop_back();
  }

  size_t count_of(char c)
  {
    return _count[c - 'A'];
  }

  void clear()
  {
    _list.clear();
    std::fill(_count, _count + 26, 0);
  }

  string to_string()
  {
    std::stringstream ss;
    ss << '[';
    for (list<char>::iterator iter = _list.begin(); iter != _list.end();)
    {
      ss << *iter;
      if (++iter != _list.end())
        ss << ", ";
    }
    ss << "]";
    return ss.str();
  }

  void add_combination(char a, char b, char result)
  {
    _combinations[sorted_concat(a, b)] = result;
  }

  bool is_combination(char a, char b)
  {
    return _combinations.find(sorted_concat(a, b)) != _combinations.end();
  }

  void add_opposition(char a, char b)
  {
    _oppositions.insert(sorted_concat(a, b));
  }

  bool opposed(char a, char b)
  {
    return _oppositions.count(sorted_concat(a, b)) == 1;
  }

  bool contains_opposition(char a)
  {
    for (set<char>::iterator iter = base_set.begin(); iter != base_set.end(); ++iter)
    {
      if (a != *iter && count_of(*iter) && opposed(a, *iter))
      {
        return true;
      }
    }
    return false;
  }

private:
  std::list<char> _list;
  size_t _count[26];
  map<string, char> _combinations;
  set<string> _oppositions;
};

int main()
{
  size_t num_test_cases;
  cin >> num_test_cases;

  for (size_t i = 0; i < num_test_cases; ++i)
  {
    element_list list;

    size_t num_combinations;
    cin >> num_combinations;
    for (size_t j = 0; j < num_combinations; ++j)
    {
      char a, b, result;
      cin >> a >> b >> result;
      list.add_combination(a, b, result);
    }

    size_t num_oppositions;
    cin >> num_oppositions;
    for (size_t j = 0; j < num_oppositions; ++j)
    {
      char a, b;
      cin >> a >> b;
      list.add_opposition(a, b);
    }

    size_t num_invocations;
    cin >> num_invocations;
    for (size_t j = 0; j < num_invocations; ++j)
    {
      char invocation;
      cin >> invocation;
      list.append(invocation);
    }
    
    cout << "Case #" << i + 1 << ": " << list.to_string() << endl;
  }
}
