#include <fstream>
#include <iostream>
#include <cassert>
#include <vector>
#include <map>
#include <string>

struct letter
{
public:

  letter() {}
  letter(char c) { add(c); }
  void add(char c) { choices_.push_back(c); }
  const std::vector<char> choices() const { return choices_; }
private:
  std::vector<char> choices_;
};

std::ostream& operator<<(std::ostream& os, const letter& l)
{
  if (l.choices().size() == 0)
    os << '-';
  if (l.choices().size() == 1)
    os << l.choices()[0];
  else
  {
    os << '(';
    for (unsigned i = 0; i < l.choices().size(); i++)
      os << l.choices()[i];
    os << ')';
  }
  return os;
}

std::ostream& operator<<(std::ostream& os, const std::vector<letter>& exp)
{
  for (unsigned i = 0; i < exp.size(); i++)
    os << exp[i];
  return os;
}

struct node;
struct node_ptr
{
  node_ptr() : p(0) {}
  node_ptr(const node_ptr& r) : p(r.p) {}
  node_ptr& operator=(const node_ptr& r) { p = r.p; return *this; }

  node* p;
};

struct node
{
public:
  node() {}
  node(char c_) : c(c_) {}
  void set(char c_) { c = c_; }
  std::map<char, node_ptr> childs() { return childs_; }
  node* set_child(char c)
  {
    if (!childs_[c].p)
      childs_[c].p = new node(c);
    return childs_[c].p;
  }
private:
  char c;
  std::map<char, node_ptr> childs_;
};

struct dico
{
public:
  dico(unsigned word_size_)
  : word_size(word_size_)
  {
  }

  void add_word(const std::string& word)
  {
    node* it = &root;
    for (unsigned i = 0; i < word.size(); i++)
      it = it->set_child(word[i]);
  }

  int matches(const std::vector<letter>& exp)
  {
    return matches_internal(0, exp, &root);
  }

private:
  int matches_internal(unsigned depth, const std::vector<letter>& exp, node*n)
  {
    assert(n);
    if (depth == word_size)
      return 1;

    unsigned s = 0;
    for (unsigned j = 0; j < exp[depth].choices().size(); j++)
    {
      node_ptr child = n->childs()[exp[depth].choices()[j]];
      if (child.p)
        s += matches_internal(depth + 1, exp, child.p);
    }
    return s;
  }
  node root;
  unsigned word_size;
};

int main(int argc, char* argv[])
{
  std::ifstream file_in(argv[1]);

  unsigned n_words, word_size, n_cases;

  file_in >> word_size;
  file_in >> n_words;
  file_in >> n_cases;

  dico dico(word_size);
  for (unsigned i = 0; i < n_words; i++)
  {
    std::string word;
    file_in >> word;
    dico.add_word(word);
  }

  for (unsigned j = 0; j < n_cases; j++)
  {
    std::string c;
    file_in >> c;
    std::vector<letter> exp;
    for (unsigned i = 0; i < c.size(); i++)
    {
      if (c[i] != '(' && c[i] != ')')
        exp.push_back(letter(c[i]));
      else
      {
        i++;
        letter l;
        while (c[i] != ')')
        {
          l.add(c[i]);
          i++;
        }
        exp.push_back(l);
      }

    }
    std::cout << "Case #" << (j + 1) << ": " << dico.matches(exp) << std::endl;
  }
}
