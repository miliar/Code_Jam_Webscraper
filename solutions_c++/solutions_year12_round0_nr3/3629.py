
#include <iostream>
#include <fstream>
#include <sstream>

#include <set>

#undef min
#undef max

class SortedPair
{
  public:
    SortedPair(int a, int b)
    {
      _first = std::min(a, b);      
      _second = std::max(a, b);      
    }
    
    bool operator <(const SortedPair& other) const
    {
      if (_first < other._first)
        return true;
      if (_first == other._first)
        return _second < other._second;
      return false;
    }

    int first_get () const {return _first;}
    int second_get() const {return _second;}
  private:
    int _first;
    int _second;
};

int stringtoi(const std::string& elt)
{
  std::stringstream tmp;
  int result;

  tmp << elt;
  tmp >> result;
  return result;  
}

bool
rotate(const std::string& input, std::string& result)
{
  std::string tmp = input;

  if (!input.size())
    return false;
  tmp = input[input.size() - 1] + tmp;
  tmp = tmp.substr(0, tmp.size() - 1);
  result = tmp;
  return true;
}

void compute_permutations(int number,
                   int threshold,
                   std::set<SortedPair>& pairs)
{
  std::stringstream tmp;
  int nb_permutations = 0;
  std::string number_str;

  tmp << number;
  tmp >> number_str;

  if (number_str.size() <= 1)
    return;

  unsigned int nb_tentatives = static_cast<unsigned int> (number_str.size() - 1);  
  std::string current_str = number_str;

  for (unsigned int i = 0; i < nb_tentatives; ++i)
  {
    int new_number;
    
    rotate(current_str, current_str);
    new_number = stringtoi(current_str);
    if (new_number > number && new_number <= threshold)
    {
      pairs.insert(SortedPair(number, new_number));
    }
  }  
}

void generate_pairs(int a, int b,
                    std::set<SortedPair>& pairs)
{
  int total_permutations = 0;
  for (int i = a; i <= b; ++i)
  {
    compute_permutations(i, b, pairs);
  }
}

int main(int argc, char* argv[])
{
  int nb_cases = -1;
  std::set<SortedPair> pairs;
  
  if (argc < 2)
    return 1;

  std::fstream input_file (argv[1]);

  if (!input_file.is_open())
    return 2;

  std::stringstream tmp;
  std::string line;

  if (!getline(input_file, line))
  {
    std::cerr << "Could not read number of cases." << std::endl;
    return 3;
  }
  tmp << line;
  tmp >> nb_cases;

  if (nb_cases < 0)
    return 4;

  bool success = true;

  for (int i = 1; i <= nb_cases; ++i)
  {
    if (!getline(input_file, line))
    {
      std::cerr << "Unexpected EOF" << std::endl;
      return 5;
    }

    int nb_a = 0;
    int nb_b = 0;

    std::stringstream tmp;
    tmp << line;
    tmp >> nb_a;
    tmp >> nb_b;
    
    generate_pairs(nb_a, nb_b, pairs);

    std::cout << "Case #" << i << ": " << pairs.size() << std::endl;
    pairs.clear();
  }

	return 0;
}
