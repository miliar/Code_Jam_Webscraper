#include <iostream>
#include <set>
#include <vector>
#include <iterator>
#include <algorithm>
#include <fstream>

using namespace std;
 
typedef std::set<int> set_type;
typedef std::set<set_type> powerset_type;
 
powerset_type powerset(set_type const& set)
{
  typedef set_type::const_iterator set_iter;
  typedef std::vector<set_iter> vec;
  typedef vec::iterator vec_iter;
 
  struct local
  {
    static int dereference(set_iter v) { return *v; }
  };
 
  powerset_type result;
 
  vec elements;
  do
  {
    set_type tmp;
    std::transform(elements.begin(), elements.end(),
                   std::inserter(tmp, tmp.end()),
                   local::dereference);
    result.insert(tmp);
    if (!elements.empty() && ++elements.back() == set.end())
    {
      elements.pop_back();
    }
    else
    {
      set_iter iter;
      if (elements.empty())
      {
        iter = set.begin();
      }
      else
      {
        iter = elements.back();
        ++iter;
      }
      for (; iter != set.end(); ++iter)
      {
        elements.push_back(iter);
      }
    }
  } while (!elements.empty());
 
  return result;
}

int get_sum(set_type s, vector<int> numbers)
{
 int sum = 0;
 for (set_type::iterator iter = s.begin(); iter != s.end(); ++iter)
 {
   sum ^= numbers[*iter];
 }
 return sum;
}

bool get_answer(set_type s, set_type complem, vector<int> numbers)
{
  int sum = get_sum(s, numbers);
  return (sum == get_sum(complem, numbers));
}

int get_normal_sum(set_type s, vector<int> numbers)
{
 int sum = 0;
 for (set_type::iterator iter = s.begin(); iter != s.end(); ++iter)
 {
   sum += numbers[*iter];
 }
 return sum;
}

 
int main()
{
  int cases_num;

  ifstream fin("input.txt");
  ofstream fout("output.txt");
  if (fin.is_open())
  {
    //cout << "file is open";
    fin >> cases_num;
    
    for (int i=0; i < cases_num; ++i)
    {
       
       int candies_num;
       fin >> candies_num;

       set_type test_set;
       vector<int> numbers;
       
       for (int x =0; x < candies_num; ++x)
       {
          test_set.insert(x);
          int candy;
          fin >> candy;
          //cout << "candy: " << candy << endl;
          numbers.push_back(candy);
       }
       
       
 
	  powerset_type test_powerset = powerset(test_set);
	  
	  int result = -1;
	  int final_sum = -1;

	  for (powerset_type::iterator iter = test_powerset.begin();
	       iter != test_powerset.end();
	       ++iter)
	  {
	    std::set<int> complement;
	    std::set_difference(test_set.begin(), test_set.end(), iter->begin(), iter->end(),
	    std::inserter(complement, complement.end()));
	    
	    if (iter->size() < 1 || complement.size() < 1) continue;

	    result = get_answer(*iter, complement, numbers);
	    if (result)
	    {
		int sum1 = get_normal_sum(*iter, numbers);
		int sum2 = get_normal_sum(complement, numbers);
		int tmp = (sum1 > sum2) ? sum1 : sum2;
		if (final_sum < tmp) final_sum = tmp;
	    }
	    
	  }
          
          if (final_sum == -1)
	     fout << "Case #" << i + 1 << ": "<< "NO" << endl;
          else
             fout << "Case #" << i + 1 << ": " << final_sum << endl;

    }
  }






   


  
}
