// exo2.cpp : Defines the entry point for the console application.
#include <vector>
#include <cmath>
#include <map>
#include <fstream>
#include <sstream>
#include <iostream>

struct triplet_s
{
  triplet_s(int a, int b, int c)
  {
    this->a = a;
    this->b = b;
    this->c = c;
  }

  int a;
  int b;
  int c;
};

void generate_normal_triplets(int score,
                              std::vector<triplet_s>& possible_triplets)
{
  for (int i = 0; i <= 10; ++i)
    for (int j = 0; j <= 10; ++j)
      for (int k = 0; k <= 10; ++k)
      {
        if (fabs(1.0f *i - j) > 1 || fabs(1.0f *i - k) > 1 || fabs(1.0f *j - k) > 1 ||
            i + j + k != score)
          continue;
        possible_triplets.push_back(triplet_s(i, j, k));
      }
}

void generate_surprising_triplets(int score,
                                  std::vector<triplet_s>& possible_triplets)
{
  for (int i = 0; i <= 10; ++i)
    for (int j = 0; j <= 10; ++j)
      for (int k = 0; k <= 10; ++k)
      {
        if (fabs(1.0f * i - j) > 2 || fabs(1.0f *i - k) > 2 || fabs(1.0f *j - k) > 2 ||
            i + j + k != score)
          continue;
        possible_triplets.push_back(triplet_s(i, j, k));
      }
}

bool valid_triplet(int score,
                   int best_result,
                   const std::map<int, std::vector<triplet_s> >& map)
{
  if (score > 30 || score < 0)
    return false;
    
  std::map<int, std::vector<triplet_s> >::const_iterator map_ite = map.find(score);

  if (map_ite == map.end())
    return false;
  const std::vector<triplet_s>& list = map_ite->second;
  for (auto i = list.begin(), end = list.end(); i != end; ++i)
  {
    if (i->a >= best_result || i->b >= best_result || i->c >= best_result)
      return true;
  }

  return false;
}

int count_candidate(const std::vector<int>& score_list,
                    int max_surprising,
                    int required_best_result,
                    const std::map<int, std::vector<triplet_s> >& normal_score_map,
                    const std::map<int, std::vector<triplet_s> >& surprising_score_map)
{
  int result = 0;

  for (auto i = score_list.begin(), end = score_list.end(); i != end; ++i)
  {
    if (valid_triplet(*i, required_best_result, normal_score_map))
    {
      ++result;
      continue;
    }
    if (max_surprising > 0 && valid_triplet(*i, required_best_result, surprising_score_map))
    {
      ++result;
      --max_surprising;
    }
  }
  return result;
}

int stoi(const std::string& elt)
{
  std::stringstream tmp;
  int result;

  tmp << elt;
  tmp >> result;
  return result;  
}

int main(int argc, char* argv[])
{
  std::map<int, std::vector<triplet_s> > normal_score_map;
  std::map<int, std::vector<triplet_s> > suprising_score_map;

  for (unsigned int i = 0; i <= 30; ++i)
  {
    std::vector<triplet_s>& normal_triplet_list = normal_score_map[i];
    std::vector<triplet_s>& suprising_triplet_list = suprising_score_map[i];

    generate_normal_triplets(i, normal_triplet_list);
    generate_surprising_triplets(i, suprising_triplet_list);
  }

  std::vector<int> score_list;
  int nb_cases = 0;  
  unsigned int result = 0;

  // I/O  
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

    int nb_googlers = 0;
    int max_surprising = 0;
    int required_best_result = 0;

    std::stringstream tmp;
    tmp << line;
    tmp >> nb_googlers;
    tmp >> max_surprising;
    tmp >> required_best_result;

    for (; nb_googlers > 0; --nb_googlers)
    {
      int elt;

      tmp >> elt;
      score_list.push_back(elt);
    }

    
    std::cout << "Case #" << i << ": " << count_candidate(score_list, max_surprising, required_best_result,
                                                          normal_score_map, suprising_score_map) << std::endl;
    score_list.clear();
  }

	return 0;

}
